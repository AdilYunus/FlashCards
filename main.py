import csv,json
from PyQt5 import QtWidgets, uic
import sys
import os
import login

csvFilePath = 'nl_words_4data.csv'
jsonFilePath = 'nl_words_4data.json'

#read csv file & add data
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows,i in zip(csvReader,range(1,5001)):
        data[i] = rows

        
        
with open(jsonFilePath,'w') as jsonFile:

    jsonFile.write(json.dumps(data, indent=4))


app = QtWidgets.QApplication(sys.argv)
window = login.Login()
app.exec_()