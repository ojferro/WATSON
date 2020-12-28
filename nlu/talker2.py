import rospy
import std_msgs.msg
#import geometry_msgs.msg

pub = rospy.Publisher('chattering', std_msgs.msg.String, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10) # 10hz
while not rospy.is_shutdown():
    text = "Hello, WATSON"
    rospy.loginfo(text)
    pub.publish(text)
    rate.sleep()

