import rclpy #import rclpy for ros2 dependecies
import numpy as np #omport numpy for sin and cos functions
from rclpy.node import Node #import ros node from rclpy
from std_msgs.msg import String #import std_msg String msg type
from std_msgs.msg import Float32 #Import std_msg Float msg type
from scipy import signal #import scipy for signal generation


#Definition of node class Setpoint
class Setpoint(Node):

    #Constructur method for node class
    def __init__(self):
        #node counter
        self.i = 0
        #definition of topic
        super().__init__('Azul_Setpoint')
        #create publisher for topic Azul_Setpont
        self.publisher = self.create_publisher(Float32, 'Azul_Setpoint', 10)

        #Definition of parameters
        self.declare_parameter('type', 1) # default signal
        self.declare_parameter('frequency', 2.0)  # default frequency
        self.declare_parameter('offset', 0.0)  # default offset
        self.declare_parameter('amplitude', 0.5)  # default amplitude

        #Definition for timer period
        timer_period = 0.5

        #create timer for calback function
        self.timer = self.create_timer(timer_period, self.timer_callback2)
        #Print info to confirm node was made.
        self.get_logger().info('setpoint node successfully initialized!!!')
        #initialize msg data type
        self.msg = Float32()
        
    #method timer calback for node
    def timer_callback2(self):

        #get parameters for signal
        #wave form
        waveform = self.get_parameter('type').get_parameter_value().integer_value
        #frecuency
        frequency = self.get_parameter('frequency').get_parameter_value().double_value
        #frecuency 2
        frequency2 = 10
        #offset
        offset = self.get_parameter('offset').get_parameter_value().double_value
        #Amplitude for signal
        amplitude = self.get_parameter('amplitude').get_parameter_value().double_value

        #chooose type form ti send
        if waveform == 1:
            #Sin Fnc
            self.msg.data = amplitude * np.sin(2 * np.pi * frequency * self.i + offset)
        elif waveform == 2:
            #Cos Fnc
            self.msg.data = amplitude * np.cos(2 * np.pi * frequency * self.i + offset)
        elif waveform == 3:
            #Saw tooth Fnc
            self.msg.data = float(amplitude * signal.sawtooth(2 * np.pi * frequency * self.i + offset))
        elif waveform == 4:
            #Square pulse Fnc
            self.msg.data = float(amplitude * signal.square(2 * np.pi * frequency * self.i + offset))
        elif waveform == 5:
            #Constant signal
            self.msg.data = float(1)
        
        #Publish signal
        self.publisher.publish(self.msg)
        #Counter manipulation
        self.i = self.i + 0.001 


#Main Fnc
def main(args=None):
    #Inicialiation for rclpy 
    rclpy.init(args=args)
    #create node
    m_p = Setpoint()
    #Spin method for publisher calback
    rclpy.spin(m_p)
    #Destoy node
    m_p.destroy_node()
    #rclpy shutdown
    rclpy.shutdown()

#main call method
if __name__ == 'main':    
    main()
