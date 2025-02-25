import cv2
import os

# Paths to file and output folder
video_path = "C:/Users/rozhk/VVID/VideoExtractor/robotCam_tst.avi"
output_folder = "C:/Users/rozhk/VVID/VideoExtractor/RESULTS/"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Failed to open video!")
    exit()
else:
    print("Video opened successfully!")

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if no more frames
    
    # Generate filename and save frame
    if count%700 == 0:
        frame_filename = os.path.join(output_folder, f"frame_{count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
    
    count += 1
    print(count)

# Release resources
cap.release()
print(f"Done! Extracted {count} frames to folder {output_folder}")