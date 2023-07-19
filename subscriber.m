node = ros2node("message_receiver");
topic = "/hello_world";
sub = ros2subscriber(node,topic,@subscriber_callback);

function subscriber_callback(msg)
    disp(msg.data);
end
