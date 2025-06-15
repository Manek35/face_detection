# 👁️‍🗨️ Face Detection using OpenCV

This simple yet powerful Python script demonstrates how to perform **face detection** on an image using **OpenCV** and Haar Cascade Classifier. Ideal for beginners in computer vision, this project shows how machine learning-based classifiers can detect faces in static images.

---

## 🔍 Overview

This project uses a **Haar cascade classifier** to identify faces in an image (`faces.png`). The script processes the image, converts it to grayscale, detects faces, and then draws bounding boxes around each detected face.

---

## 🧠 How It Works

1. **Load Haar Cascade**: Uses a pre-trained Haar cascade XML file for face detection.
2. **Read Image**: Loads the target image using OpenCV.
3. **Grayscale Conversion**: Converts the image to grayscale to optimize detection.
4. **Detect Faces**: Applies the `detectMultiScale()` method to find faces.
5. **Draw Bounding Boxes**: Marks detected faces with green rectangles.
6. **Display Output**: Shows the result in a window.

---

## 🖼️ Demo

<img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Faces_detected_in_picture.png" width="400" alt="Face Detection Example" />

---

## 🛠 Requirements

- Python 3.x
- OpenCV (`opencv-python`)

Install with pip:

```bash
pip install opencv-python
```

---

## 📁 Files

- `face_detection.py`: The main script.
- `faces.png`: The input image (replace with your own).
- `face detection.xml`: Haar cascade file (commonly available as `haarcascade_frontalface_default.xml`).

---

## ▶️ Run the Script

```bash
python face_detection.py
```

---

## 📌 Notes

- Make sure the XML file (`face detection.xml`) is in the same directory or provide the correct path.
- You can download pre-trained Haar cascades from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

---

## 🌟 Features

- Simple and beginner-friendly
- Real-time or image-based detection (can be easily extended to webcam input)
- Based on classical computer vision, no training required

---

## 🚀 Future Enhancements

- Add webcam face detection
- Integrate with dlib or deep learning-based detectors (e.g., MTCNN)
- Extend to detect eyes, smiles, or full bodies

---


## 📄 License

This project is open-source under the [MIT License](LICENSE).
