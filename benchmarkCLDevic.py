from CellModeller.Biophysics.BacterialModels.CLBacterium import CLBacterium
from CellModeller import Simulator
from CellModeller.Regulation.ModuleRegulator_standalone import ModuleRegulator
import numpy
import time
import pyopencl as cl

if __name__ == '__main__':

#     platform = cl.get_platforms()[0]
#     context = cl.Context(devices=[platform.get_devices()[1]])
#     kernel_src = open('CellModeller/Biophysics/BacterialModels/CLBacterium.cl', 'r').read()
#     program = cl.Program(context, kernel_src).build(cache_dir=False)


#### Benchmark on hold until I figure out why I get different results from CPU vs GPU
    sim=Simulator.Simulator(None,.2)
    biophys = CLBacterium(sim, max_substeps=8, max_cells=1000, max_contacts=32, max_sqs=192**2, jitter_z=False, reg_param=2, gamma=10)
    reg=ModuleRegulator(sim)
    sim.init(biophys, reg, None, None)
    sim.addCell(cellType=0, pos=(0,0,0))


    running = True


    ite = 0
    start=time.time()

    prevShapes=[]

    ### Main loop:
    while running:
        ite=ite+1
        sim.step()
        states = sim.cellStates
        #print(str(len(sim.cellStates)) +' cells')

        if ite >71:
            running=False

    print("Took ",time.time()-start)



