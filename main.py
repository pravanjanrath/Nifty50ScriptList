import pandas
from selenium import webdriver
import time
import shutil
import os
import glob


SYMBOLS_FILE = "C:\\Users\\prava\\Downloads\\data.csv"
SYMBOLS_PATH = "C:\\Users\\prava\\Downloads\\"
NSE_NIFTY50_URL = "https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm"


def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver


def read_data():
    df = pandas.read_csv("data.csv")
    symbols = df["Symbol"][1:].tolist()
    return symbols


def write_output(symbols):
    with open("output.txt", "w") as file:
        for symbol in symbols:
            if symbol == "BAJAJ-AUTO":
                symbol = symbol.replace("-", "_")
            elif symbol == "M&M":
                symbol = symbol.replace("&", "_")
            file.write(f"{symbol},")


def del_previous_files():
    filepaths = glob.glob(f"{SYMBOLS_PATH}data*.csv")
    print(filepaths)
    for filepath in filepaths:
        if os.path.isfile(filepath):
            os.remove(filepath)


def main():
    del_previous_files()
    driver = get_driver(NSE_NIFTY50_URL)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div[2]/div/div[1]/div[1]/div[1]/a[2]").click()
    time.sleep(2)
    shutil.copy(SYMBOLS_FILE, os.getcwd())
    symbols = read_data()
    write_output(symbols)


if __name__ == '__main__':
    main()
    print("******************************")
    print("Latest Nifty50 data is imported. Open Trading View and add all the latest scripts from output.txt.")
    print("******************************")

