#import ros_actions for node
from launch_ros.actions import Node
#import launch description
from launch import LaunchDescription

#Generate launch description Fnc
def generate_launch_description():

    #launch node methd
    Setpoint_node = Node(
        #Definition for node parameters 
        package='final_challenge',
        executable='Setpoint',
        output='screen',
        parameters=[{'type': 1,
                     'frequency': 2.0,
                     'offset': 0.0,
                     'amplitude': 1.0,
                     }]#mandar parametros
    )

    #launch rqt_graph
    rqt_graph_node = Node(
        #definition for graph launch parameter
        package='rqt_graph',
        executable='rqt_graph',
        output='screen',
    )

    #launch rqt_plot 
    rqt_plot_node = Node(
        #definition for graph launch parameter
        package='rqt_plot',
        executable='rqt_plot',
        output='screen',
    )

    #creates the launcher 
    ld = LaunchDescription([Setpoint_node,rqt_graph_node,rqt_plot_node])
    #return launcher
    return ld