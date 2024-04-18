# Sign-Language-Based-Messenger

Sure, here's a brief description of the code for sign language detection:

**Sign Language Detection using MediaPipe and OpenCV**

This Python code provides a real-time sign language detection system using the MediaPipe library for hand landmark detection and OpenCV for image processing. The system allows users to interact with their computer through sign language gestures captured by a webcam.

**Key Features:**

1. **Gesture Recognition:** The code utilizes the MediaPipe library to detect hand landmarks in real-time webcam feed.

2. **Model Loading:** It loads a pre-trained machine learning model for gesture classification. The model is trained to recognize specific hand gestures corresponding to sign language symbols.

3. **Real-time Feedback:** As the user performs sign language gestures in front of the webcam, the system detects and displays the recognized gestures in real-time on the screen.

4. **User Interaction:** Users can trigger gesture recognition by pressing a designated key ('a' in this case). Once triggered, the system captures the current frame from the webcam, performs gesture recognition, and displays the recognized gesture along with the bounding box and label.

5. **Message Sending:** Additionally, users can send messages containing the recognized gestures via Telegram using the `sendtoTelegram()` function.

**Dependencies:**

- `tkinter`: Python's standard GUI library used for creating the user interface.
- `cv2` (OpenCV): An open-source computer vision and machine learning software library used for image processing and computer vision tasks.
- `PIL` (Python Imaging Library): A library for opening, manipulating, and saving many different image file formats.
- `numpy`: A fundamental package for scientific computing with Python, used for array manipulation.
- `mediapipe`: A library for building real-time multi-modal machine learning pipelines.
- `pickle`: Python's built-in module for serializing and deserializing Python objects.
- `send_msg`: Custom module for sending messages to Telegram.

**Usage:**

1. Run the Python script.
2. Perform sign language gestures in front of the webcam.
3. Press the 'a' key to trigger gesture recognition.
4. The recognized gesture will be displayed on the screen along with its label.
5. Optionally, press the 'Send Message' button to send the recognized gesture as a message via Telegram.

**Note:** Ensure that all dependencies are installed and the `model.p` file containing the pre-trained model is available in the same directory as the script. Additionally, users may need to configure the Telegram API integration for message sending functionality.


**Results:**

https://github.com/HuligeshBondade/Sign-Language-Based-Messenger/assets/107861136/f8f3e277-f28e-4487-8de5-4c8129e9907f


