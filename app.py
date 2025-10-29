from flask import Flask, render_template, Response
import cv2
from detect_items import detect_objects

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # webcam, change to 'sample_video.mp4' for file

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame, _ = detect_objects(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return "<h2>AI Lost Item Finder Running...</h2><img src='/video'>"

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
