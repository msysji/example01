import cv2

image = "pos/test_image2.png"

face_cascade = cv2.CascadeClassifier('cascade/trained_data/cascade.xml')

loaded_img = cv2.imread(f"{image}")

gray = cv2.cvtColor(loaded_img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, minNeighbors=5, minSize=(30, 30))

if len(faces) == 0:
    print('Not recognized image')
    cv2.imshow('img', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    for (x, y, w, h) in faces:
        penned_img = cv2.rectangle(loaded_img, (x,y), (x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = penned_img[y:y+h, x:x+w]

    scaled_img = cv2.resize(penned_img, dsize=None, fx=0.5, fy=0.5)
    cv2.imshow('img', scaled_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
