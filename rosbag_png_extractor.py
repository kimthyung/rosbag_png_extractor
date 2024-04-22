#!/usr/bin/env python3

"""Extract images from a rosbag.
"""

import os
import argparse
import cv2
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    """Extract a folder of images from a rosbag.
    """
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("bag_file", help="Input ROS bag.")
    parser.add_argument("output_dir", help="Output directory.")
    parser.add_argument("image_topic", help="Image topic.")

    args = parser.parse_args()

    print("Extract images from %s on topic %s into %s" % (args.bag_file, args.image_topic, args.output_dir))

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    bag = rosbag.Bag(args.bag_file, "r")
    bridge = CvBridge()
    count = 0
    for topic, msg, t in bag.read_messages(topics=[args.image_topic]):
        cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")

        # Write image with timestamp as filename

        filename = "%d.png" % t.to_nsec()
        cv2.imwrite(os.path.join(args.output_dir, filename), cv_img)
        
        # Also write the timestamp to a text file
        #with open(os.path.join(args.output_dir, str(t.to_nsec()) + ".txt"), "w") as f:
        #    time = str(msg.header.stamp.to_sec())
        #    f.write(time)
            
        print("Wrote image %s" % filename)

        count += 1

    bag.close()

    return

if __name__ == '__main__':
    main()

