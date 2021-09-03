# dcd.py

import struct


refpdb = "file.pdb"
natoms = len([x for x in open(refpdb)])
dcdfile = "file.dcd"
B = open(dcdfile, "rb").read()
crds = B[300:len(B)]
nframes = int(len(crds) / (natoms * 3. * 4.)) 
X = []
Y = []
Z = []
byte = 0
for frame in range(nframes):
    X.append([])
    Y.append([])
    Z.append([])
    atx = []
    aty = []
    atz = []
    for atom in range(natoms):
        crdx = list(struct.unpack("<f", crds[60+byte:64+byte]))[0]
        atx.append(crdx)
        byte += 4
    byte += 8
    for atom in range(natoms):
        crdy = list(struct.unpack("<f", crds[60+byte:64+byte]))[0]
        aty.append(crdy)
        byte += 4
    byte += 8
    for atom in range(natoms):
        crdz = list(struct.unpack("<f", crds[60+byte:64+byte]))[0]
        atz.append(crdz)
        byte += 4
    byte += 8
    for atom in range(natoms):
        X[-1].append(atx[atom])
        Y[-1].append(aty[atom])
        Z[-1].append(atz[atom])
trj = [list(zip(X[frame], Y[frame], Z[frame])) for frame in range(nframes)]
