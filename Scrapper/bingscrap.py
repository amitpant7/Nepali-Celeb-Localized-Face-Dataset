from bing_image_downloader import downloader


def download_images(request):
    try:
        downloader.download(request,
                        limit=50,
                        output_dir='Images',
                        adult_filter_off=False,
                        force_replace=False,
                        timeout=60)
    except:
        print('Error occured while downloading images for {}'.format(request))
actors = list()

with open('./actors.txt', 'r') as f:
    for line in f:
        actors.append(line.strip())


for actor in actors:
    download_images(actor)