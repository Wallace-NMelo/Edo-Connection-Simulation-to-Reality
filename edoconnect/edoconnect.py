import sim
from edoconstants import *
from edorobot import EdoRobot


class EdoController(EdoRobot):
    def __init__(self, Client_ID, joint_numbers=JOINTS_NUMBERS, max_Vel=MAX_JOINTS_VEL):
        # Connection to CoppeliaSim
        edo_robot = super(EdoRobot).__init__(Client_ID)
        self.joint_numbers = joint_numbers
        self.max_Vel = max_Vel
        self.joints_handles = self._get_joint_handles()
        self.initial_joints_relative_pos = self.get_joints_relative_position(operation_mode=sim.simx_opmode_streaming)
        self.initial_joint_pos = self.get_object_position(sim.simx_opmode_streaming)

        # # Simulation of movement from ikpy
        # self.urdf_file_path = urdf_file_path
        # self.base_elements = base_elements
        # self.chain = ikpy.chain.Chain.from_urdf_file(self.urdf_file_path, self.base_elements)
        # self.joints_numbers = len(self.chain.links)
        # self.initial_matrix = self.chain.forward_kinematics([0] * self.joints_numbers)
        # self.initial_pos = self._get_pos_from_matrix(self.initial_matrix)
        # self.initial_orient = self._get_orient_from_matrix(self.initial_matrix)

    # Relative to CoppeliaSim
    def _set_upper_limit(self, joint):
        sim.simxSetObjectFloatParameter(self.client_id, joint, sim.sim_jointfloatparam_upper_limit, self.max_Vel,
                                        sim.simx_opmode_oneshot)

    def _set_target_position(self, joint, joint_mov):
        self._set_upper_limit(joint)
        if joint_mov is not None:
            return sim.simxSetJointTargetPosition(self.client_id, joint, joint_mov, sim.simx_opmode_oneshot)

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
