from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from datetime import date

postal = int(input('Enter the postal code: '))
options = Options()

#Replace with path to browser executable
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Initialize the web driver (make sure you have the appropriate webdriver installed)
chrome_path = r"C:\Users\isaac\Downloads\chromedriver-win64\chromedriver.exe"

# Create a Service object
chrome_service = ChromeService(executable_path=chrome_path)

# Initialize Chrome browser
driver = webdriver.Chrome(service=chrome_service, options=options)



# Open the form URL
form_url = ""
driver.get(form_url)


file_path = "data.txt"
data_list = []

with open('data.txt', 'r') as file:
    lines = file.read().split('\n\n')  # Assumes paragraphs are separated by two newlines
    
    for paragraph in lines:
        paragraph_dict = {}
        for i, line in enumerate(paragraph.split('\n'), 1):
            paragraph_dict[f'key{i}'] = line.strip()
        data_list.append(paragraph_dict)

for x in range((len(data_list))):

    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[4]/div[1]/div[1]/form/div[1]/div/div[1]/div[2]/div/div/input").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div[1]/div[1]/form/div[1]/div/div[1]/div[2]/div/div/input").send_keys("Scam")
    time.sleep(1)
    # below line will press enter key
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div[1]/div[1]/form/div[1]/div/div[1]/div[2]/div/div/input").send_keys(Keys.ENTER)

    time.sleep(1)
    today = date.today()
    date1 = today.strftime('%d%m%Y')
    driver.find_element(By.ID, "64ffdde72bf4c800121af608").click()

    driver.find_element(By.ID, "64ffdde72bf4c800121af608").send_keys(date1)

    time.sleep(1)
    driver.find_element(By.ID, "64ffde1b869057001275d1ad").send_keys(postal)
    driver.find_element(By.ID, "64ffe0809ebd2000125e749f").send_keys(data_list[x].get('key1'))
    driver.find_element(By.ID, "64ffdeeddf2e250012da5b76").send_keys(data_list[x].get('key2'))

    #To check if data inlcudes personal particulars to press yes/no
    y = (type(data_list[x].get('key3')))

    if y is type(None):
        #Press No
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[4]/div[1]/div[1]/form/div[1]/div/div[6]/div[2]/label[1]/div").click()
    else:
        #Press Yes
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div[1]/div[1]/form/div[1]/div/div[6]/div[2]/label[2]/div").click()
        driver.find_element(By.ID, "64ffdf0d78305700125ac23c").send_keys(data_list[x].get('key3'))
        driver.find_element(By.ID, "64ffdf2f9ebd2000125e2d9e").send_keys(data_list[x].get('key6'))
        driver.find_element(By.ID, "64ffdfc36272300011110eb4").send_keys(data_list[x].get('key5'))
        if "Mr " in data_list[x].get('key3'):
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div[1]/div[1]/form/div[1]/div/div[9]/div[2]/label[1]/span[1]").click()
        else:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div[1]/div[1]/form/div[1]/div/div[9]/div[2]/label[2]").click()
           
        driver.find_element(By.ID, "64ffdfda62723000111113c5").send_keys(data_list[x].get('key4'))

    time.sleep(10)

    #SUBMIT BUTTON
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div[1]/div[1]/form/div[2]/button").click()

    time.sleep(10)
    driver.refresh()

input()
driver.quit()
