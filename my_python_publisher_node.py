import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class MyPublisher(Node):
    def __init__(self):
        super().__init__("my_publisher_node")
        self.publisher = self.create_publisher(String, 'my_talker', 5)
        self.timer = self.create_timer(1, self.publish)
        self.counter = 0
    def publish(self):
        msg = String()
        msg.data = f"'Hello World: {self.counter}'"
        self.publisher.publish(msg)
        print(f"[INFO] [{format(time.time(),'0.7f')}] [talker]: Publishing: {msg.data}")
        self.counter += 1

def talker():
    rclpy.init()
    my_publisher_object = MyPublisher()
    try:
        rclpy.spin(my_publisher_object)
    except KeyboardInterrupt:
        print("Destroying node...")
        my_publisher_object.destroy_node()
    finally:
        print("Bye bye!")

if __name__ == "__main__":
    talker()

