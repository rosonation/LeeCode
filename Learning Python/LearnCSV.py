import csv
downPath='/Users/tony/Downloads/automate_online-materials'
exampleFile = open(downPath + '/example.csv')
exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# print(exampleData)
# print(exampleData[0][0])
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))