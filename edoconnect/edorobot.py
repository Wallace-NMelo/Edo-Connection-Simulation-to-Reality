import sim


class EdoRobot:
    def __init__(self, Client_ID, joint_numbers):
        self.client_id = Client_ID
        self.joint_numbers = joint_numbers
        self.joint_handles = self._get_joint_handles()

    def _get_joint_handles(self):
        objects_handles = [sim.simxGetObjectHandle(self.client_id, f'joint_{i}',
                                                   sim.simx_opmode_oneshot_wait) for i in
                           range(1, self.joint_numbers + 1)]

        return [object[1] for object in objects_handles if object[0] == 0]
