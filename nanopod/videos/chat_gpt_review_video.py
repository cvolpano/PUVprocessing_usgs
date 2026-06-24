import cv2
import os
import matplotlib.pyplot as plt

def review_video(video_file):
    # Open the video file
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Extract filename
    fname = os.path.basename(video_file)

    # Setup matplotlib figure
    plt.ion()  # Enable interactive mode
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.canvas.manager.set_window_title(fname)
    plt.title(fname)

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # End of video

        # Convert color from BGR (OpenCV) to RGB (matplotlib)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display frame
        ax.clear()
        ax.imshow(frame_rgb)
        ax.axis('off')
        plt.pause(0.2)  # Pause for 0.2 seconds

    cap.release()
    plt.ioff()
    plt.close()

# Example usage:
# review_video('path_to_video.mp4')