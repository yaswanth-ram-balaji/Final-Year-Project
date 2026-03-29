# 🔍 Defect Classification in Solar Panels Using ElectroLuminescence Imaging Using YOLOv9

## 📌 Project Overview

This project presents an **AI-based system** for detecting defects in solar panels using **Electroluminescence (EL) images** and the **YOLOv9 deep learning model**.

The system allows users to upload solar panel EL images through a web interface and predicts whether the panel is **Defective** or **Normal**.

The model provides:

* 🏷️ Prediction label (**Defective / Normal**)
* 📊 Confidence score
* 🧭 Bounding box covering the solar panel region

The project integrates a **YOLOv9 deep learning model** with a **Django web application** to provide real-time predictions.

---

## ❗ Problem Statement

Solar panels can develop internal defects such as:

* Microcracks
* Broken finger lines
* Dark regions
* Inactive cells

These defects reduce power generation efficiency.

Manual inspection is:

* time consuming
* expensive
* not scalable for large solar farms

This project automates the defect detection process using **Artificial Intelligence**.

---

## 💡 Solution

We used the **YOLOv9 deep learning model** trained on **Electroluminescence (EL) solar panel images**.

The system performs **panel-level defect detection** and classifies whether a solar panel is **defective** or **normal**.

Users can upload images using a **Django web interface** and get instant prediction results.

---

## 🛠️ Tech Stack

### Programming Language:

* 🐍 Python

### Deep Learning:

* 🤖 YOLOv9
* 🔥 PyTorch
* 📦 Ultralytics

### Web Framework:

* 🌐 Django

### Libraries:

* 👁️ OpenCV
* 🔢 NumPy
* 🖼️ Pillow

### Frontend:

* 🎨 HTML
* 🎨 CSS

---

## 🔄 Project Workflow

1️⃣ User uploads EL image through web interface
2️⃣ Django backend receives the image
3️⃣ Image preprocessing is applied
4️⃣ YOLOv9 model performs prediction
5️⃣ Model classifies panel as Defective or Normal
6️⃣ Confidence score is generated
7️⃣ Result is displayed on webpage

---

## 🧠 Model Information

**Model Used:** YOLOv9

The model performs **panel-level defect detection**.

Instead of detecting individual defect types separately, the model predicts whether the entire solar panel image is **defective** or **normal**.

### Output includes:

* 📦 Bounding box covering panel
* 🏷️ Prediction label
* 📊 Confidence score

---

## 📁 Project Structure

```
Final-Year-Project
│
├── Backend
│   ├── yolov8.pt
│   ├── yolov9.pt
│
├── Frontend
│   └── Solar
│       ├── app
│       ├── templates
│       ├── media
│       ├── best.pt
│       ├── manage.py
│       ├── db.sqlite3
│
├── Solar Panel images
```

---

## ⚙️ Installation

### Step 1: Clone repository

```
git clone https://github.com/yaswanth-ram-balaji/Final-Year-Project.git
```

### Step 2: Navigate to project folder

```
cd Frontend/Solar
```

### Step 3: Create environment

```
conda create -n venv python=3.10
conda activate venv
```

### Step 4: Install dependencies

```
pip install -r requirements.txt
```

### Step 5: Run project

```
python manage.py runserver
```

### Step 6: Open browser

```
http://127.0.0.1:8000/
```

Upload EL image and check prediction.

---

## ⭐ Features

* AI-based defect detection
* Django web application
* Real-time prediction
* Confidence score output
* Easy to use
* Scalable architecture

---

## 📤 Output

**Input:** Solar panel EL image

**Output:**

* Prediction: Defective or Normal
* Confidence score
* Bounding box covering panel region

---

## ⚠️ Limitations

* Detects defects at panel level
* Does not localize individual defect types
* Accuracy depends on dataset quality

---

## 🚀 Future Scope

* Detect individual defect types
* Improve localization accuracy
* Deploy using cloud platform
* Drone-based inspection
* Edge device deployment

---

## 👨‍🎓 Author

Final Year B.Tech Project

Artificial Intelligence and Machine Learning

Project Title: **Defect Classification in Solar Panels Using ElectroLuminescence Imaging Using YOLOv9**

---

## 📜 License

This project is developed for academic purposes.

