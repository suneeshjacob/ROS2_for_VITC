node = ros2node("message_receiver");
topic = "/hello_world";
sub = ros2subscriber(node,topic,@subCallback);

function subCallback(msg)
    disp(msg.data);
end
