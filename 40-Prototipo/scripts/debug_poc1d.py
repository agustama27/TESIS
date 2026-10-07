import sys, warnings; warnings.filterwarnings("ignore")
sys.path.insert(0, "src")
import numpy as np
from bcibench import data, decoder
from sklearn.metrics import balanced_accuracy_score
from moabb.paradigms import MotorImagery
from moabb.datasets import BNCI2014_001
sd = data.load_subject(1)
p = MotorImagery(n_classes=2, events=["left_hand","right_hand"], fmin=8, fmax=30)
X, y, meta = p.get_data(BNCI2014_001(), subjects=[1])
tr = (meta.session=="0train").values
# --- comparar run 0 alineado (mi run0 tiene 23, MOABB 24: el ultimo se cayo por TOO_SHORT)
ep = data.epochs_of(sd["0train"]["0"]); Xe = ep.get_data(copy=False)*1e6
Xm = X[tr & (meta.run=="0").values]
cors = [np.corrcoef(Xe[i].ravel(), Xm[i].ravel())[0,1] for i in range(len(Xe))]
print("corr trial-a-trial run0 (min/median):", round(min(cors),3), round(float(np.median(cors)),3))
# --- mi pipeline con escala 1e6
trn = data.session_xy(sd, "0train"); tst = data.session_xy(sd, "1test")
for scale in (1.0, 1e6):
    d = decoder.train(1, trn.X*scale, trn.y)
    print(f"scale={scale:g}: bal.acc =", round(balanced_accuracy_score(tst.y, d.predict(tst.X*scale)),3))
