import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class My_Talker_Params(Node):
    def __init__(self):
        super().__init__('my_talker_params_node')#asi aparece
        self.declare_parameter('my_param', 'mundo')#valor parametro default
        self.pub = self.create_publisher(String, 'chit_chat',10)#nombre del canal publicador
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Talker params node initialized')#mensaje inicializado
        self.msg = String()

    def timer_callback(self):
        #parametro de la etiqueta
        my_param = self.get_parameter('my_param').get_parameter_value().string_value
        self.msg.data = 'Hola {}'.format(my_param)#nuevo mensaje
        self.pub.publish(self.msg)    

def main(args = None):
    rclpy.init(args=args)
    m_t_p=My_Talker_Params()
    rclpy.spin(m_t_p)
    m_t_p.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
