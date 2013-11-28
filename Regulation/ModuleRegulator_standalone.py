import copy
import os.path
import sys
import random

class ModuleRegulator:
    def __init__(self, sim, biophys=None, signalling=None):
        self.sim = sim
        self.cellStates = sim.cellStates
        self.biophys = biophys
        self.signal = signalling
        self.module = None
        self.reset()

    def addCell(self, cell):
        cell.targetVol = 2.5 + random.uniform(0.0,0.5)
        cell.growthRate = 2.0

    def reset(self):
        self.nSpecies = 0
        self.nSignals =0

    def setSignalling(self, signal):
        self.signal = signal

    def setIntegrator(self, integ):
        self.integ = integ

    def setBiophysics(self, biophys):
        self.biophys = biophys

    def initSpeciesLevels(self, levels):
        csv = self.cellStates.values()
        nCells = len(csv)
        for i in range(nCells):
            levels[i,:] = csv[i].species

    def step(self, dt=0):
        cells=self.cellStates
        for (id, cell) in cells.iteritems():
            cell.color = [cell.cellType*0.6+0.1, 1.0-cell.cellType*0.6, 0.3]
            #max(cell.startVol*2.0,0.0): #cell.startvol*2: #random.uniform(1.75,2.0):
            if cell.volume > cell.targetVol:
                a = 1#random.uniform(0.95,1.05)
                cell.asymm = [a,1]
                cell.divideFlag = True

    def divide(self, pState, d1, d2):
        d1.targetVol = 2.5 + random.uniform(0.0,0.5)
        d2.targetVol = 2.5 + random.uniform(0.0,0.5)


