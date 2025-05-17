import imutils             # Utility functions for image processing (e.g., resizing)
import cv2                # OpenCV library for computer vision tasks

# HSV color range for detecting blue objects
redLower = (95, 49, 100)
redUpper = (154, 255, 255)

camera = cv2.VideoCapture(0)  # Start video capture from webcam

while True:
    grabbed, frame = camera.read()  # Capture frame from webcam
    frame = imutils.resize(frame, width=1000)  # Resize frame for consistency
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)  # Blur to reduce noise
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)  # Convert to HSV color space

    # Create a mask for blue color and clean it with erosion and dilation
    mask = cv2.inRange(hsv, redLower, redUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours in the mask
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)  # Largest contour
        ((x, y), radius) = cv2.minEnclosingCircle(c)  # Minimum enclosing circle
        M = cv2.moments(c)  # Moments for centroid calculation
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:  # Filter small noise by radius size
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)  # Draw circle
            cv2.circle(frame, center, 5, (0, 0, 255), -1)  # Draw centroid

            # Determine object position and print commands
            if radius > 250:
                print("stop")  # Object too close
            else:
                if center[0] < 150:
                    print("Right")  # Object on left side
                elif center[0] > 450:
                    print("Left")  # Object on right side
                else:
                    print("Front")  # Object in center

    cv2.imshow("Frame", frame)  # Show the output frame

    if cv2.waitKey(1) == ord("q"):  # Exit on 'q' key
        break

camera.release()
cv2.destroyAllWindows()
