import requests

res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])

res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % exc)

import requests

res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('/Users/tony/Tony/RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
