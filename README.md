# rosbag_png_extractor
extract image in png format in rosbag, and name the file in rosbag unix time

# How to execute 
python3 rosbag_png_extractor.py <your_bag_path.bag> <image_folder_path> <topic_you_want>

ex) python3 image_time_letgo.py /home/kth/Desktop/play_bag/S_KRUSN_DATA_SEAD-CM-2200-000_20240311162344.bag /home/kth/Desktop/play_bag/img0 camera_module_0

### pip install opencv-python rosbag cv-bridge
