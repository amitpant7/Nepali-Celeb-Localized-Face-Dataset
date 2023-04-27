import cv2
import os
dir_path = './Images'
save_folder = './Cropped Images'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def image_cropper(img_path, save_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # need to loop through each folder, each file open it and crop it and replace it.
    faces = face_cascade.detectMultiScale(gray, 1.2, 6)
    for i, (x, y, w, h) in enumerate(faces):
        # Crop the face region from the original image
        face = img[y-20:y+h+20, x-20:x+w+20]
        cv2.imwrite(save_path, face)
        print('done!')


# Looping through each folder
for foldername in os.listdir(dir_path):
    folder_path = os.path.join(dir_path, foldername)

    folder_save_dir = os.path.join(save_folder, foldername)
    os.makedirs(folder_save_dir, exist_ok=True)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        save_path = os.path.join(folder_save_dir, file)
        try:
            image_cropper(file_path, save_path)
        except:
            print('error')
