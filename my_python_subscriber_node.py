import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class MySubscriber(Node):
    def __init__(self):
        super().__init__("my_subscriber_node")
        self.subscriber = self.create_subscription(String, 'my_topic', self.receipt, 5)

    def receipt(self, msg):
        print(f"[INFO] [{format(time.time(),'0.7f')}] [listener]: I heard: {msg.data}")

def listener():
    rclpy.init()
    my_subscriber_object = MySubscriber()
    try:
        rclpy.spin(my_subscriber_object)
    except KeyboardInterrupt:
        print("Destroying node...")
        my_subscriber_object.destroy_node()
    finally:
        print("Bye bye!")

if __name__ == "__main__":
    listener()

