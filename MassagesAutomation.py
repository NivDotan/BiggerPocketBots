from bs4 import BeautifulSoup
import requests
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time



workbook = load_workbook(filename="C:/Users/niv/Downloads/NWICopy.xlsx")
sheet = workbook.active




def GetUserID(x,index):
    r = requests.get('https://www.biggerpockets.com/search/users?term=' + x)
    soup = BeautifulSoup(r.text, "html.parser")
    ChatID = soup.findAll(class_='search-result-user-name')
    for link in ChatID:
        if (link['href']):
            ChatID = link['href']
            print(ChatID)
            break

    ChatID = ChatID[(ChatID.find('users') + 6):]

    r = requests.get("https://www.biggerpockets.com/users/" + ChatID)
    soup = BeautifulSoup(r.text, "html.parser")
    ChatID = soup.findAll(class_='cover-image-element')
    for link in ChatID:
        if (link['src']):
            ChatID = link['src']
            break

    t = ChatID[(ChatID.find('user_avatar') + 12):]
    temp2 = []
    for i in t:
        if i == '/':
            break
        temp2.append(i)

    MassageID = ''.join(temp2)
    print("https://www.biggerpockets.com/conversations/new?ids=" + MassageID)
    print(str(index))
    print(index)
    sheet['B' + str(index)] = MassageID

    workbook.save(filename="C:/Users/niv/Downloads/NWICopy.xlsx")

def sendMassage(ID):
    options = Options()
    options.add_argument('user-data-dir=C:/Users/niv/AppData/Local/Google/Chrome/User Data')
    options.add_argument('profile-directory=Person 1')
    driver = webdriver.Chrome(executable_path='C:/Users/niv/Downloads/chromedriver', chrome_options=options)

    driver.get("https://www.biggerpockets.com/conversations/new?ids=" + ID)
    time.sleep(3)
    input_1 = driver.find_element("css selector", "input[id='conversation_subject']")
    input_1.click()
    time.sleep(3)

    input_1.send_keys('MASSAGE')
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//html/body/div[4]/div/div/div/div[2]/form/div[3]/div[1]/div/div/div"))).send_keys('MASSAGE')
    time.sleep(3)
    Submit = driver.find_element("css selector", "input[value='Send Message']")

    time.sleep(3)
    Submit.click()
    time.sleep(3)


def main():
    workbook = load_workbook(filename="C:/Users/niv/Downloads/NWICopy.xlsx")
    sheet = workbook.active
    AcuuntNameCol = sheet['A']
    i = 1


    #options = Options()
    #options.add_argument('user-data-dir=C:/Users/niv/AppData/Local/Google/Chrome/User Data')
    #options.add_argument('profile-directory=Person 1')
    #C:                                     \Users\niv\AppData\Local\Google\Chrome\User Data\Person 1
    #driver = webdriver.Chrome(executable_path='C:/Users/niv/Downloads/chromedriver',chrome_options=options)



    #AcuuntNameCol = ['Arie Bitton','Chris Mullinax','Wendy Stclair']
    #AcuuntNameCol = ['Amit Rozen']

    for x in AcuuntNameCol:
        GetUserID(x.value,i)
        i = i + 1
        '''
        r = requests.get('https://www.biggerpockets.com/search/users?term=' + x)
        soup = BeautifulSoup(r.text, "html.parser")
        ChatID = soup.findAll(class_='search-result-user-name')
        for link in ChatID:
            if (link['href']):
                ChatID = link['href']
                print(ChatID)
                break

        ChatID = ChatID[(ChatID.find('users') + 6):]



        r = requests.get("https://www.biggerpockets.com/users/" + ChatID)
        soup = BeautifulSoup(r.text, "html.parser")
        ChatID = soup.findAll(class_='cover-image-element')
        for link in ChatID:
            if (link['src']):
                ChatID = link['src']
                break

        t = ChatID[(ChatID.find('user_avatar') + 12):]
        temp2 = []
        for i in t:
            if i == '/':
                break
            temp2.append(i)

        MassageID = ''.join(temp2)
        MassageID = '2549559'
        print("https://www.biggerpockets.com/conversations/new?ids="+ MassageID)

        '''

        #Get the massages URL and send a massage
        '''
        driver.get("https://www.biggerpockets.com/conversations/new?ids="+ '2549559')
        time.sleep(3)
        input_1 = driver.find_element("css selector","input[id='conversation_subject']")
        input_1.click()
        time.sleep(3)
        #myInputElm.clear();

        input_1.send_keys('MASSAGE')
        time.sleep(3)
        #input_2 = driver.find_element("css selector","class=notranslate public-DraftEditor-content")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//html/body/div[4]/div/div/div/div[2]/form/div[3]/div[1]/div/div/div"))).send_keys('MASSAGE')
        time.sleep(3)
        Submit = driver.find_element("css selector","input[value='Send Message']")


        time.sleep(3)

        Submit.click()
        time.sleep(3)
        '''

main()