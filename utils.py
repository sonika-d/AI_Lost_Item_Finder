import time

class ObjectTracker:
    def __init__(self, timeout=15):
        self.detected_objects = {}
        self.timeout = timeout

    def update(self, detections):
        current_time = time.time()
        for obj in detections:
            label = obj["label"]
            if label not in self.detected_objects:
                self.detected_objects[label] = current_time
            elif current_time - self.detected_objects[label] > self.timeout:
                print(f"[ALERT] {label} unattended for {self.timeout} seconds!")
