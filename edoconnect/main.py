import sim
from connect import EdoConnection


if __name__ == '__main__':
    print('Program Started')
    clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID != -1:
        print('Connected to remote API server')
    else:
        print('Failed connecting to remote API server')

    edo_robot = EdoConnection(Client_ID=clientID, joint_numbers=6, max_Vel=0.1)
    edo_robot.move_joints(j_mov_all=45)


