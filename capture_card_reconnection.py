import cv2
import time

def reconnect_capture():
    # Attempt to reconnect to the capture card
    print("Attempting to reconnect to capture card...")
    time.sleep(1)  # Add a short delay before attempting to reconnect
    
    # Iterate through possible device indices and attempt to create a capture object
    for index in range(10):  # Assuming a maximum of 10 devices
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            print("Successfully connected to device at index:", index)
            return cap
    
    # If no device is found, return None
    return None

def capture_frames():
    cap = reconnect_capture()  # Initialize capture object
    
    while True:
        try:
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            # Check if frame is captured successfully
            if not ret:
                raise Exception("No frame found")
            
            # Resize frame
            frame_resized = cv2.resize(frame, (480, 360))
            
            # Display the resized frame
            cv2.imshow('Resized Frame', frame_resized)
            
            # Check for key press to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        except Exception as e:
            print("Error:", e)
            # Attempt to reconnect to the capture card
            cap.release()
            cap = reconnect_capture()
            if cap is None:
                print("Failed to reconnect. Exiting...")
                break
        
    # Release the capture object and close windows
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()

# Call the function to start capturing frames
capture_frames()

