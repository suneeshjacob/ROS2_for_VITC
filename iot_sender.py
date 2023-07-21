import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
import json
import time

url = 'https://8863-49-37-148-1.ngrok.io/'
headers = {'Content-Type':'application/json'}
data = lambda msg: {'data' : {msg.data}'}

class MySubscriber(Node):
    def __init__(self):
        super().__init__("my_subscriber_node")
        self.subscriber = self.create_subscription(String, 'my_topic', self.receipt, 5)

    def receipt(self, msg):
	json_data = json.dumps(data(msg))
	r = requests.post(url, headers = headers, data = json_data)
	time.sleep(1)
        


rclpy.init()
my_subscriber_object = MySubscriber()
try:
	rclpy.spin(my_subscriber_object)
except KeyboardInterrupt:
	my_subscriber_object.destroy_node()
