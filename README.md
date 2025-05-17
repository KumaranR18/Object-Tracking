# **Object Tracking Based on Color**

A real-time computer vision project that detects and tracks objects based on their color using OpenCV and Python.

---

**🚀 Project Overview**  
This project uses color-based segmentation in the HSV color space to detect and track objects in real time through a webcam feed. It isolates objects of a specific color, finds their contours, and marks their position and size visually. The program also prints directional commands (Right, Left, Front, Stop) based on the object's position and size.

---

**🛠️ Features**  
- **Real-time video capture using a webcam**  
- **Color detection in HSV color space for better robustness**  
- **Noise reduction with Gaussian blur, erosion, and dilation**  
- **Contour detection for accurate object localization**  
- **Visual tracking by drawing circles around detected objects**  
- **Command outputs based on object position and size**  

---

**📋 Prerequisites**  

Make sure you have the following installed:  
- **Python 3.10+**  
- **OpenCV (`opencv-python`)**  
- **imutils**  

You can install the required Python libraries using:

```bash
pip install opencv-python imutils
```
---

**⚙️ How to Run**  

**Clone this repository:**

```bash
git clone https://github.com/KumaranR18/Object-Tracking.git
```
**Navigate into the project directory:**

```bash
cd Object-Tracking
```
**Run the script:**

```bash
python Object Tracking based on Color.py
```
A window will open showing the webcam feed with detected objects highlighted.
Press q to quit the program.

---

**🎯 How It Works**
- **The program captures frames from the webcam.**
- **Converts each frame to HSV color space for effective color segmentation.**
- **Creates a mask to isolate pixels within the specified color range.**
- **Cleans up the mask by applying erosion and dilation to remove noise.**
- **Detects contours and finds the largest one corresponding to the object.**
- **Calculates the centroid and radius of the object.**
- **Draws circles on the frame for visualization.**
- **Prints positional commands based on the object's location relative to the frame.**

---

**🔧 Customization**
- Adjust the HSV color range (redLower and redUpper) to track different colors.
- Modify the positional thresholds to fine-tune the commands (Right, Left, Front, Stop).

---

**🤝 Contributions**

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

---

**📄 License**

This project is licensed under the MIT License - see the LICENSE file for details.

