import rclpy
import numpy as np
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32

class My_Publisher(Node):
    '''def _init_(self):
        super()._init_('talker_node')
        self.publisher = self.create_publisher(String, 'chit_chat', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Talker node successfully initialized!!!')
        self.msg = String()'''

    def __init__(self):
        super().__init__('signal_generator')
        self.publisher = self.create_publisher(Float32, 'signal', 10)
        timer_period = 0.01
        self.timer = self.create_timer(timer_period, self.timer_callback2)
        self.get_logger().info('signal node successfully initialized!!!')
        self.msg = Float32()
        self.i = 0
        
    def timer_callback2(self):
        self.msg.data = np.sin(np.pi*self.i) 
        ##self.msg.data = i
        self.publisher.publish(self.msg)
        self.i = self.i + 0.001 

    '''def timer_callback(self):
        self.msg.data = 'Hola :)'
        self.publisher.publish(self.msg)'''


def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()


if __name__ == 'main':    
    main()