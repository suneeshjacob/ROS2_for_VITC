from flask import Flask, request
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class MyPublisher(Node):
    def __init__(self):
        super().__init__("my_publisher_node")
        self.publisher = self.create_publisher(String, 'my_topic', 5)
    def publish_received_message(self,message):
        msg = String()
        msg.data = message
        self.publisher.publish(msg)

rclpy.init()
my_publisher_object = MyPublisher()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def listener():
    received_data = request.get_json()
    my_publisher_object.publish_received_message(f"Data received: {received_data['data']}")
    return 'Got it!'


try:
    app.run(host="localhost", port=5000)
except KeyboardInterrupt:
    my_publisher_object.destroy_node()
