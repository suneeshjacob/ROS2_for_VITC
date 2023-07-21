import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
import json
import time

class MySubscriber(Node):
    def __init__(self):
        super().__init__("my_subscriber_node")
        self.subscriber = self.create_subscription(String, 'my_topic', self.receipt, 5)

    def receipt(self, msg):
        print(f"[INFO] [{format(time.time(),'0.7f')}] [listener]: I heard: {msg.data}")

url = 'https://8863-49-37-148-1.ngrok.io/'
headers = {'Content-Type':'application/json'}
data = lambda number: {'data' : f'Hello World: {number}'}

for i in range(100):
	json_data = json.dumps(data(i+1))
	r = requests.post(url, headers = headers, data = json_data)
	time.sleep(1)
