# This file introduces controller startup [Source 21]
from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    joy_params = os.path.join(get_package_share_directory('my_bot'), 'config', 'joystick.yaml')

    joy_node = Node(
        package='joy',
        executable='joy_node',
        parameters=[joy_params, {'use_sim_time': use_sim_time}],
    )

    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_node',
        parameters=[joy_params, {'use_sim_time': use_sim_time}],
        remappings=[('/cmd_vel', '/diff_cont/cmd_vel_unstamped')],
    )

    # Provisions for mobile control (Source 22)
    #twist_stamper = Node(
        #package='twist_stamper',
        #executable='twist_stamper,
        #parameters=[joy_params, {'use_sim_time': use_sim_time}],
        #remappings=[('/cmd_vel_in', '/diff_cont/cmd_vel_unstamped'),('/cmd_vel_out', '/diff_cont/cmd_vel')],
    #)

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),
        joy_node,
        teleop_node,
        #twist_stamper #Provisions for mobile control (Source 22)
    ])