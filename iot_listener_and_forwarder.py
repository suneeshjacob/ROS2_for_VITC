from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def listener():
    received_data = request.get_json()
    print(received_data)
    return 'Got it!'

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
