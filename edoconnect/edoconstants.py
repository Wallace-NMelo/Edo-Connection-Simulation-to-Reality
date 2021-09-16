# EDO Robot Constants

# COPPELIASIM PARAMETERS
JOINTS_NUMBERS = 6
MAX_JOINTS_VEL = 0.01
JOINTS_NAMES = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']
JOINT_PARAMETERS_TEMPLATE = {'object_handle': None, 'object_pos': 0, 'relative_pos': 0}
JOINTS_TEMPLATE = {'joint_1': JOINT_PARAMETERS_TEMPLATE, 'joint_2': JOINT_PARAMETERS_TEMPLATE,
                   'joint_3': JOINT_PARAMETERS_TEMPLATE, 'joint_4': JOINT_PARAMETERS_TEMPLATE,
                   'joint_5': JOINT_PARAMETERS_TEMPLATE, 'joint_6': JOINT_PARAMETERS_TEMPLATE}
# IKPY PARAMETERS
EDO_URDF_PATH = '../resources/edo_sim.urdf'
EDO_BASE_ELEMENTS = 'base_link'
