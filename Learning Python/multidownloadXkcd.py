import threading
import bs4
import requests
import os
import sys

os.makedirs('/Users/tony/Tony/xkcd', exist_ok=True)  # store comics in xkcd/


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        url = 'https://xkcd.com/%s' % urlNumber
        print('Downloading page ', url)
        res = requests.get(url)
        # print('page status_code:', res.status_code)
        if res.status_code != 200:
            sys.exit(res.status_code)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)
        # print('soup: ', soup)
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        # print('comicElem:', comicElem[0].get('src'))
        if not comicElem:
            print('Cound not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % comicUrl)
            res = requests.get('http:' + comicUrl)
            if res.status_code != 200:
                sys.exit(res.status_code)
            # print('image status_code: ', res.status_code)
            # res.raise_for_status()

            # Save the image to xkcd/
            imageFile = open(os.path.join('/Users/tony/Tony/xkcd/', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# Create and start the Thread object.
downloadThreads = []    # a list of all the thread objects
for i in range(0, 1400, 100):  # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
