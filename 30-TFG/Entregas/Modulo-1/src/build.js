const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, Header, PageNumber,
  LineRuleType, HeadingLevel, PageBreak, TabStopType, Table, TableRow, TableCell,
  WidthType, BorderStyle,
} = require("docx");
const C = require("./contenido.js");

const FONT = "Times New Roman";
const SIZE = 24; // 12 pt
const MARGIN = 1701; // 3 cm en DXA (1 cm = 567)
const DOUBLE = { line: 480, lineRule: LineRuleType.AUTO, before: 0, after: 0 };
const INDENT = 709; // 1,25 cm

// *cursiva* -> runs
function runs(text, extra = {}) {
  const out = [];
  const parts = text.split(/(\*[^*]+\*)/g);
  for (const p of parts) {
    if (!p) continue;
    if (p.startsWith("*") && p.endsWith("*")) {
      out.push(new TextRun({ text: p.slice(1, -1), italics: true, font: FONT, size: SIZE, ...extra }));
    } else {
      out.push(new TextRun({ text: p, font: FONT, size: SIZE, ...extra }));
    }
  }
  return out;
}

function body(text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    spacing: DOUBLE,
    indent: { firstLine: INDENT },
    children: runs(text),
  });
}

function h1(text, pageBreak = true) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: DOUBLE,
    pageBreakBefore: pageBreak,
    children: [new TextRun({ text, bold: true, font: FONT, size: 28 })],
  });
}

function h2(text) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    spacing: DOUBLE,
    children: [new TextRun({ text, italics: true, font: FONT, size: SIZE })],
  });
}

function ref(text) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    spacing: DOUBLE,
    indent: { left: INDENT, hanging: INDENT },
    children: runs(text),
  });
}

const SINGLE = { line: 276, lineRule: LineRuleType.AUTO, before: 0, after: 0 };
const TEXTW = 11906 - 2 * MARGIN; // 8504
const NOB = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const LINE = { style: BorderStyle.SINGLE, size: 8, color: "000000" };

function cellPara(text, bold = false) {
  return new Paragraph({ alignment: AlignmentType.LEFT, spacing: SINGLE, children: runs(text, { bold, size: 22 }) });
}
function apaTable(tb) {
  const widths = [1300, 2000, 1450, 1750, 2004]; // suma 8504
  const mkRow = (cells, isHeader) => new TableRow({
    tableHeader: isHeader,
    children: cells.map((c, i) => new TableCell({
      width: { size: widths[i], type: WidthType.DXA },
      margins: { top: 60, bottom: 60, left: 80, right: 80 },
      borders: {
        top: isHeader ? LINE : NOB,
        bottom: isHeader ? LINE : NOB,
        left: NOB, right: NOB,
      },
      children: [cellPara(c, isHeader)],
    })),
  });
  const rows = [mkRow(tb.headers, true), ...tb.rows.map((r) => mkRow(r, false))];
  // borde inferior de la última fila
  const last = rows[rows.length - 1];
  const out = [
    new Paragraph({ alignment: AlignmentType.LEFT, spacing: { ...SINGLE, before: 240 }, children: [new TextRun({ text: tb.num, bold: true, font: FONT, size: SIZE })] }),
    new Paragraph({ alignment: AlignmentType.LEFT, spacing: { ...SINGLE, after: 120 }, children: [new TextRun({ text: tb.title, italics: true, font: FONT, size: SIZE })] }),
    new Table({
      width: { size: TEXTW, type: WidthType.DXA },
      columnWidths: widths,
      borders: { top: LINE, bottom: LINE, left: NOB, right: NOB, insideHorizontal: NOB, insideVertical: NOB },
      rows,
    }),
  ];
  if (tb.note) {
    out.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { ...SINGLE, before: 120, after: 240 },
      children: [new TextRun({ text: "Nota. ", italics: true, font: FONT, size: 22 }), ...runs(tb.note, { size: 22 })] }));
  } else {
    out.push(new Paragraph({ spacing: { ...SINGLE, after: 240 }, children: [] }));
  }
  return out;
}

function center(text, opts = {}) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: DOUBLE,
    children: [new TextRun({ text, font: FONT, size: opts.size || SIZE, bold: !!opts.bold })],
  });
}
function blank(n = 1) {
  return Array.from({ length: n }, () => new Paragraph({ spacing: DOUBLE, children: [new TextRun({ text: "", font: FONT, size: SIZE })] }));
}

// ---------- Portada ----------
const P = C.portada;
const portada = [
  ...blank(2),
  center(P.universidad, { bold: true, size: 28 }),
  center(P.carrera, { bold: true }),
  ...blank(2),
  center(P.materia, { bold: true }),
  center(P.modulo),
  ...blank(2),
  center(P.tipo),
  ...blank(1),
  center("Tema de investigación:", { bold: true }),
  center(P.tema, { bold: true, size: 28 }),
  ...blank(2),
  center(`Alumno: ${P.autor}`),
  center(`Legajo: ${P.legajo}`),
  center(`Profesor tutor: ${P.tutor}`),
  ...blank(1),
  center(`Fecha de entrega: ${P.fecha}`),
];

// ---------- Cuerpo ----------
const cuerpo = [];
cuerpo.push(h1("Introducción"));
for (const p of C.introduccion) cuerpo.push(body(p));

cuerpo.push(h1("Métodos"));
for (const item of C.metodos) {
  if (typeof item === "string") cuerpo.push(body(item));
  else if (item.h2) cuerpo.push(h2(item.h2));
  else if (item.table) cuerpo.push(...apaTable(item.table));
}

cuerpo.push(h1("Referencias"));
const refsSorted = [...C.referencias].sort((a, b) =>
  a.replace(/\*/g, "").localeCompare(b.replace(/\*/g, ""), "es", { sensitivity: "base" })
);
for (const r of refsSorted) cuerpo.push(ref(r));

// ---------- Documento ----------
const pageProps = {
  page: {
    size: { width: 11906, height: 16838 }, // A4
    margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN, header: 850 },
  },
  titlePage: true,
};

const headerNum = new Header({
  children: [
    new Paragraph({
      alignment: AlignmentType.RIGHT,
      children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: SIZE })],
    }),
  ],
});
const headerEmpty = new Header({ children: [new Paragraph({ children: [] })] });

const doc = new Document({
  creator: P.autor,
  title: P.tema,
  styles: {
    default: { document: { run: { font: FONT, size: SIZE } } },
  },
  sections: [
    {
      properties: { ...pageProps, titlePage: true },
      headers: { default: headerEmpty, first: headerEmpty },
      children: portada,
    },
    {
      properties: {
        ...pageProps,
        titlePage: false,
        pageNumberStart: 2,
      },
      headers: { default: headerNum },
      children: cuerpo,
    },
  ],
});

const outDir = process.argv[2] || __dirname;
const outFile = path.join(outDir, "Tamagusuku_Agustin - Entregable 1 - Introduccion y Metodos.docx");
Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outFile, buf);
  console.log("OK", outFile);
});
