from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from User_agent import agent
from selenium.webdriver.chrome.service import Service
import sys
import math

# Making chrome headless
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(f"user-agent={agent}")
chrome_options.add_argument("--no-sandbox")



window = webdriver.Chrome(executable_path="/root/chromedriver-linux64/chromedriver", options=chrome_options)

pages = 0

url = sys.argv[1]

# checks if the url is vaild
if "house" in url:
    print("Invaild Link")
    exit()
elif "condos" in url:
    print("Invaild Link")
    exit()
elif "townhomes" in url:
    print("Invaild Link")
    exit()

window.get(url)  # open chrome and goes to url


try:
    # Attempt to find the number of pages
    pages_text = window.find_element(By.CLASS_NAME, "pageRange").text
    pages = int(pages_text.split(" ")[-1])
    window.quit()

    # Adjust the number of pages
    if pages > 10:
        pages = math.floor(pages / 2) if pages % 2 else int(pages / 2)

except Exception:
    pass

info = ""
aparment_info = []

# Checks what type of link is given
# links with or without ?
if url.find("?") == -1:

    # goes through each page and grabs the data
    for web in range(1, pages + 1):
        url = f"{url}{web}"  # adds the page number to url

        noQ_driver = webdriver.Chrome(executable_path="/root/chromedriver-linux64/chromedriver", options=chrome_options)

        noQ_driver.get(url)

        # finds the number apartments on the page
        base_cards = noQ_driver.find_elements(
            By.XPATH, '//*[@id="placardContainer"]/ul/li'
        )

        # goes thourgh each apartment cards and gets the Name, Address, Cost, Room, Number and extra Info
        for i in range(1, len(base_cards)):
            try:
                name = noQ_driver.find_element(
                    By.XPATH,
                    f'//*[@id="placardContainer"]/ul/li[{i}]/article/header/div[1]/a/div[1]/span',
                )
                address = noQ_driver.find_element(
                    By.XPATH,
                    f'//*[@id="placardContainer"]/ul/li[{i}]/article/header/div[1]/a/div[2]',
                )
                cost = noQ_driver.find_element(
                    By.CSS_SELECTOR,
                    f"#placardContainer > ul > li:nth-child({i}) > article > section > div > div.property-info > div > div.top-level-info > a > p.property-pricing",
                )
                room = noQ_driver.find_element(
                    By.XPATH,
                    f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[1]/a/p[2]',
                )
                try:
                    number = noQ_driver.find_element(
                        By.XPATH,
                        f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[2]/a/span',
                    )
                except:
                    number = noQ_driver.find_element(
                        By.XPATH,
                        f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[3]/a/span',
                    )
                try:  # some apartments don't have extra info so
                    info = noQ_driver.find_element(
                        By.XPATH,
                        f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/a/p',
                    )
                except Exception:
                    pass

                if info != "":
                    aparment_info.append(  # Adds information into a list
                        [
                            name.text,
                            address.text,
                            cost.text,
                            room.text,
                            number.text,
                            info.text,
                        ]
                    )
                else:
                    aparment_info.append(
                        [name.text, address.text, cost.text, room.text, number.text]
                    )
            except Exception:
                pass
        noQ_driver.quit()

elif url.find("?") != -1:
    split_url = url.split("?")  # seprates the link intoo two

    # goes through each page and grabs the data
    for web in range(1, pages + 1):
        url = f"{split_url[0]}/{web}/?{split_url[1]}"  # adding the page number to the link

        Q_driver = webdriver.Chrome(executable_path="/root/chromedriver-linux64/chromedriver", options=chrome_options)
        Q_driver.get(url)

        # finds the number apartments on the page
        base_cards = Q_driver.find_elements(
            By.XPATH, '//*[@id="placardContainer"]/ul/li'
        )

        # goes thourgh each apartment cards and gets the Name, Address, Cost, Room, Number and extra Info
        for i in range(1, len(base_cards)):
            try:
                name = Q_driver.find_element(
                    By.XPATH,
                    f'//*[@id="placardContainer"]/ul/li[{i}]/article/header/div[1]/a/div[1]/span',
                )
                address = Q_driver.find_element(
                    By.XPATH,
                    f'//*[@id="placardContainer"]/ul/li[{i}]/article/header/div[1]/a/div[2]',
                )
                cost = Q_driver.find_element(
                    By.CSS_SELECTOR,
                    f"#placardContainer > ul > li:nth-child({i}) > article > section > div > div.property-info > div > div.top-level-info > a > p.property-pricing",
                )
                room = Q_driver.find_element(
                    By.XPATH,
                    f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[1]/a/p[2]',
                )
                try:
                    number = Q_driver.find_element(
                        By.XPATH,
                        f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[2]/a/span',
                    )
                except:
                    number = Q_driver.find_element(
                        By.XPATH,
                        f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[3]/a/span',
                    )
                try:
                    info = Q_driver.find_element(
                        By.XPATH,
                        f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/a/p',
                    )
                except Exception:
                    pass
                if info != "":
                    aparment_info.append(  # Adds information into a list
                        [
                            name.text,
                            address.text,
                            cost.text,
                            room.text,
                            number.text,
                            info.text,
                        ]
                    )
                else:
                    aparment_info.append(
                        [name.text, address.text, cost.text, room.text, number.text]
                    )
            except Exception:
                pass
        Q_driver.quit()
        print(aparment_info)
sys.stdout.flush()