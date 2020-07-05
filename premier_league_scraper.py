import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

#============================== File Setup =========================================
urls = "https://en.wikipedia.org/wiki/2014%E2%80%9315_Premier_League"

page = requests.get(urls)
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.find_all('table', class_ = 'wikitable')[3]

#============================== List setup ==========================================
rowValList = []
new_List = []
converted_List = []
converted_List1 = []

#============================== Setup of table ======================================
for i in range(len(tables.find_all('td'))):
    rowVal = tables.find_all('td')[i].get_text()
    rowValList.append(rowVal)

for element in rowValList:
    converted_List.append(element.strip())

delety_list = ['Qualification', 'Relegation', 'League']

my_list = [el for el in converted_List if not any(ignore in el for ignore in delety_list)]
for i in my_list:
    if i not in (''):
        converted_List1.append(i)

#=================================== Table creation ====================================
teamList = []
for i in range(0, len(converted_List1), 9):
    teamList.append(converted_List1[i])

playList = []
for i in range(1, len(converted_List1), 9):
    playList.append(converted_List1[i])

wonList = []
for i in range(2, len(converted_List1), 9):
    wonList.append(converted_List1[i])

drawList = []
for i in range(3, len(converted_List1), 9):
    drawList.append(converted_List1[i])

lossList = []
for i in range(4, len(converted_List1), 9):
    lossList.append(converted_List1[i])

GFList = []
for i in range(5, len(converted_List1), 9):
    GFList.append(converted_List1[i])

GAList = []
for i in range(6, len(converted_List1), 9):
    GAList.append(converted_List1[i])

GDList = []
for i in range(7, len(converted_List1), 9):
    GDList.append(converted_List1[i])

pointsList = []
for i in range(8, len(converted_List1), 9):
    pointsList.append(converted_List1[i])

pl_Goal_difference = []

plDF = pd.DataFrame()
# ===================== Build lists with certain types ===============================
plDF['Team'] = teamList
plDF['Played'] = playList
plDF['Won'] = wonList
plDF['Draw'] = drawList
plDF['Loss'] = lossList
plDF['GF'] = GFList
plDF['GA'] = GAList
plDF['GD'] = GDList
plDF['Points'] = pointsList
# ======================= Convert types ==============================================
# plDF['Team'] = plDF['Team'].astype(int)
plDF['Played'] = plDF['Played'].astype(int)
plDF['Won'] = plDF['Won'].astype(int)
plDF['Draw'] = plDF['Draw'].astype(int)
plDF['Loss'] = plDF['Loss'].astype(int)
plDF['GF'] = plDF['GF'].astype(int)
plDF['GA'] = plDF['GA'].astype(int)
plDF['Points'] = plDF['Points'].astype(int)
plDF['pl_Goal_difference'] = plDF['GF'] - plDF['GA']
print(plDF)

#================================= File Saving =====================================
plDF.to_csv("plDF1415.csv")
