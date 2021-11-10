import csv
import json
from PyQt5 import QtWidgets, uic
import sys
import os
import login

csvFilePath = 'nl_words_4data.csv'
jsonFilePath = 'nl_words_4data.json'

# read csv file & add to data dict.
data = {}
with open(csvFilePath, encoding='utf-8') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows, i in zip(csvReader, range(1, 5001)):
        data[i] = rows
#open json file and write data to json file
with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile:

    jsonFile.write(json.dumps(data, indent=4))


app = QtWidgets.QApplication(sys.argv)
window = login.Login()
app.exec_()
