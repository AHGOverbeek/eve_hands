# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float64
from halodi_msgs.msg import HandCommand

import time

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        self.publisher_thumb_r_ = self.create_publisher(HandCommand, '/bebionic/right/finger_thumb', 10)
        self.publisher_index_r_ = self.create_publisher(HandCommand, '/bebionic/right/finger_index', 10)
        self.publisher_middle_r_ = self.create_publisher(HandCommand, '/bebionic/right/finger_middle', 10)
        self.publisher_ring_r_ = self.create_publisher(HandCommand, '/bebionic/right/finger_ring', 10)
        self.publisher_little_r_ = self.create_publisher(HandCommand, '/bebionic/right/finger_little', 10)

        self.publisher_thumb_l_ = self.create_publisher(HandCommand, '/bebionic/left/finger_thumb', 10)
        self.publisher_index_l_ = self.create_publisher(HandCommand, '/bebionic/left/finger_index', 10)
        self.publisher_middle_l_ = self.create_publisher(HandCommand, '/bebionic/left/finger_middle', 10)
        self.publisher_ring_l_ = self.create_publisher(HandCommand, '/bebionic/left/finger_ring', 10)
        self.publisher_little_l_ = self.create_publisher(HandCommand, '/bebionic/left/finger_little', 10)

        timer_period = 2 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Initialize handcommand with max speed and force
        msg = HandCommand()
        msg.speed = 255.0
        msg.force = 100.0
        
        #  Open first
        msg.closure = 12000.0

        # Cannot publish at the same time (without explicit delay or time.sleep), otherwise only one is executed
        # The limit seems to be about 0.04s, only 25Hz
        delay = 0.05;

        # Right open fingers
        self.publisher_little_r_.publish(msg)
        time.sleep(delay)
        self.publisher_ring_r_.publish(msg)
        time.sleep(delay)
        self.publisher_middle_r_.publish(msg)
        time.sleep(delay)
        self.publisher_index_r_.publish(msg)
        time.sleep(delay)
        self.publisher_thumb_r_.publish(msg)
        time.sleep(delay)

        # Left open fingers
        self.publisher_thumb_l_.publish(msg)
        time.sleep(delay)
        self.publisher_index_l_.publish(msg)
        time.sleep(delay)
        self.publisher_middle_l_.publish(msg)
        time.sleep(delay)
        self.publisher_ring_l_.publish(msg)
        time.sleep(delay)
        self.publisher_little_l_.publish(msg)
        time.sleep(delay)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
