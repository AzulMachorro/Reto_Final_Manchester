import rclpy
import numpy as np
from std_msgs.msg import Float32
from rclpy.node import Node
from std_msgs.msg import String

class Process(Node):
    def __init__(self):
        super().__init__('process')
        self.sub = self.create_subscription(Float32, 'signal_params', self.listener_callback, 10)
        self.get_logger().info('process node initialized!!!')
        self.publisher = self.create_publisher(Float32, 'signal_reconstructed', 10)

        self.declare_parameter('phase_shift', 0.0)  # default PS
        self.declare_parameter('offset', 0.0)  # default offset
        self.declare_parameter('amplitude', -3.0)  # default amplitude

    def listener_callback(self, msg):

        offset = self.get_parameter('offset').get_parameter_value().double_value
        amplitude = self.get_parameter('amplitude').get_parameter_value().double_value
        phase_shift = self.get_parameter('phase_shift').get_parameter_value().double_value

        self.msg2 = Float32()
        self.msg1 = msg.data
        if not self.msg1:
            self.msg2.data = 0.0
        else:
            self.msg2.data = (self.msg1* amplitude ) + offset
        self.publisher.publish(self.msg2)       

def main(args=None):
    rclpy.init(args=args)
    m_s = Process()
    rclpy.spin(m_s)
    m_s.destroy_node()
    rclpy.shutdown()

if __name__ == 'main':
    main()