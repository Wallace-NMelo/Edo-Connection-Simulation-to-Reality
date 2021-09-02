import sim
from connect import EdoConnection
import time

if __name__ == '__main__':
    print('Program Started')
    clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID != -1:
        print('Connected to remote API server')
    else:
        print('Failed connecting to remote API server')

    edo_robot = EdoConnection(Client_ID=clientID, joint_numbers=6, max_Vel=0.1)

    for i in range(60):
        print(f'{i}:{edo_robot.get_joints_relative_position()}')
        print(f'{i}: {edo_robot.get_object_position()}')
        time.sleep(1)
    #edo_robot.move_joints(j2_mov=360)
