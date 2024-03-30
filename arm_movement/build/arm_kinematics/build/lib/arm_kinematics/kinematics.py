import serial
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

serial_name = "/dev/ttyACM0"

class ArmPublisher(Node):

	def __init__(self):
		super().__init__('arm_publisher')
		self.publisher_ = self.create_publisher(String, 'arm_topic', 10)
		self.serialport = serial.Serial(serial_name, 9600)
		timer_period = 0.5  # seconds
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0

	def timer_callback(self):
		msg = String()
		msg.data = 'Hello World: %d' % self.i
		self.publisher_.publish(msg)
		self.serialport.write(b'HI')
		self.get_logger().info('Publishing: "%s"' % msg.data)
		self.i += 1


def main(args=None):
	rclpy.init(args=args)

	arm_publisher = ArmPublisher()

	rclpy.spin(arm_publisher)
	arm_publisher.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()
