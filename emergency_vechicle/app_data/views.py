# from django.shortcuts import render, redirect
# from ultralytics import YOLO
# import cv2
# import math
# from django.http import StreamingHttpResponse
# import tempfile
# import os


# model = YOLO("app_data/model/best.pt")
# videos = []

# def start_live(request, path, road):
#     cap = cv2.VideoCapture(path)
#     cap.set(3, 640)
#     cap.set(4, 480)  

#     classNames = ['Emergency Vehicles','Emergency Vehicles']
#     c = 0


#     while True:
#         success, img = cap.read()
#         results = model(img, stream=True)

#         # coordinates
#         for r in results:
#             boxes = r.boxes

#             for box in boxes:
#                 x1, y1, x2, y2 = box.xyxy[0]
#                 x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
#                 confidence = math.ceil((box.conf[0]*100))/100
#                 print("Confidence --->",confidence)
#                 if confidence > 0.30:
#                     cls = int(box.cls[0])
#                     # print("class : ",cls)
#                     name=classNames[cls]
#                     print("Class name -->", name)
#                     c +=1
#                     print(c)    
#                     org = [x1, y1]
#                     font = cv2.FONT_HERSHEY_SIMPLEX
#                     fontScale = 1
#                     color = (0, 0, 255)
#                     thickness = 2
#                     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                     cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
                    
#                         # return render(request, 'home.html', {'data': 'road1'})
#         cv2.imshow('Webcam', img)
#         # _, buffer = cv2.imencode('.jpg', img)
#         # frame = buffer.tobytes()

#         # Yield the frame as bytes for the StreamingHttpResponse
#         # yield (b'--frame\r\n'
#         #         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#         if c == 5:
#             cap.release()
#             cv2.destroyAllWindows()
#             break
#         if cv2.waitKey(1) == ord('q'):
#             break

#     # cap.release()
#     # cv2.destroyAllWindows()
#     print('########outtheloop')
#     return c  

# def home(request):
#     if not videos:
#         return render(request, 'home.html')
#     return render(request, 'home.html',{'data': 'road'.format(videos[0])})



# def detect_page1(request):
#     if request.method == 'POST' and request.FILES.get('vid'):
#         vid_file = request.FILES['vid']
#         # Save the uploaded video temporarily
#         with tempfile.NamedTemporaryFile(delete=False) as temp_vid:
#             for chunk in vid_file.chunks():
#                 temp_vid.write(chunk)
#             temp_vid.close()
#             videos.append(1)
#             print(temp_vid)
#             det = start_live(request, temp_vid.name, 1)
#             if det >= 0:
#                 return render(request, 'home.html', {'data': 'road1'})
#     return render(request, 'home.html')

# def detect_page2(request):
#     if request.method == 'POST' and request.FILES.get('vid'):
#         vid_file = request.FILES['vid']
#         # Save the uploaded video temporarily
#         with tempfile.NamedTemporaryFile(delete=False) as temp_vid:
#             for chunk in vid_file.chunks():
#                 temp_vid.write(chunk)
#             temp_vid.close()
#             videos.append(2)
#             print(temp_vid)
#             det = start_live(request, temp_vid.name, 2)
#             if det >= 0:
#                 return render(request, 'home.html', {'data': 'road2'})
#     return render(request, 'home.html')

# def detect_page3(request):
#     if request.method == 'POST' and request.FILES.get('vid'):
#         vid_file = request.FILES['vid']
#         # Save the uploaded video temporarily
#         with tempfile.NamedTemporaryFile(delete=False) as temp_vid:
#             for chunk in vid_file.chunks():
#                 temp_vid.write(chunk)
#             temp_vid.close()
#             videos.append(3)
#             print(temp_vid)
#             det = start_live(request, temp_vid.name, 3)
#             if det >= 0:
#                 return render(request, 'home.html', {'data': 'road3'})
#     return render(request, 'home.html')

# def detect_page4(request):
#     if request.method == 'POST' and request.FILES.get('vid'):
#         vid_file = request.FILES['vid']
#         # Save the uploaded video temporarily
#         with tempfile.NamedTemporaryFile(delete=False) as temp_vid:
#             for chunk in vid_file.chunks():
#                 temp_vid.write(chunk)
#             temp_vid.close()
#             videos.append(4)
#             print(temp_vid)
#             det = start_live(request, temp_vid.name, 4)
#             if det >= 0:
#                 return render(request, 'home.html', {'data': 'road4'})
#     return render(request, 'home.html')

# # def detection(request):
# #     return StreamingHttpResponse(start_live(request, videos[0], videos[1]), content_type="multipart/x-mixed-replace;boundary=frame")


from django.shortcuts import render
from ultralytics import YOLO
import cv2
import math
import tempfile
import os
import numpy as np
from django.core.files.uploadedfile import InMemoryUploadedFile

# Load the YOLO model
model = YOLO("app_data/model/best.pt")
videos = []

def process_image(image_path):
    """Process an image for YOLO detection."""
    img = cv2.imread(image_path)

    # Ensure the image is properly loaded
    if img is None:
        print("Error: Could not read image")
        return None

    classNames = ['Emergency Vehicles', 'Emergency Vehicles']
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            confidence = math.ceil((box.conf[0] * 100)) / 100

            if confidence > 0.30:
                cls = int(box.cls[0])
                name = classNames[cls]
                print(f"Detected: {name} with Confidence: {confidence}")

                # Draw bounding box and label on image
                org = (x1, y1)
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, name, org, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    output_path = image_path.replace(".jpg", "_detected.jpg")
    cv2.imwrite(output_path, img)  # Save the processed image
    return output_path

def start_live(request, path, is_image=False):
    """Process video or image based on the input type."""
    if is_image:
        return process_image(path)  # Process the image and return result

    cap = cv2.VideoCapture(path)
    cap.set(3, 640)
    cap.set(4, 480)  
    classNames = ['Emergency Vehicles', 'Emergency Vehicles']
    c = 0

    while True:
        success, img = cap.read()
        if not success:
            break

        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                confidence = math.ceil((box.conf[0]*100))/100

                if confidence > 0.30:
                    cls = int(box.cls[0])
                    name = classNames[cls]
                    c += 1
                    org = (x1, y1)
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(img, name, org, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Webcam', img)
        if c == 5:
            break
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return c  

def detect_media(request):
    """Handle both image and video uploads."""
    if request.method == 'POST' and request.FILES.get('media'):
        media_file = request.FILES['media']

        # Determine if it's an image or video
        file_ext = os.path.splitext(media_file.name)[1].lower()
        is_image = file_ext in ['.jpg', '.jpeg', '.png']

        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as temp_media:
            for chunk in media_file.chunks():
                temp_media.write(chunk)
            temp_media.close()

            if is_image:
                detected_image = start_live(request, temp_media.name, is_image=True)
                return render(request, 'home.html', {'data': 'image_detected', 'image_path': detected_image})
            else:
                videos.append(1)
                det = start_live(request, temp_media.name)
                if det >= 0:
                    return render(request, 'home.html', {'data': 'road1'})

    return render(request, 'home.html')
