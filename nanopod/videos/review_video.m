function review_video(videoFile)

% Read the video file
video= VideoReader(videoFile);
fname=strsplit(videoFile,'\');

% Loop through each frame of the video
figure('Units','normalized','Position',[0 0 1 0.9])
title(fname(end),'Interpreter', 'none')
hold on
while hasFrame(video)
    % Read the current frame
    frame = readFrame(video);
    
    % Display the frame
    imshow(frame, 'InitialMagnification', 'fit')    

    % Pause for a specified duration (e.g., 0.5 seconds)
    pause(0.2);
end

end