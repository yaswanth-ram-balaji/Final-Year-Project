from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.core.files.storage import default_storage
from django.conf import settings
import os
from ultralytics import YOLO
import cv2

# -----------------------------
# Load ONLY YOLOv8 model
# -----------------------------
model = YOLO('Yolo_v8.pt')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')

        if password == confirm_password:
            if Register.objects.filter(email=email).exists():
                messages.error(request, "Your Email ID already exists")
                return render(request, 'register.html')
            else:
                Register.objects.create(
                    name=name, email=email, password=password, address=address
                )
                messages.success(request, "Registration successful")
                return render(request, 'login.html')
        else:
            messages.error(request, "Passwords do not match")
            return render(request, 'register.html')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Register.objects.filter(email=email).first()

        if user:
            if user.password == password:
                return render(request, 'home.html')
            else:
                messages.error(request, "Incorrect password")
                return render(request, 'login.html')
        else:
            messages.error(request, "User does not exist")
            return render(request, 'login.html')

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


# -----------------------------
# Function to classify image using YOLOv8
# -----------------------------
def classify_image(image_path):
    # Run YOLOv8 inference
    results = model(image_path)

    # Extract detections
    boxes = results[0].boxes

    # Annotated image
    annotated_image = results[0].plot()

    # Save annotated image
    base, ext = os.path.splitext(image_path)
    annotated_path = f"{base}_annotated{ext}"
    cv2.imwrite(annotated_path, annotated_image)

    detections = []

    if boxes and len(boxes) > 0:
        class_ids = boxes.cls.cpu().numpy().astype(int)
        confidences = boxes.conf.cpu().numpy()
        xyxy = boxes.xyxy.cpu().numpy()

        for cid, conf, bb in zip(class_ids, confidences, xyxy):
            detections.append({
                "class_name": model.names[cid],
                "confidence": round(float(conf), 3),
                "bbox": bb.tolist()
            })

        max_idx = confidences.argmax()
        highest_class = model.names[class_ids[max_idx]]
    else:
        highest_class = "normal"

    return highest_class, detections, annotated_path


# -----------------------------
# File Upload + YOLOv8 Prediction
# -----------------------------
def upload(request):
    context = {}

    if request.method == 'POST':
        uploaded_file = request.FILES.get('uploaded_file')

        if not uploaded_file:
            context['error'] = "Please upload a file."
        else:
            # Save file
            file_path = default_storage.save(f'uploads/{uploaded_file.name}', uploaded_file)
            full_path = os.path.join(settings.MEDIA_ROOT, file_path)

            # Run YOLOv8 detection
            classification, detections, annotated_path = classify_image(full_path)

            annotated_url = str(annotated_path).replace(str(settings.MEDIA_ROOT), settings.MEDIA_URL)

            context.update({
                "classification": classification,
                "detections": detections,
                "image_url": f"{settings.MEDIA_URL}{file_path}",
                "annotated_image": annotated_url
            })

    return render(request, 'upload.html', context)
