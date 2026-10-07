import sys, warnings; warnings.filterwarnings("ignore")
sys.path.insert(0, "src")
import numpy as np, mne
from bcibench import data
from moabb.paradigms import MotorImagery
from moabb.datasets import BNCI2014_001
sd = data.load_subject(1)
raw = sd["0train"]["0"]
ep = data.epochs_of(raw)
print("non-IGNORED drops:", [(i,d) for i,d in enumerate(ep.drop_log) if d and d!=('IGNORED',)])
print("first_samp:", raw.first_samp)
p = MotorImagery(n_classes=2, events=["left_hand","right_hand"], fmin=8, fmax=30)
X, y, meta = p.get_data(BNCI2014_001(), subjects=[1])
m = (meta.session=="0train") & (meta.run=="0")
Xm = X[m]
# mi raw filtrado igual que en epochs_of, canal eeg 0
r = raw.copy().pick(data.eeg_picks(raw)); r.filter(8,30,method="iir",verbose=False)
sig = r.get_data()[0]*1e6
t = Xm[0,0]
onset = int(round(raw.annotations.onset[0]*250))
best=[]
for lag in range(-1000, 3001, 1):
    s = onset+lag
    if s<0 or s+1001>len(sig): continue
    c = np.corrcoef(sig[s:s+1001], t)[0,1]
    best.append((c, lag))
best.sort(reverse=True)
print("best (corr, lag samples) vs annotation onset:", best[:3])
# tambien probar FIR
r2 = raw.copy().pick(data.eeg_picks(raw)); r2.filter(8,30,verbose=False)
sig2 = r2.get_data()[0]*1e6
best2=[]
for lag in range(-1000, 3001, 1):
    s = onset+lag
    if s<0 or s+1001>len(sig2): continue
    best2.append((np.corrcoef(sig2[s:s+1001], t)[0,1], lag))
best2.sort(reverse=True)
print("best with FIR filter:", best2[:3])
