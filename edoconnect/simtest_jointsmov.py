from edoSim import edosim
import time


def simtest_jointsmov():
    edosim_test = edosim()
    edosim_test.init6Axes()
    edosim_test.mov_to_default_pos()
    edosim_test.mov_joints_pos(0.5, 0.5, 0.5, 0.5, 0.5, 0.5)
    time.sleep(2)
    edosim_test.mov_joints_pos(0.5, 0.5, -0.5, -0.5, 0.5, 0.5)
    time.sleep(2)
    edosim_test.mov_joints_pos(-0.5, 0.5, 0.5, 0.5, 0.5, -0.5)
    time.sleep(2)
    edosim_test.mov_joints_pos(1, 0.5, 0.5, 0.5, 0.5, 1)
    time.sleep(2)
    edosim_test.mov_to_default_pos()
    time.sleep(2)
    edosim_test.finish()


if __name__ == '__main__':
    simtest_jointsmov()
