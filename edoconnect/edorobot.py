import ikpy

import sim
from edoconstants import *


class EdoRobot:
    def __init__(self, client_id, urdf_file_path=EDO_URDF_PATH, base_elements=EDO_BASE_ELEMENTS):
        # ikpy parameters
        self.urdf_file_path = urdf_file_path
        self.base_elements = base_elements
        self.chain = ikpy.chain.Chain.from_urdf_file(self.urdf_file_path, self.base_elements)
        self.joints_numbers = len(self.chain.links)
        self.initial_matrix = self.chain.forward_kinematics([0] * self.joints_numbers)
        self.initial_pos = self._get_pos_from_matrix(self.initial_matrix)
        self.initial_orient = self._get_orient_from_matrix(self.initial_matrix)

        # CoppeliaSim Parameters
        self.client_id = client_id
        self.joints = JOINTS_TEMPLATE

    def _get_pos_from_matrix(self, matrix):
        return matrix[:3, :3]

    def _get_orient_from_matrix(self, matrix):
        return matrix[:3, 3]

    def _get_joint_handles(self, joint_name):
        return sim.simxGetObjectHandle(self.client_id, joint_name, sim.simx_opmode_oneshot_wait)

    def _get_target_position(self, joint, operation_mode):
        ret, pos = sim.simxGetJointPosition(self.client_id, joint, operation_mode)
        return pos if ret == 0 else None

    def _get_relative_position(self, joint_handle, operation_mode=sim.simx_opmode_buffer):
        ret, rel_pos = self._get_target_position(joint_handle, operation_mode)
        return rel_pos if ret == 0 else None

    def _get_object_position(self, joint_handle, operation_mode=sim.simx_opmode_buffer):
        ret, obj_pos = sim.simxGetObjectPosition(self.client_id, joint_handle, -1, operation_mode)
        return obj_pos if ret == 0 else None

    def define_joints_handle(self):
        for joint_name, joint_param in self.joints.items():
            self.joints[joint_name]['object_handle'] = self._get_joint_handles(joint_name)

    def get_joints_object_pos(self):
        for joint_name, joint_param in self.joints.items():
            self.joints[joint_name]['object_pos'] = self._get_object_position(joint_param['object_handle'])

    def get_joints_rel_pos(self):
        for joint_name, joint_param in self.joints.items():
            self.joints[joint_name]['relative_pos'] = self._get_relative_position(joint_param['object_handle'])

    def run(self):
        self.define_joints_handle()
        self.get_joints_rel_pos()
        self.get_joints_object_pos()


if __name__ == '__main__':
    # test
    print('Program Started')
    clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID != -1:
        print('Connected to remote API server')
    else:
        print('Failed connecting to remote API server')

    edorobot = EdoRobot(client_id=clientID)
    edorobot.run()
    print(edorobot.joints)
