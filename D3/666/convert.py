import math
import numpy as np

path_r = "receiver_raw.bin"
path_t = "transmitter_raw.bin"

with open(path_r , "rb") as f1:
    receiver = f1.read()
with open(path_t , "rb") as f2:
    transmitter = f2.read()

def hex2bin(sift):
    out = []
    for he in sift:
        bi = "{:0>8}".format(bin(he)[2:])
        bi = np.array(list(bi))
        out.append(bi)
    return out

sift_r = np.array(hex2bin(receiver))
sift_t = np.array(hex2bin(transmitter))

judge = (sift_r == sift_t)

correct = np.sum(judge)
total = judge.shape[0] * judge.shape[1]

print("误码率:", (total - correct) / total)
