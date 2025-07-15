#This code has been obtained from source 20
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart

from launch_ros.actions import Node


def generate_launch_description():


    # 1. Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='my_bot'

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true', 'use_ros2_control': 'false'}.items()
    )

     # Include the joystick launch file (Source 22)
    joystick = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','joystick.launch.py'
                )]), launch_arguments={'use_sim_time': 'true', 'use_ros2_control': 'false'}.items()
    )

    # 2. Define the path to the Gazebo parameters file (Source 18)
    gazebo_params_file = os.path.join(get_package_share_directory(package_name),'config', 'gazebo_params.yaml')

        #Source 20:
        robot_description = Command('ros2 param get --hide /robot_state_publisher robot_description')

        controller_params_file = os.path.join(get_package_share_directory(package_name),'config', 'my_controllers.yaml')

        controller_manager = Node(
            package="controller_manager",
            executable="ros2_control_node",
            parameters=[{'robot_description': robot_description},
                        controller_params_file]
        )

        delayed_controller_manager = TimerAction(period=3.0,actions=[controller_manager])

    # 3. Differental drive controller spawner
        #Source 17:
        diff_drive_spawner = Node(
            package="controller_manager",
            executable="spawner.py",
            arguments=["diff_cont"],
        )

        #Source 20:
        delayed_diff_drive_spawner = RegisterEventHandler(
            event_handler=OnProcessStart(
                target_action=controller_manager,
                on_start=[diff_drive_spawner],
            )
        )

    # 4. Joint broad caster spawner
        #Source 17:
        joint_broad_spawner = Node(
            package="controller_manager",
            executable="spawner.py",
            arguments=["joint_broad"],
        )

        #Source 20:
        delayed_joint_broad_spawner = RegisterEventHandler(
            event_handler=OnProcessStart(
                target_action=controller_manager,
                on_start=[diff_drive_spawner],
            )
        )

    # 5. Launch them all!
    return LaunchDescription([
        rsp,
        joystick,
        delayed_controller_manager
        delayed_diff_drive_spawner,
        delayed_joint_broad_spawner
    ])