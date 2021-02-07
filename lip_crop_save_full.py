# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 00:21:30 2019

@author: bnone
"""

import os
import cv2
from mtcnn import MTCNN


detector = MTCNN()

s = 0

data_path = "../data"
videos_path = os.path.join(data_path,'VIDEOS')

assert os.path.isdir(videos_path)

frames_path = os.path.join(data_path,'FRAMES')

image_list = []
video_counter = 0
assert os.path.isdir(videos_path)
for video in os.listdir(videos_path):
    
	if video.endswith('mp4'):
        print("Video: " + video + " loaded!")
        video_counter += 1
        video_path = os.path.join(videos_path, video)
        video_frame_path = os.path.join(frames_path, video[:-4])
        video_number = video.split('_')[0]
        
        if not os.path.exists(video_frame_path):
            os.mkdir(video_frame_path)
            print("Directory " , video_frame_path ,  " Created ")    
        
        video_capture = cv2.VideoCapture(video_path)
        count = 0
        
        while True:
            retval, image = video_capture.read()
            
            if not retval: # retval will be True as long as the video plays
                "end of video"
                break
            
#            image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            if not (count+1) % 25:
                print ('Video: ' + str(video_counter) + '    Frame: ' + str(count+1) + ' captured...')
            
            result = detector.detect_faces(image)
            
            if not len(result) :
                try:
                    for person in result:    # to work with multiple faces
						keypoints = person['keypoints']
						lx1,ly1 = keypoints["mouth_left"]
						lx2,ly2 = keypoints["mouth_right"]
						m = (lx2-lx1) // 6
						lip_image = image[ly1-2*m:ly2+3*m, lx1-m:lx2+m ]
						width = 64
						height = 32
						dim = (width, height)
						resized = cv2.resize(lip_image, dim, interpolation = cv2.INTER_AREA)
						cv2.imwrite(os.path.join(video_frame_path, "frame_{}_{}.jpg".format(video_number, count)), resized)
						count += 1
                except Exception as e:
                    print(str(e))
            else:
                print("no face in frame")

