
from bs4 import BeautifulSoup
import requests
from openpyxl import load_workbook


def CheckByCityName(city,KindOfCity,workbook,sheet,FilePath):
    addWords = ["IN", "Indiana", "NWI", "NW Indiana", "NW IN", "North West Indiana"] #Pass it as input Words for input
    addWords2 = ["Indiana", "NWI", "NW Indiana", "NW IN", "North West Indiana"]

    if KindOfCity == 2:
        sortingKind = '&sort=date&term=' #sorting the posts by date
    else:
        sortingKind = '&sort=&term=' #sorting the posts by relevent

    i = 1
    str_links = wordSearch = postLink = NamesList = PostList = DatesList = DatesListExcel = ([] for i in range(7))
    NameIndex = 0
    NumberOfPages = 20 #The number of pages that you want to search in

    while i < NumberOfPages:
        r = requests.get('https://www.biggerpockets.com/search/topics?page=' + str(i) + sortingKind + city)
        soup = BeautifulSoup(r.text, "html.parser")
        Names = soup.findAll('a', class_="search-result-topic-author")#Get the user of the topic author
        Titles = soup.findAll('a', class_="search-result-title") #Get also the link from there and paste it in the DB
        Dates = soup.findAll(class_="search-result-details") #Get the date of the post

        for name in Names:
            if (name['href']):
                ChatID = name['href']
                ChatID = ChatID[(ChatID.find('users') + 6):]
                NamesList.append(ChatID)

        for link in Titles:
            if (link['href']):
                PostID = link['href']
                PostList.append(PostID)

        for link in Dates:
            pr = link.text
            DatesList.append(pr)

        for title in Titles:
            pr = title.text
            if KindOfCity == 2:#If you pass a place that is not a city
                for word in addWords:
                    if (word in pr):
                        str_links.append(NamesList[NameIndex])
                        wordSearch.append(city)
                        postLink.append(PostList[NameIndex])
                        DatesListExcel.append(DatesList[NameIndex])
                        break

            else:
                if city in pr: #add or city in the subject or ["Indiana", "NWI", "NW Indiana", "NW IN", "North West Indiana"]
                    str_links.append(NamesList[NameIndex])
                    wordSearch.append((city))
                    postLink.append(PostList[NameIndex])
                    DatesListExcel.append(DatesList[NameIndex])
                    break
                else:
                    for word in addWords2:
                        if word in pr:
                            str_links.append(NamesList[NameIndex])
                            wordSearch.append((word + city))
                            postLink.append(PostList[NameIndex])
                            DatesListExcel.append(DatesList[NameIndex])
                            break
            NameIndex = NameIndex + 1

        i = i + 1 #Move to the next page
    WritingInExcel(str_links,wordSearch,postLink,DatesListExcel,workbook,sheet,FilePath)


def WritingInExcel(str_links,wordSearch,postLink,DatesListExcel,workbook,sheet,FilePath):
    i = len(sheet['A']) #Get the last row
    j = 0
    for a in str_links:
        if (CheckingEachOne(str_links[j])) != False: #Print the info in the DB
            sheet["A"+str(i)] = str_links[j]
            sheet["B" + str(i)] = wordSearch[j]
            sheet["C" + str(i)] = postLink[j]
            sheet["D" + str(i)] = DatesListExcel[j]
        j = j + 1
        i = i + 1
    workbook.save(filename=FilePath)


def CheckingEachOne(name,sheet): #Checking if the name is already in the DB
    for cell in sheet['A']:
        if (cell.value == name):
            return False
    return True



def mainRun():
    FilePath = "C:/Users/USERNAME/Documents/FILENAME" #Enter you DB path (where you want to store your user id)
    workbook = load_workbook(filename=FilePath)
    sheet = workbook.active

    #Cities from where you want to get users
    MainRunArray = [ "NWI",'Hammond',  "Elkhart", 'South+Bend','Gary', 'East+Chicago', 'Michigan+City', 'La+Porte']

    #pos = 1
    for i in MainRunArray:
        print(i)
        if (i == "NWI"):# NWI (North-West Indiana) is a name for a large place and to a city
            CheckByCityName(i, 2,workbook,sheet,FilePath)
        else:
            CheckByCityName(i, 1,workbook,sheet,FilePath)

        #pos = pos +1

mainRun()
