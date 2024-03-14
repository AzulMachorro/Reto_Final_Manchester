import rclpy
import numpy as np
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32
from scipy import signal

class Setpoint(Node):

    def __init__(self):
        self.i = 0
        super().__init__('Azul_Setpoint')
        self.publisher = self.create_publisher(Float32, 'Azul_Setpoint', 10)
        #self.publisher2 = self.create_publisher(Float32, 'signal_params', 10)

        self.declare_parameter('type', 1) # default signal
        self.declare_parameter('frequency', 2.0)  # default frequency
        self.declare_parameter('offset', 0.0)  # default offset
        self.declare_parameter('amplitude', 0.5)  # default amplitude

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback2)
        self.get_logger().info('setpoint node successfully initialized!!!')
        self.msg = Float32()
        
        
    def timer_callback2(self):

        waveform = self.get_parameter('type').get_parameter_value().integer_value
        frequency = self.get_parameter('frequency').get_parameter_value().double_value
        frequency2 = 10
        offset = self.get_parameter('offset').get_parameter_value().double_value
        amplitude = self.get_parameter('amplitude').get_parameter_value().double_value

        if waveform == 1:
            self.msg.data = amplitude * np.sin(2 * np.pi * frequency * self.i + offset)
        elif waveform == 2:
            self.msg.data = amplitude * np.cos(2 * np.pi * frequency * self.i + offset)
        elif waveform == 3:
            self.msg.data = float(amplitude * signal.sawtooth(2 * np.pi * frequency * self.i + offset))
        elif waveform == 4:
            self.msg.data = float(amplitude * signal.square(2 * np.pi * frequency * self.i + offset))
        elif waveform == 5:
            self.msg.data = float(1)
        
        self.publisher.publish(self.msg)
        #self.publisher2.publish(self.msg)
        self.i = self.i + 0.001 


def main(args=None):
    rclpy.init(args=args)
    m_p = Setpoint()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()


if __name__ == 'main':    
    main()
