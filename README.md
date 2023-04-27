# Nepali-Celeb-Localized-Face-Dataset
Face images of 49 famous individuals from Nepal, including actors, singers

# About Dataset

Dataset Link : https://www.kaggle.com/datasets/amitpant7/nepali-celeb-localized-face-dataset

The dataset contains images of 49 famous individuals from Nepal, including actors, actresses, singers, and social figures.

The individuals in the dataset vary in age, gender, and profession. The images were taken from different angles and forms, including front-facing, side-facing, and profile views, to capture each individual's facial features.

However, it is possible that there could be some errors or inconsistencies in the dataset, such as variations in lighting or image quality. It is important to carefully review and preprocess the images before using them in any analysis or application.

Regarding potential uses for this dataset, it could be used for tasks such as face recognition, face detection, and emotion recognition. Additionally, it could be used to train and evaluate machine learning models for tasks related to facial analysis.

# Procedure

Firstly, I started by collecting all the images of the actors from the internet. Since I had some experience with Python, I decided to write a script to automate the process. However, I found that using Selenium wasn't yielding the results I wanted, so I explored other options.

After some research, I found that bing_image_downloader was a good tool to use for downloading images. I installed the package using the pip install bing_image_downloader command in the terminal. Then, I wrote a Python script that utilized the bing_image_downloader library to download images of each actor in the dataset.

Once I had downloaded all the images, I compiled them into a single directory and made sure to manually verify the quality of each image. Since the images were from different sources, the quality varied considerably. I removed any images that were too blurry or had any other issues that would make them unsuitable for the dataset.

Next, I used OpenCV library to detect faces in the images using the Haar Cascade classifier algorithm. This allowed me to automatically crop the image to extract only the face region. I then used the resize function in OpenCV to resize the cropped face image to a standard size.

Finally, I saved the processed images in a separate directory with appropriate naming convention. I named the images with the actor's name followed by an index number to ensure uniqueness.
