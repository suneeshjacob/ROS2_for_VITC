from flask import Flask, request
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class MyPublisher(Node):
    def __init__(self):
        super().__init__("my_publisher_node")
        self.publisher = self.create_publisher(String, 'my_topic', 5)
        #self.timer = self.create_timer(1, self.publish)
    def publish_received_message(self,message):
        msg = String()
        msg.data = message
        self.publisher.publish(msg)
        #print(f"[INFO] [{format(time.time(),'0.7f')}] [talker]: Publishing: {msg.data}")

rclpy.init()
my_publisher_object = MyPublisher()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def listener():    
    received_data = request.get_json()
    my_publisher_object.publish(f'Data received: {msg.data}')
    print(received_data)
    return 'Got it!'

if __name__ == "__main__":
    try:
        app.run(host="localhost", port=5000)
    except KeyboardInterrupt:
        my_publisher_object.destroy_node()
