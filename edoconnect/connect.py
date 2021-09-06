import sim


class EdoController:
    def __init__(self, Client_ID, joint_numbers, max_Vel):
        self.client_id = Client_ID
        self.joint_numbers = joint_numbers
        self.max_Vel = max_Vel
        self.joints_handles = self._get_joint_handles()
        self.initial_joints_relative_pos = self.get_joints_relative_position(operation_mode=sim.simx_opmode_streaming)
        self.initial_joint_pos = self.get_object_position(sim.simx_opmode_streaming)

    def _get_joint_handles(self):
        objects_handles = [sim.simxGetObjectHandle(self.client_id, f'joint_{i}',
                                                   sim.simx_opmode_oneshot_wait) for i in
                           range(1, self.joint_numbers + 1)]

        return [object[1] for object in objects_handles if object[0] == 0]

    def _set_upper_limit(self, joint):
        sim.simxSetObjectFloatParameter(self.client_id, joint, sim.sim_jointfloatparam_upper_limit, self.max_Vel,
                                            sim.simx_opmode_oneshot)

    def _set_target_position(self, joint, joint_mov):
        self._set_upper_limit(joint)
        if joint_mov is not None:
            return sim.simxSetJointTargetPosition(self.client_id, joint, joint_mov, sim.simx_opmode_oneshot)

    def _get_target_position(self, joint, operation_mode):
        ret, pos = sim.simxGetJointPosition(self.client_id, joint, operation_mode)
        return pos if ret == 0 else None

    def get_joints_relative_position(self, operation_mode=sim.simx_opmode_buffer):
        return [self._get_target_position(joint, operation_mode) for joint in self.joints_handles]

    def get_object_position(self, operation_mode=sim.simx_opmode_buffer):
        return [sim.simxGetObjectPosition(self.client_id, joint, -1, operation_mode)[1] for joint in self.joints_handles]

    def move_joints(self, j1_mov=None, j2_mov=None, j3_mov=None, j4_mov=None, j5_mov=None, j6_mov=None, j_mov_all=None):
        if j_mov_all is None:
            # Individual Movement for each Joint
            joint1, joint2, joint3, joint4, joint5, joint6 = self.joints_handles
            self._set_target_position(joint1, j1_mov)
            self._set_target_position(joint2, j2_mov)
            self._set_target_position(joint3, j3_mov)
            self._set_target_position(joint4, j4_mov)
            self._set_target_position(joint5, j5_mov)
            self._set_target_position(joint6, j6_mov)
        else:
            # Same Movement for all Joints
            for joint in self.joints_handles:
                self._set_target_position(joint, j_mov_all)

    def mov_cartesian(self, x, y, z):
        pass

    def mov_to_default_pos(self):
        pass

    def mov_cancel(self):
        pass
