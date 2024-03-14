import rclpy
import numpy as np
from std_msgs.msg import Float32
from rclpy.node import Node
from std_msgs.msg import String

class My_Subscriber(Node):
    def __init__(self):
        super()._init_('process')
        self.sub = self.create_subscription(Float32, 'signal', self.listener_callback, 10)
        self.get_logger().info('process node initialized!!!')
        self.publisher = self.create_publisher(Float32, 'proc_signal', 10)

    def listener_callback(self, msg):
        self.msg2 = Float32()
        self.msg1 = msg.data
        ##self.get_logger().info('Chisme: {}'.format(msg.data))
        self.msg2.data = self.msg1 * -3 
        self.publisher.publish(self.msg2)       

def main(args=None):
    rclpy.init(args=args)
    m_s = My_Subscriber()
    rclpy.spin(m_s)
    m_s.destroy_node()
    rclpy.shutdown()

if __name__ == 'main':
    main()