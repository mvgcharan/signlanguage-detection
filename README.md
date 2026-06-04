# signlanguage-detection dataset
# Dataset Recommendation: ASL Alphabet (Kaggle)

For a beginner-level research project focusing on sign language detection, the **ASL Alphabet** dataset is the industry standard.

### 🔗 Link
[Kaggle: ASL Alphabet Dataset](https://www.kaggle.com/datasets/grassknoted/asl-alphabet)

### Recommended Folder Structure
```text
dataset/
├── train/
│   ├── A/ (3000 images)
│   ├── B/ (3000 images)
│   ├── ...
│   └── space/
├── test/
│   ├── A_test.jpg
│   ├── B_test.jpg
│   └── ...
└── models/
    └── asl_classifier_v1.h5
```

###  Preprocessing Steps (Python/OpenCV)

1. **Gray Scaling & Normalization**:
   ```python
   img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   img = img / 255.0  # Normalize to [0,1]
   ```

2. **Region of Interest (ROI)**:
   Instead of the whole frame, crop the square where the hand is detected.
   
3. **Resizing**:
   Standardize all input images to **64x64** or **224x224** (if using MobileNet).

4. **Landmark Extraction (Recommended for CPU)**:
   Instead of raw pixels, pass the image through MediaPipe Hands first to get 21 landmarks (x,y,z). This reduces the input from 50,000+ pixels to just 63 coordinates, making the model incredibly fast on CPUs.

### Why this approach?
By using **Landmarks + Small Neural Network**, you achieve >90% accuracy with sub-10ms latency on a standard laptop CPU. This is the "Secret Sauce" for a high-distinction research project.
