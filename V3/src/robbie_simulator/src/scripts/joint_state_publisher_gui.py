#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import tkinter as tk

class JointStatePublisherGUI(Node):
    def __init__(self):
        super().__init__('joint_state_publisher_gui')
        self.publisher = self.create_publisher(JointState, '/joint_states', 10)
        self.joint_names = ['joint1', 'joint2', 'joint3', 'joint4']  
        self.joint_positions = [0.0] * len(self.joint_names) 
        
        self.root = tk.Tk()
        self.root.title("Joint State Publisher GUI")
        self.sliders = []

        for i, joint in enumerate(self.joint_names):
            tk.Label(self.root, text=joint).pack()
            slider = tk.Scale(self.root, from_=-3.14, to=3.14, resolution=0.01, orient=tk.HORIZONTAL, command=self.update_joint(i))
            slider.pack()
            self.sliders.append(slider)

        self.root.after(100, self.publish_joint_states)
        self.root.mainloop()

    def update_joint(self, index):
        def callback(value):
            self.joint_positions[index] = float(value)
        return callback

    def publish_joint_states(self):
        joint_state = JointState()
        joint_state.header.stamp = self.get_clock().now().to_msg()
        joint_state.name = self.joint_names
        joint_state.position = self.joint_positions
        self.publisher.publish(joint_state)
        self.root.after(100, self.publish_joint_states)

def main(args=None):
    rclpy.init(args=args)
    node = JointStatePublisherGUI()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
