from edoSim import edosim
import time


def simtest_cartesian_mov():
    edosim_test = edosim()
    edosim_test.init6Axes()
    edosim_test.mov_to_default_pos()

    print(f'sphere = {edosim_test.sphere.init_pos}')
    x = -2.3703e-01
    y = +5.1957e-01
    z = +9.7262e-01
    delta = 0.5
    edosim_test.mov_to_default_pos()
    time.sleep(2)
    edosim_test.mov_cartesian(x, y, z)
    time.sleep(2)
    edosim_test.mov_cartesian(x + delta, +4.4457e-01, +9.7262e-01)
    time.sleep(2)
    edosim_test.mov_cartesian(x + delta, +4.4457e-01 - delta, +9.7262e-01)
    time.sleep(2)
    edosim_test.mov_cartesian(x, +4.4457e-01 - delta, +9.7262e-01)
    time.sleep(2)

    edosim_test.mov_to_default_pos()


if __name__ == '__main__':
    simtest_cartesian_mov()
