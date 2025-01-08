from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def login():
    email=driver.find_element(By.NAME,"email")
    email.send_keys("example@gmail.com")
    time.sleep(0.5)
    password=driver.find_element(By.NAME,"password")
    password.send_keys("password")
    time.sleep(0.5)
    login_btn=driver.find_element(By.XPATH,"//div[text()='Log In']")
    login_btn.click()
    driver.implicitly_wait(30)



driver=webdriver.Chrome()
driver.get("https://discord.com/login")
driver.maximize_window()
driver.implicitly_wait(30)

login()


servers_area=driver.find_element(By.XPATH,"//div[contains(@aria-label,'Servers')]")

servers=servers_area.find_elements(By.TAG_NAME,"foreignObject")
print(len(servers))

for i in servers:
    server_name=i.find_element(By.TAG_NAME,"div").get_attribute("aria-label")
    server_name=server_name.split(",")[-1]
    print(server_name) 
    i.click()
    driver.implicitly_wait(30)
    all_channels=driver.find_element(By.ID,"channels")
    channels=all_channels.find_elements(By.TAG_NAME,"a")
    for c in channels:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(c))
        c.click() 
        time.sleep(3)
        driver.implicitly_wait(30)
        channel_name=c.text
        print(channel_name) # channel name
        if not os.path.exists(server_name):
           
           os.makedirs(server_name)
        
        file=open(f"{server_name}/{channel_name}.txt","a",encoding="utf-8")   
        try:
            msgs=driver.find_element(By.XPATH,f"//main[contains(@aria-label,'{c.text}')]")
            user=msgs.find_element(By.XPATH,f"//span[contains(@id,'message-username')]")
            text=msgs.find_elements(By.XPATH,"//div[contains(@id,'message-content')]")
            for t in text:
                file.write(t.text)
                #print(f"{user.text}: {t.text}\n\n")
        except:
            print("\ntry didnt work\n")
            thread_block=driver.find_elements(By.XPATH,"//div[contains(@data-grid-item-id,'forum-grid-view')]") 
            
            for t in thread_block:
                print(t.text)
                
                

      


    time.sleep(3)
    driver.back()
    



time.sleep(10)  


