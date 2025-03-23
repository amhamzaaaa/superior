from detection.detector import detect_animals
from alert.alert_map import create_alert_map
from alert.location import get_current_location

import cv2
import webbrowser

video_path = 'data/sample_video.mp4'
model_path = 'models/yolov8n.pt'
herd_threshold = 5

cap = cv2.VideoCapture(video_path)
alert_triggered = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    animal_count, annotated_frame = detect_animals(frame, model_path)

    cv2.imshow("Animal Detection", annotated_frame)

    if animal_count >= herd_threshold and not alert_triggered:
        print(f"[ALERT] Herd detected! {animal_count} animals.")
        lat, lon = get_current_location()

        create_alert_map(lat, lon, animal_count)
        webbrowser.open("map_output/map.html")
        alert_triggered = True

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
