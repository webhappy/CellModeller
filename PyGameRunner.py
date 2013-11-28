from CellModeller.Biophysics.BacterialModels.CLBacterium import CLBacterium
from CellModeller import Simulator
from CellModeller.Regulation.ModuleRegulator_standalone import ModuleRegulator
import numpy
from visual import *

max_cells = 400000

if __name__ == '__main__':

    sim=Simulator.Simulator(None,1)
    biophys = CLBacterium(sim, max_substeps=8, max_cells=max_cells, max_contacts=32, max_sqs=192**2, jitter_z=False, reg_param=2, gamma=10)
    reg=ModuleRegulator(sim)
    sim.init(biophys, reg, None, None)
    sim.addCell(cellType=0, pos=(0,0,0))


    running = True
    w=window()
    scene=display(window=w)
    scene.title='Test'

    ite = 0
    scene.range=20; #zoom out

    prevShapes=[]

    ### Main loop:
    while running:
        ite=ite+1
        sim.step()
        states = sim.cellStates
        #print(str(len(sim.cellStates)) +' cells')

        if (ite%5) == 0:
            rate(100)
            for obj in prevShapes:
                obj.visible=False
                del obj
            prevShapes=[]

            cells = sim.cellStates.values()
            print "Dumping cell stats at iteration=",ite
            for cell in cells:
                l = cell.length
                # r = cell.radius*2.0
                r = cell.radius

                (e1, e2) = cell.ends
                ae1 = numpy.array(e1)
                ae2 = numpy.array(e2)
                zaxis = numpy.array([0, 0, 1])
                caxis = numpy.array(cell.dir)  # (ae2-ae1)/l
                rotaxis = numpy.cross(caxis, zaxis)
                rotangle = numpy.arccos(numpy.dot(caxis, zaxis))
                print cell.length,cell.radius

                start=ae1
                cax=(ae2-ae1)
                prevShapes.append(cylinder(pos=ae1,axis=cax,radius=cell.radius))
                prevShapes.append(sphere(pos=ae1,radius=cell.radius))
                prevShapes.append(sphere(pos=ae2,radius=cell.radius))

        if ite >350:
            running=False



