from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from User_agent import agent
from selenium.webdriver.chrome.service import Service
import sys
import math

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless=new") # for Chrome >= 109
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
chrome_options.add_argument("--disable-dev-shm-usage")

chrome_options.add_argument(f"user-agent={agent}")
chrome_options.add_argument("--no-sandbox")
s=Service('/Users/jamarionhines/Downloads/chromedriver-mac-arm64/chromedriver')
pages_driver = webdriver.Chrome(service=s,options=chrome_options)

pages = 0
intro_url =sys.argv[1]


if "house" in intro_url:
    print("Invaild Link")
    exit()
elif "condos" in intro_url:
    print("Invaild Link")
    exit()
elif "townhomes" in intro_url:
    print("Invaild Link")
    exit()
 
#print(intro_url)
pages_driver.get(intro_url)


try:
    # Attempt to find the number of pages
    pages_text = pages_driver.find_element(By.CLASS_NAME, 'pageRange').text
    pages = int(pages_text.split(' ')[-1])
    pages_driver.quit()  

    # Adjust the number of pages
    if pages > 10:
        pages = math.floor(pages / 2) if pages % 2 else int(pages / 2)

except Exception:
    pass
info=""
aparment_info=[]


if intro_url.find("?")==-1:
    for web in range(1,pages+1):
        url = f'{intro_url}{web}'
        noQ_driver= webdriver.Chrome(service=s,options=chrome_options)

        noQ_driver.get(url)


        base_cards= noQ_driver.find_elements(By.XPATH,'//*[@id="placardContainer"]/ul/li')
        print(base_cards)
        for i in range(1,len(base_cards)):
            try:
                name=noQ_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/header/div[1]/a/div[1]/span')
                address=noQ_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/header/div[1]/a/div[2]')
                cost=noQ_driver.find_element(By.CSS_SELECTOR,f'#placardContainer > ul > li:nth-child({i}) > article > section > div > div.property-info > div > div.top-level-info > a > p.property-pricing')
                room=noQ_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[1]/a/p[2]')
                try:
                    number=noQ_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[2]/a/span')
                except:
                    number=noQ_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[3]/a/span')
                try:
                    info=noQ_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/a/p')
                except Exception:
                    pass
                if info !="":
                    aparment_info.append([name.text,address.text,cost.text,room.text,number.text,info.text])
                else:
                    aparment_info.append([name.text,address.text,cost.text,room.text,number.text])
            except Exception:
                pass
        noQ_driver.quit()        

elif intro_url.find("?")!=-1:
    split_url=intro_url.split("?")
    for web in range(1,pages+1):
        url = f'{split_url[0]}/{web}/?{split_url[1]}'
    
        Q_driver= webdriver.Chrome(service=s,options=chrome_options)
        Q_driver.get(url)



        base_cards= Q_driver.find_elements(By.XPATH,'//*[@id="placardContainer"]/ul/li')
        for i in range(1,len(base_cards)):
            try:
                name=Q_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/header/div[1]/a/div[1]/span')
                address=Q_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/header/div[1]/a/div[2]')
                cost=Q_driver.find_element(By.CSS_SELECTOR,f'#placardContainer > ul > li:nth-child({i}) > article > section > div > div.property-info > div > div.top-level-info > a > p.property-pricing')
                room=Q_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[1]/a/p[2]')
                try:
                    number=Q_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[2]/a/span')
                except:
                    number=Q_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/div[3]/a/span')
                try:
                    info=Q_driver.find_element(By.XPATH,f'//*[@id="placardContainer"]/ul/li[{i}]/article/section/div/div[2]/div/a/p')
                except Exception:
                    pass
                if info !="":
                    aparment_info.append([name.text,address.text,cost.text,room.text,number.text,info.text])
                else:
                    aparment_info.append([name.text,address.text,cost.text,room.text,number.text])
            except Exception:
                pass
        Q_driver.quit()
sys.stdout.flush()