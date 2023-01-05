
from bs4 import BeautifulSoup
import requests
from openpyxl import load_workbook


def CheckByCityName(city,KindOfCity,workbook,sheet,FilePath):
    addWords = ["IN", "Indiana", "NWI", "NW Indiana", "NW IN", "North West Indiana"] #Pass it as input Words for input
    addWords2 = ["Indiana", "NWI", "NW Indiana", "NW IN", "North West Indiana"]

    if KindOfCity == 2:
        sortingHat = '&sort=date&term='
    else:
        sortingHat = '&sort=&term='

    i = 1
    str_links = wordSearch = postLink = NamesList = PostList = DatesList = DatesListExcel = ([] for i in range(7))
    NameIndex = 0
    NumberOfPages = 20
    while i < NumberOfPages:
        print('Page: ', i)
        r = requests.get('https://www.biggerpockets.com/search/topics?page=' + str(i) + sortingHat + city)
        soup = BeautifulSoup(r.text, "html.parser")
        Names = soup.findAll('a', class_="search-result-topic-author")#search-result-topic-author -> user ID same as what i did in the PC
        Titles = soup.findAll('a', class_="search-result-title") # get also the link from there and paste it in the excel
        Dates = soup.findAll(class_="search-result-details") # get also the link from there and paste it in the excel

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


        #NumOfPost = 2
        for title in Titles:
            pr = title.text
            if KindOfCity == 2:
                for word in addWords:
                    if (word in pr):
                        str_links.append(NamesList[NameIndex])
                        wordSearch.append(city)
                        postLink.append(PostList[NameIndex])
                        DatesListExcel.append(DatesList[NameIndex])
                        #print("NamesList[NameIndex]", NamesList[NameIndex])
                        break

            else:
                if city in pr: #add or city in the subject or ["Indiana", "NWI", "NW Indiana", "NW IN", "North West Indiana"]
                    str_links.append(NamesList[NameIndex])
                    wordSearch.append((city))
                    postLink.append(PostList[NameIndex])
                    DatesListExcel.append(DatesList[NameIndex])
                    #print("NamesList[NameIndex]", NamesList[NameIndex])
                    break
                else:
                    for word in addWords2:
                        if word in pr:
                            str_links.append(NamesList[NameIndex])
                            wordSearch.append((word + city))
                            postLink.append(PostList[NameIndex])
                            DatesListExcel.append(DatesList[NameIndex])
                            #print("NamesList[NameIndex]", NamesList[NameIndex])
                            break
            NameIndex = NameIndex + 1

        i = i + 1
    #print("str_links,wordSearch,postLink,DatesListExcel",str_links, " ",wordSearch," ",postLink," ",DatesListExcel)
    WritingInExcel(str_links,wordSearch,postLink,DatesListExcel,workbook,sheet,FilePath)


def WritingInExcel(str_links,wordSearch,postLink,DatesListExcel,workbook,sheet,FilePath):
    i = len(sheet['A'])
    print(DatesListExcel)
    print(i)
    j = 0
    #while i<(len(str_links)+1):
    for a in str_links:
        #if (CheckingEachOne(str_links[i-1])) != False:
        if (CheckingEachOne(str_links[j])) != False:
            sheet["A"+str(i)] = str_links[j]
            sheet["B" + str(i)] = wordSearch[j]
            sheet["C" + str(i)] = postLink[j]
            sheet["D" + str(i)] = DatesListExcel[j]
        j = j + 1
        i = i + 1
    workbook.save(filename=FilePath)


def CheckingEachOne(name,sheet):
    for cell in sheet['A']:
        if (cell.value == name):
            return False
    return True



def mainRun():
    FilePath = "" #Enter you DB path (where you want to store your user id)
    workbook = load_workbook(filename=FilePath)
    sheet = workbook.active
    MainRunArray = [ "NWI",'Hammond',  "Elkhart", 'South+Bend','Gary', 'East+Chicago', 'Michigan+City', 'La+Porte']
    #['Hammond', "elkhart", 'South Bend','Gary', 'East Chicago', 'Michigan City', 'la porte',] kind == 1
    #MainRunArray = ["NWI"] kind == 2
    #MainRunArray = ["NWI"]
    pos = 1
    for i in MainRunArray:
        print(i)
        if (i == "NWI"):
            #if (i == "NWI"):
            print(i)
            CheckByCityName(i, 2,workbook,sheet,FilePath)
        else:
            CheckByCityName(i, 1,workbook,sheet,FilePath)

        pos = pos +1
    #print(len(str_links))
    #print(str_links)

mainRun()



