# Abstract

The "Real-Time Sign Language Detection System with Text and Speech Output" aims to bridge the communication gap between the hearing-impaired community and the general public. By utilizing advancements in computer vision and deep learning, this project develops a system capable of interpreting American Sign Language (ASL) gestures in real-time. 

The system leverages MediaPipe for hand landmark extraction and a classification algorithm (CNN or Landmark-based analysis) to identify gestures. Recognized gestures are converted into text displayed on a graphical user interface and simultaneously synthesized into audible speech using Text-to-Speech (TTS) technology. 

Achieving over 80% accuracy, this prototype demonstrates a cost-effective, CPU-based solution suitable for deployment on standard hardware, promoting inclusivity and accessibility in daily communication.

# Problem Statement

Individuals who rely on sign language often face significant barriers when interacting with those who do not understand it. Human interpreters are not always available or affordable. While text-based translation apps exist, they often require manual input, which is slow and less natural than sign-based communication. 

There is a critical need for an automated, real-time tool that can "speak" on behalf of sign language users, enabling seamless two-way interactions without requiring the other party to learn signing.

# Methodology

1. **Data Acquisition**: Utilization of the ASL Alphabet dataset containing images of hand gestures.
2. **Preprocessing**: Frames from the webcam are resized and normalized. Hand landmarks are extracted using Google's MediaPipe framework to minimize noise from backgrounds.
3. **Model Selection**: 
   - **Approach A (Web)**: Distance-based landmark classification for ultra-low latency.
   - **Approach B (Local/Python)**: A convolutional neural network (CNN) trained on cropped hand images for higher spatial feature extraction.
4. **Integration**: Prediction results are piped to a text overlay and the Web Speech API.
5. **Evaluation**: Testing against a validation set to ensure >80% precision across common signs.

# Supported Lexicon

The current prototype supports 8 fundamental gestures for real-time translation:
- **Hello**: Open palm, all fingers extended.
- **Yes**: Agreement or fist shape (all fingers folded).
- **Victory**: Peace or victory sign (index and middle fingers up).
- **I Love You**: Standard ASL sign for affection (thumb, index, pinky).
- **Point**: Directional gesture (index finger only up).
- **OK**: Confirmation gesture (thumb and index forming a circle).
- **Thumb Up**: Positive affirmation (thumb pointing up).
- **Call Me**: Communication request (thumb and pinky extended).

# Features
- **Real-Time Vision**: 30FPS hand landmark tracking via MediaPipe.
- **Dynamic Speech**: Synchronized Web Speech API output.
- **Engine Control**: Ability to pause/resume detection and mute/unmute audio.
- **Lexicon Guide**: In-app dictionary with how-to descriptions.

# Tools & Technologies

- **Frontend**: React.js, Tailwind CSS, Framer Motion.
- **Computer Vision**: MediaPipe Hands, OpenCV (for Python version).
- **Audio**: Web Speech API (TTS), gTTS/pyttsx3 (for Python version).
- **Libraries**: Lucide React for UI, React-Webcam.
