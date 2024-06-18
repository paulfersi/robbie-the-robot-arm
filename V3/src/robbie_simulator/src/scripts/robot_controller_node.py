import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.subscription1 = self.create_subscription(Float64, '/robot_arm/joint1_position_controller/command', self.move_joint1, 10)
        self.subscription1  # prevent unused variable warning
        self.subscription2 = self.create_subscription(Float64, '/robot_arm/joint2_position_controller/command', self.move_joint2, 10)
        self.subscription2  # prevent unused variable warning
        self.subscription3 = self.create_subscription(Float64, '/robot_arm/joint3_position_controller/command', self.move_joint3, 10)
        self.subscription3  # prevent unused variable warning
        self.subscription4 = self.create_subscription(Float64, '/robot_arm/joint4_position_controller/command', self.move_joint4, 10)
        self.subscription4  # prevent unused variable warning

        # Initial joint positions
        self.joint_positions = {
            'joint1': 0.0,
            'joint2': 0.0,
            'joint3': 0.0,
            'joint4': 0.0
        }

        # Joint state publisher
        self.joint_state_publisher = self.create_publisher(JointState, '/joint_states', 10)
        self.timer = self.create_timer(0.1, self.publish_joint_states)  # Adjust rate as needed

    def move_joint1(self, msg):
        self.joint_positions['joint1'] = msg.data

    def move_joint2(self, msg):
        self.joint_positions['joint2'] = msg.data

    def move_joint3(self, msg):
        self.joint_positions['joint3'] = msg.data

    def move_joint4(self, msg):
        self.joint_positions['joint4'] = msg.data

    def publish_joint_states(self):
        joint_state_msg = JointState()
        joint_state_msg.header.stamp = self.get_clock().now().to_msg()

        joint_state_msg.name = ['joint1', 'joint2', 'joint3', 'joint4']
        joint_state_msg.position = [
            self.joint_positions['joint1'],
            self.joint_positions['joint2'],
            self.joint_positions['joint3'],
            self.joint_positions['joint4']
        ]
        joint_state_msg.velocity = [0.0, 0.0, 0.0, 0.0]  # Example: set velocities if available
        joint_state_msg.effort = [0.0, 0.0, 0.0, 0.0]    # Example: set efforts if available

        self.joint_state_publisher.publish(joint_state_msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
