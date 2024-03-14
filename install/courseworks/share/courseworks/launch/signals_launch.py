from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():

    signal_generator_node = Node(
        package='courseworks',
        executable='signal_generator',
        output='screen',
        parameters=[{'type': 1,
                     'frequency': 2.0,
                     'offset': 0.0,
                     'amplitude': 0.5,
                     }]#mandar parametros
    )

    process_node = Node(
        package='courseworks',
        executable='process',
        output='screen',
        parameters=[{'phase_shift': 0.0,
                     'offset': 0.0,
                     'amplitude': -3.0,
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

    ld = LaunchDescription([signal_generator_node,process_node,rqt_graph_node,rqt_plot_node])
    return ld