import sys, os
import win32com.client

docx = os.path.abspath(sys.argv[1])
pdf = os.path.splitext(docx)[0] + ".pdf"
word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
try:
    doc = word.Documents.Open(docx, ReadOnly=True)
    pages = doc.ComputeStatistics(2)  # wdStatisticPages
    words = doc.ComputeStatistics(0)  # wdStatisticWords
    doc.SaveAs2(pdf, FileFormat=17)   # wdFormatPDF
    doc.Close(False)
    print(f"PDF OK: {pdf}\npages={pages} words={words}")
finally:
    word.Quit()
