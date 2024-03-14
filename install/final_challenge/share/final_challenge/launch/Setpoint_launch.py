from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():

    Setpoint_node = Node(
        package='final_challenge',
        executable='Setpoint',
        output='screen',
        parameters=[{'type': 1,
                     'frequency': 2.0,
                     'offset': 0.0,
                     'amplitude': 1.0,
                     }]#mandar parametros
    )

    rqt_graph_node = Node(
        package='rqt_graph',
        executable='rqt_graph',
        output='screen',
    )

    rqt_plot_node = Node(
        package='rqt_plot',
        executable='rqt_plot',
        output='screen',
    )

    ld = LaunchDescription([Setpoint_node,rqt_graph_node,rqt_plot_node])
    return ld