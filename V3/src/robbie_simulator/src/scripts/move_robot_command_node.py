import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class MoveRobotCommand(Node):
    def __init__(self):
        super().__init__('move_robot_command')
        self.publisher1 = self.create_publisher(Float64, '/robot_arm/joint1_position_controller/command', 10)
        self.publisher2 = self.create_publisher(Float64, '/robot_arm/joint2_position_controller/command', 10)
        self.publisher3 = self.create_publisher(Float64, '/robot_arm/joint3_position_controller/command', 10)
        self.publisher4 = self.create_publisher(Float64, '/robot_arm/joint4_position_controller/command', 10)
        
        # Example command values (you can set these as per your control strategy)
        self.joint_commands = {
            'joint1': 0.0,
            'joint2': 0.0,
            'joint3': 0.0,
            'joint4': 0.0
        }

        # Timer to publish commands periodically (you can use your own logic)
        self.timer = self.create_timer(1.0, self.publish_commands)

    def publish_commands(self):
        msg1 = Float64()
        msg1.data = self.joint_commands['joint1']
        msg2 = Float64()
        msg2.data = self.joint_commands['joint2']
        msg3 = Float64()
        msg3.data = self.joint_commands['joint3']
        msg4 = Float64()
        msg4.data = self.joint_commands['joint4']

        self.publisher1.publish(msg1)
        self.publisher2.publish(msg2)
        self.publisher3.publish(msg3)
        self.publisher4.publish(msg4)

def main(args=None):
    rclpy.init(args=args)
    node = MoveRobotCommand()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
