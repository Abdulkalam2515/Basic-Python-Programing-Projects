import cv2

# Initialize the video capture (0 for default camera)
cap = cv2.VideoCapture(0)

# Initialize variables
previous_frame = None
motion_detected = False

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if previous_frame is None:
        previous_frame = gray_frame
        continue

    # Compute the absolute difference between the current and previous frame
    frame_delta = cv2.absdiff(previous_frame, gray_frame)

    # Apply a threshold to the frame delta to create a binary image
    threshold = 30  # You can adjust this threshold value
    _, thresh_frame = cv2.threshold(frame_delta, threshold, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the contours to detect motion
    for contour in contours:
        if cv2.contourArea(contour) > 100:  # You can adjust this area threshold
            motion_detected = True
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with motion detection
    cv2.imshow("Video Motion Sensor", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()