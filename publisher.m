node = ros2node("message_publisher");
topic = "/hello_world";
pub = ros2publisher(node,topic,"std_msgs/String");

msg = ros2message(pub);


for i = 1:100
    msg.data = strcat('Hello World: ',num2str(i));
    send(pub,msg);
    pause(1);
end
