from edoSim import edosim
import time


def simtest_cartesian_mov():
    edosim_test = edosim()
    edosim_test.init6Axes()
    edosim_test.mov_to_default_pos()

    time.sleep(2)

    time.sleep(2)

    time.sleep(2)

    time.sleep(2)
    edosim_test.mov_to_default_pos()


if __name__ == '__main__':
    simtest_cartesian_mov()
