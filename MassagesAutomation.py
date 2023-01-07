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


# Function that get the user id from the username
def GetUserID(x, index, workbook, sheet, FilePath):
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
    sheet['B' + str(index)] = MassageID

    workbook.save(filename=FilePath)
    return MassageID


# Function that send the massage to the user
def sendMassage(ID):
    options = Options()
    options.add_argument(
        'user-data-dir=C:/Users/USERNAME/AppData/Local/Google/Chrome/User Data')  # Where your chrome is installed
    options.add_argument('profile-directory=Person 1')
    driver = webdriver.Chrome(executable_path='C:/Users/USERNAME/Downloads/chromedriver',
                              chrome_options=options)  # Where your chromedriver is installed

    driver.get("https://www.biggerpockets.com/conversations/new?ids=" + ID)
    time.sleep(3)
    input_1 = driver.find_element("css selector", "input[id='conversation_subject']")
    input_1.click()
    time.sleep(3)

    input_1.send_keys('MASSAGE')  # Enter here your massage
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//html/body/div[4]/div/div/div/div[2]/form/div[3]/div[1]/div/div/div"))).send_keys('MASSAGE')
    time.sleep(3)
    Submit = driver.find_element("css selector", "input[value='Send Message']")

    time.sleep(3)
    Submit.click()
    time.sleep(3)


def main():
    FilePath = "C:/Users/USERNAME/Documents/FILENAME"  # Enter you DB path (where you want to store your user id)
    workbook = load_workbook(filename=FilePath)
    sheet = workbook.active
    AcuuntNameCol = sheet['A']
    i = 1

    # Function for move all over the user name in the DB
    # Each name will be sent to the GetUserID

    for cell in sheet['A']:
        MassageID = GetUserID(cell.value, i, workbook, sheet, FilePath)
        sendMassage(MassageID)
        i = i + 1


main()



