import time

import sim, os
from edoconnect import EdoController

if __name__ == '__main__':
    print('Program Started')
    clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID != -1:
        print('Connected to remote API server')
    else:
        print('Failed connecting to remote API server')
    # sim.simxStopSimulation(clientID, sim.simx_opmode_oneshot_wait)
    # sim.simxStartSimulation(clientID, sim.simx_opmode_oneshot_wait)

    edo_robot = EdoController(Client_ID=clientID)
    edo_robot.move_joints(j2_mov=3.14 / 2)

    for i in range(60):
        print(f'{i}:{edo_robot.get_joints_relative_position()}')
        print(f'{i}: {edo_robot.get_object_position()}')
        os.system('clear')
        # print(f'{i}: {edo_robot.get_object_position()}')
        time.sleep(1)
    edo_robot.move_joints(j2_mov=-350)
