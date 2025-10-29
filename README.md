![Project Banner](banner.png)

# 🧠 AI-Based Lost Item Finder in Public Places using CCTV Feeds

## 📘 Overview
This project is an AI-powered surveillance solution designed to **detect unattended or lost items in public areas** using CCTV video feeds.  
It uses a **YOLOv8 object detection model** integrated with a **Flask web app** to process live video streams in real-time.

The system can help **authorities identify forgotten bags, purses, or other objects** to improve safety and reduce theft or panic situations in crowded public spaces like malls, airports, and railway stations.

---

## 🎯 Problem Statement
In urban environments, unattended items can pose security risks or cause inconvenience.  
Traditional manual monitoring of CCTV feeds is inefficient and prone to human error.  
This project provides an **automated, real-time detection system** that alerts security personnel when a potentially lost or unattended object is detected.

---

## 🧩 Key Features
- Real-time object detection using **YOLOv8**
- Flask web interface for live camera feed
- Bounding boxes drawn for detected items
- Alerts triggered when an object remains unattended beyond a time threshold
- Modular design for integration with existing CCTV systems

---

## 🧠 Tech Stack
- **Python 3.10+**
- **YOLOv8 (Ultralytics)**
- **OpenCV**
- **Flask**
- **NumPy, Pandas**
- **Matplotlib** (for optional visualization)

---

## ⚙️ Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/sonikadvlr/AI_Lost_Item_Finder.git
   cd AI_Lost_Item_Finder
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000` in your browser to view the live feed.

---

## 🧩 Workflow
1. **Video Input** → CCTV footage or webcam feed  
2. **YOLOv8 Model** → Detects objects (bags, boxes, personal items)  
3. **Tracking Module** → Monitors item movement  
4. **Alert System** → If item remains stationary beyond threshold, triggers alert  

---

## 🧪 Example Output
Below is a sample frame where the model detects an unattended bag:

![Detection Screenshot](outputs/detection_example.png)

---

## 🚀 Future Scope
- Integrate with cloud databases to log incidents.
- Add facial detection to identify owners returning for items.
- Deploy to edge devices (like Jetson Nano) for real-time surveillance in the field.

---

## 📜 Author
**Sonika Duvvuru**  
B.E. Computer Science Engineering  
Passionate about Data Science, AI, and building solutions for public safety.  
📧 sonikaduvvuru@gmail.com

---


