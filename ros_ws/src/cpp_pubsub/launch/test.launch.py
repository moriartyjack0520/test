from  launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cpp_pubsub',
            # node_namespace='pub',
            node_executable='talker',
            # node_name='talker_launch',
	    output='screen'
        ),
        Node(
            package='cpp_pubsub',
            # node_namespace='sub',
            node_executable='listener',
            # node_name='listener_launch',
	    output='screen'
        ),
    ])

