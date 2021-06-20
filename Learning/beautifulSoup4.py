import bs4

# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text)
# print(type(noStarchSoup))

# print(exampleSoup.select('div'))                       # 所有名为<div>的元素
# print(exampleSoup.select('#author'))                   # 带有 id 属性为 author 的元素
# print(exampleSoup.select('.notice'))                   # 所有使用 CSS class 属性名为 notice 的元素
# print(exampleSoup.select('div span'))                  # 所有在<div>元素之内的<span>元素
# print(exampleSoup.select('div > span'))                # 所有直接在<div>元素之内的<span>元素，中间没有其他元素
# print(exampleSoup.select('input[name]'))               # 所有名为<input>，并有一个 name 属性，其值无所谓的元素
# print(exampleSoup.select('input[type="button"]'))      # 所有名为<input>，并有一个 type 属性，其值为 button 的元素
exampleFile = open('/Users/tony/Tony/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, features='html.parser')
print(type(exampleSoup))
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print("-----------------")
print(pElems[0].getText())
print("-----------------")
print(str(pElems[1]))
print("-----------------")
print(pElems[1].getText())
print("-----------------")
print(str(pElems[2]))
print("-----------------")
print(pElems[2].getText())
