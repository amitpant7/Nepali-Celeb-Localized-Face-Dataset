from selenium import webdriver
import requests
import io
from PIL import Image
import time
from selenium.webdriver.common.by import By

PATH = 'Z:\\Projects\\Which Nepali Celibratey\\Scrapper\\chromedriver.exe'
wd = webdriver.Chrome(PATH)


def download_google_images(wd, delay, max_img):
    def scroll_down():
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)
    src = 'https://www.google.com/search?q=rajesh+hamal&rlz=1C1PNKB_en__1020NP1020&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiflZmjtsn-AhX_6jgGHXA7DIEQ_AUoAXoECAEQAw&biw=1038&bih=600&dpr=1.35'
    wd.get(src)

    image_urls = set()
    while len(image_urls) < max_img:
        scroll_down()
        thumbnails = wd.find_elements(By.CLASS_NAME, 'iPVvYb')
        for img in thumbnails[len(image_urls):max_img]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue
            images = wd.find_elements(By.CLASS_NAME, "iPVvYb")
            for image in images:
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"Found {len(image_urls)}")
    return(image_urls)


def download_image(dir_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = dir_path + file_name
    except Exception as e:
        print('Failed', e)

    with open(file_path, 'wb') as f:
        image.save(f, 'JPEG')
    print('Done done ! boii')


image_urls = download_google_images(wd, 1, 10)
wd.quit()
