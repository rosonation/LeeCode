import os

import bs4
import requests

url = 'https://xkcd.com'
os.makedirs('/Users/tony/Tony/xkcd', exist_ok=True)
while not url.endswith('#'):
    # Downlaod the page
    print("Downloading page %s ..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("Cound not find comic image.")
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image.
        print("Downloading image %s..." % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to /Users/tony/Tony/xkcd.
        imageFile = open(os.path.join('/Users/tony/TOny/xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print("Download Done.")
