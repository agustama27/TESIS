"""Diagnóstico: imprime marcas de tiempo crudas de marcadores y EEG por 12 s."""
import os, subprocess, sys, time
import numpy as np
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
from mne_lsl.lsl import StreamInlet, local_clock, resolve_streams

exec_id = f"dbg-{int(time.time())}"
env = dict(os.environ, PYTHONPATH=os.path.join(ROOT, "src"))
prod = subprocess.Popen([sys.executable, "-m", "bcibench.replay", "--subject", "1", "--run", "0",
                         "--exec-id", exec_id, "--outdir", os.path.join(ROOT, "results", "smoke", exec_id),
                         "--max-seconds", "12"], env=env, cwd=ROOT, stderr=subprocess.DEVNULL)

def res(name):
    for _ in range(60):
        s = resolve_streams(timeout=1.0, name=name)
        if s: return s[0]
    raise SystemExit("no stream " + name)
e = StreamInlet(res(f"{exec_id}-eeg"), recover=True); m = StreamInlet(res(f"{exec_id}-markers"), recover=True)
e.open_stream(); m.open_stream()
print("consumer local_clock at open:", round(local_clock(), 3))
first = None; last = None; n = 0; t_end = local_clock() + 16
while local_clock() < t_end:
    ms, mts = m.pull_chunk(timeout=0.0)
    for s, ts in zip(np.asarray(ms).reshape(-1), mts):
        print(f"MARKER code={int(s)} ts={ts:.3f} now={local_clock():.3f} type={type(ts).__name__}")
    xs, ts = e.pull_chunk(timeout=0.0, max_samples=4096)
    if len(ts):
        ts = np.asarray(ts, dtype=float)
        if first is None:
            first = ts[0]; print("EEG first ts:", round(first, 3), "shape xs:", np.asarray(xs).shape, "ts dtype:", ts.dtype, "now:", round(local_clock(), 3))
        last = ts[-1]; n += len(ts)
    time.sleep(0.005)
print("EEG n:", n, "first:", round(first, 3), "last:", round(last, 3), "span:", round(last - first, 3))
prod.wait()
