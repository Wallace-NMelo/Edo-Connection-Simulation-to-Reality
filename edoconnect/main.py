import sim


class EdoConnection:
    def __init__(self, Client_ID, joint_numbers, max_Vel):
        self.client_id = Client_ID
        self.joint_numbers = joint_numbers
        self.max_Vel = max_Vel
        self.joint_handles = self._get_joint_handles()

    def _get_joint_handles(self):
        objects_handles = [sim.simxGetObjectHandle(clientID, f'joint_{i}',
                                                   sim.simx_opmode_oneshot_wait) for i in
                           range(1, self.joint_numbers + 1)]

        return [object[1] for object in objects_handles if object[0] == 0]

    def _set_upper_limit(self, joints):
        for joint in joints:
            sim.simxSetObjectFloatParameter(self.client_id, joint, sim.sim_jointfloatparam_upper_limit, self.max_Vel,
                                            sim.simx_opmode_oneshot)

    def _set_target_position(self, joint, joint_mov):
        if joint_mov is not None:
            sim.simxSetJointTargetPosition(self.client_id, joint, joint_mov, sim.simx_opmode_oneshot)

    def move_joints(self, j1_mov=None, j2_mov=None, j3_mov=None, j4_mov=None, j5_mov=None, j6_mov=None, j_mov_all=None):
        for joint in self.joint_handles:
            self._set_upper_limit(self.joint_handles)
            if j_mov_all is None:
                # Individual Movement for each Joint
                joint1, joint2, joint3, joint4, joint5, joint6 = self.joint_handles
                self._set_target_position(joint1, j1_mov)
                self._set_target_position(joint2, j2_mov)
                self._set_target_position(joint3, j3_mov)
                self._set_target_position(joint4, j4_mov)
                self._set_target_position(joint5, j5_mov)
                self._set_target_position(joint6, j6_mov)
            else:
                # Same Movement for all Joints
                for joint in self.joint_handles:
                    self._set_target_position(joint, j_mov_all)

    def mov_cartesian(self, x, y, z):
        pass

    def mov_to_default_pos(self):
        pass


if __name__ == '__main__':
    print('Program Started')
    clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID != -1:
        print('Connected to remote API server')
    else:
        print('Failed connecting to remote API server')

    edo_robot = EdoConnection(Client_ID=clientID, joint_numbers=6, max_Vel=0.1)
    edo_robot.move_joints(j_mov_all=45)


