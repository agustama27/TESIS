import sys, os, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, "src")
import numpy as np, mne
from bcibench import data, decoder
sd = data.load_subject(1)
print("sessions:", list(sd.keys()), "runs:", list(sd[data.SESSION_TRAIN].keys()))
raw = sd[data.SESSION_TRAIN]["0"]
print("ch types:", {t: raw.get_channel_types().count(t) for t in set(raw.get_channel_types())})
print("sfreq:", raw.info["sfreq"], "duration s:", raw.times[-1])
ann = raw.annotations
print("n annotations:", len(ann), "descs:", sorted(set(ann.description)))
print("first onsets:", np.round(ann.onset[:5], 2), "durations:", np.round(ann.duration[:5], 2))
ev = data.events_of(raw)
print("events shape:", ev.shape, "codes:", np.unique(ev[:,2], return_counts=True))
d = raw.get_data(picks=data.eeg_picks(raw))
print("EEG scale (median abs):", np.median(np.abs(d)))
# MOABB ground truth
from moabb.paradigms import MotorImagery
from moabb.datasets import BNCI2014_001
p = MotorImagery(n_classes=2, events=["left_hand","right_hand"], fmin=8, fmax=30)
X, y, meta = p.get_data(BNCI2014_001(), subjects=[1])
print("MOABB X:", X.shape, "y:", np.unique(y, return_counts=True), "sessions:", meta.session.unique())
tr = meta.session == "0train"; te = ~tr
m = decoder.make_pipeline().fit(X[tr], y[tr])
from sklearn.metrics import balanced_accuracy_score
print("MOABB paradigm CSP+LDA bal.acc:", balanced_accuracy_score(y[te], m.predict(X[te])))
print("MOABB epoch length samples:", X.shape[-1], " mine tmin/tmax:", data.TMIN, data.TMAX)
