# from flask import Flask, render_template, request, Response, jsonify
# from ultralytics import YOLO
# import cv2
# import math
# import tempfile
# import os

# app = Flask(__name__)
# model = YOLO("model/best.pt")
# videos = []

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/detect_page1', methods=['POST'])
# def detect_page1():
#     global videos
#     if request.method == 'POST' and 'vid' in request.files:
#         vid_file = request.files['vid']
#         # Save the uploaded video temporarily
#         with tempfile.NamedTemporaryFile(delete=False) as temp_vid:
#             for chunk in vid_file.stream:
#                 temp_vid.write(chunk)
#             temp_vid.close()
#             print(temp_vid.name)
#             videos.append(temp_vid.name)
#             videos.append(1)
#     return render_template('home.html', data='data1')

# @app.route('/detect_page2', methods=['POST'])
# def detect_page2():
#     global videos
#     if request.method == 'POST' and 'vid' in request.files:
#         vid_file = request.files['vid']
#         # Save the uploaded video temporarily
#         with tempfile.NamedTemporaryFile(delete=False) as temp_vid:
#             for chunk in vid_file.stream:
#                 temp_vid.write(chunk)
#             temp_vid.close()
#             print(temp_vid.name)
#             videos.append(temp_vid.name)
#             videos.append(2)
#     return render_template('home.html', data='data2')

# @app.route('/detect_page3', methods=['POST'])
# def detect_page3():
#     global videos
#     if request.method == 'POST' and 'vid' in request.files:
#         vid_file = request.files['vid']
#         # Save the uploaded video temporarily
#         with tempfile.NamedTemporaryFile(delete=False) as temp_vid:
#             for chunk in vid_file.stream:
#                 temp_vid.write(chunk)
#             temp_vid.close()
#             print(temp_vid.name)
#             videos.append(temp_vid.name)
#             videos.append(3)
#     return render_template('home.html', data='data3')

# @app.route('/detect_page4', methods=['POST'])
# def detect_page4():
#     global videos
#     if request.method == 'POST' and 'vid' in request.files:
#         vid_file = request.files['vid']
#         # Save the uploaded video temporarily
#         with tempfile.NamedTemporaryFile(delete=False) as temp_vid:
#             for chunk in vid_file.stream:
#                 temp_vid.write(chunk)
#             temp_vid.close()
#             print(temp_vid.name)
#             videos.append(temp_vid.name)
#             videos.append(4)
#     return render_template('home.html', data='data4')

# @app.route('/detection')
# def detection():
#     global videos
#     return Response(start_live(videos[0], videos[1]), mimetype='multipart/x-mixed-replace; boundary=frame')

# def start_live(path, road):
#     cap = cv2.VideoCapture(path)
#     cap.set(3, 640)
#     cap.set(4, 480)
#     try:
#         videos.clear()
#         print('#################', videos)
#     except:
#         pass    

#     classNames = ['Ambulance','FireTruck']
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
#                     name=classNames[cls]
#                     print("Class name -->", name)
#                     c +=1
#                     print(c)    
#                     org = (x1, y1)
#                     font = cv2.FONT_HERSHEY_SIMPLEX
#                     fontScale = 1
#                     color = (0, 0, 255)
#                     thickness = 2
#                     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                     cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
#                     if c == 10:
#                         change(road)
#         _, buffer = cv2.imencode('.jpg', img)
#         frame = buffer.tobytes()

#         yield (b'--frame\r\n'
#                 b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#         if cv2.waitKey(1) == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     return render_template('home.html')

# def change(road):
#     if road == 1:
#         return render_template('home.html', data1='road1')
#     elif road == 2:
#         return render_template('home.html', data1='road2')
#     elif road == 3:
#         return render_template('home.html', data1='road3')
#     elif road == 4:
#         return render_template('home.html', data1='road4')

# if __name__ == '__main__':
#     app.run(debug=True)
