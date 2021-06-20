import re

import pyperclip

# 利用括号分组
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))

# 用管道匹配多个分组
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# 用问号实现可选匹配
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# 用星号匹配零次或多次
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# 用加号匹配一次或多次
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
ans: bool = True if mo3 is None else False
print(ans)

# 用花括号匹配特定次数
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 is None)

# 贪心和非贪心匹配
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# 415-555-4242 ext 33  334230789@qq.com

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
(\d{3}) # first 3 digits
(\s|-|\.) # separator
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
 [a-zA-Z0-9._%+-]+ # username
 @ # @ symbol
 [a-zA-Z0-9.-]+ # domain name
(\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(matches)

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

import os

print(os.path.join('/', 'user', 'bin', 'spam'))
print(os.getcwd())
os.chdir('/Users')
print(os.getcwd())
print(os.path.abspath("../../Extension"))
print(os.path.isabs("../../Extension"))
print(os.path.isabs(os.path.abspath("../../Extension")))
print(os.path.relpath("/Users", "/Users/tony"))
print(os.path.dirname("/Users/tony"))
print(os.path.basename("/Users/tony"))
print(os.path.split("/Users/otny"))
print(os.path.dirname("/Users/tony"))
print(os.path.basename("/Users/tony"))
print(os.path.getsize("/Users/tony"))
print(os.listdir("/Users/tony"))
# os.path.exists()
# os.path.isdir()
# os.path.isfile()
import shelve

shelfFile = shelve.open("/Users/tony/Tony/test1.sh")
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile1 = shelve.open("/Users/tony/Tony/test1.sh")
print(list(shelfFile1.keys()))
print(list(shelfFile1.values()))
shelfFile1.close()

# import pprint
for folderName, subfolders, filenames in os.walk('/Users/tony/Tony'):
    print('The current folder is '.ljust(23) + folderName.ljust(25, '•'))
    for subfolder in subfolders:
        print('SUBFOLDER OF '.ljust(23) + folderName.ljust(25, '•') + ': ' + subfolder.rjust(15))
    for filename in filenames:
        print('FILE INSIDE '.ljust(23) + folderName.ljust(25, '•') + ': ' + filename.rjust(15))

import zipfile
import os

os.chdir('/Users/tony/Tony')  # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('test.sh')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()

import zipfile

newZip = zipfile.ZipFile('example1.zip', 'w')
newZip.write('test.sh', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
