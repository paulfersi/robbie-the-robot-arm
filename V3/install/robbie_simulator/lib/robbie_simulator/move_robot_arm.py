#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class MoveRobotArm(Node):
    def __init__(self):
        super().__init__('move_robot_arm')
        self.publisher1 = self.create_publisher(Float64, '/robot_arm/joint1_position_controller/command', 10)
        self.publisher2 = self.create_publisher(Float64, '/robot_arm/joint2_position_controller/command', 10)
        self.publisher3 = self.create_publisher(Float64, '/robot_arm/joint3_position_controller/command', 10)
        self.publisher4 = self.create_publisher(Float64, '/robot_arm/joint4_position_controller/command', 10)
        self.timer = self.create_timer(0.1, self.move_arm)

    def move_arm(self):
        msg1 = Float64()
        msg2 = Float64()
        msg3 = Float64()
        msg4 = Float64()

<<<<<<< HEAD
        msg1.data = 1.0 
=======
        msg1.data = 1.0  # Replace with the desired joint angle
>>>>>>> dev
        msg2.data = 0.5
        msg3.data = 0.0
        msg4.data = -1.0

        self.publisher1.publish(msg1)
        self.publisher2.publish(msg2)
        self.publisher3.publish(msg3)
        self.publisher4.publish(msg4)

def main(args=None):
    rclpy.init(args=args)
    node = MoveRobotArm()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
