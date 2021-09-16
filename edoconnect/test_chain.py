import matplotlib.pyplot as plt
import numpy as np
# IKPy imports
from ikpy import chain
from ikpy.utils import plot
from mpldatacursor import datacursor

def test_chain():

    #fig, ax = plot.init_3d_figure()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Change 3d figure

    edo_robot = chain.Chain.from_urdf_file(
        "../resources/edo_sim.urdf",
        base_elements=["base_link"])

    # Plot left arm
    print(f'joints = {len(edo_robot.links)}')
    joints = [0] * len(edo_robot.links)

    edo_robot.plot(joints, ax, show=True)
    datacursor(axes=ax)


if __name__ == '__main__':
    test_chain()
