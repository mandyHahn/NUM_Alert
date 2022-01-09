from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import showToast
import os
import threading

# Needed installations:
# pip install selenium


class COVIDAlert:
    # Constructor
    # notificationDuration - How long the notification will be on screen (in seconds)
    # timeBetweenAlert - The time (in minutes) between notifications
    def __init__(self, notificationDuration, timeBetweenAlert):
        self.notificationDuration = notificationDuration
        self.timeBetweenAlert = timeBetweenAlert
        current_dir = os.path.dirname(os.path.realpath(__file__))  # Create an object to the current directory
        chromeOptions = Options()  # Create what options you're going to be using
        chromeOptions.headless = True  # Make non-visible
        driver = webdriver.Chrome(current_dir + "/chromedriver.exe", options=chromeOptions)  # Create the chrome driver
        driver.get("https://www.worldometers.info/coronavirus/")  # Get the website from the driver
        # Wait up to 10 seconds to get the data from the covid case website
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="odd" or @class="even"]')))
        # Find the country name
        countryNames = driver.find_elements(By.XPATH, '//*[@class="odd" or @class="even"]//child::td//child::a[@class="mt_a"]')
        # Find the amount of active cases
        countryActiveCases = driver.find_elements(By.XPATH, '//*[contains(@style, "text-align:right;font-weight:bold;")]')
        self.covDic = {}  # Use a dictionary to associate the names to the amount of cases
        for i in range(0, 30):
            self.covDic[countryNames[i].text] = countryActiveCases[i].text
        self.timer = None  # Create an empty timer instance variable

    # createTimer - Create a timer for the COVIDAlerts
    # country - The country of interest
    def createTimer(self, country):
        self.timer = threading.Timer(self.timeBetweenAlert * 60, self.sendAlert, args=[country])
        self.timer.start()

    # sendAlert - Send the COVID alert
    # country - The country of interest
    def sendAlert(self, country):
        showToast("COVID Update",
                  f"{country} currently has {self.covDic[country]} total active cases!",
                  self.notificationDuration)
        self.createTimer(country)
