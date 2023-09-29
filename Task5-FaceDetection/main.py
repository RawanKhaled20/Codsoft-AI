""" Author: Rawan Khaled   https://github.com/RawanKhaled20/Codsoft-AI.git"""

import cv2

def detectface_frame(image, frontalface, scalefactor, min_neb, color, text):
    grayscaled_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_Detect = frontalface.detectMultiScale(grayscaled_image, scaleFactor=scalefactor, minNeighbors=min_neb)
    coord = []

    for x, y, w, h in face_Detect:
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 3)
        cv2.putText(image, text, (x, y - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coord = [x, y, w, h]

    return coord, image

def detectface(image, facecascade):
    color = {"blue": (255, 0, 0), "red": (0, 0, 255), "green": (0, 255, 0)}
    coord, image = detectface_frame(image, facecascade, 1.1, 10, color["blue"], "This is Live Face Detection")
    return image


# Start the video capture
capture_on_video = cv2.VideoCapture(0)
# Get frontalface haar cascade
facecascade = cv2.CascadeClassifier("raw.githubusercontent.com_opencv_opencv_master_data_haarcascades_haarcascade_frontalface_default.xml")

while True:
    _, frame_Detect_img = capture_on_video.read()
    image = detectface(frame_Detect_img, facecascade)
    cv2.imshow("Video for face detection is on", image)
    # If the user presses q on the keyboard to quit the video, terminate
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture_on_video.release()
cv2.destroyAllWindows()