
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.firefox.options import Options
from multiprocessing import Process
import time

def check_ip(driver, url="https://api.ipify.org"):
    driver.get(url)
    ip = driver.find_element_by_tag_name("body").text
    print("Current IP:", ip)


def main():
    iteration = 0
    while True:
        
        
        print("[+] Dextools Bot Starting")

        myProxy = "shnuqnvu-rotate:mg5i9hbxda5c@p.webshare.io:80"

        proxy_url = "shnuqnvu-rotate:mg5i9hbxda5c@p.webshare.io:80"  # Replace with your details

        if iteration>= 10:
            print('-----proxy limit complete-----')
            break
        iteration+=1
        firefox_options = Options()
        # firefox_options.add_argument('--headless')  # Run Firefox in headless mode
        firefox_options.add_argument(f'--proxy-server=http://{proxy_url}')

        driver = webdriver.Firefox(options=firefox_options)
        print(f'running{iteration} times with following proxy:',myProxy)
        check_ip(driver)
        
        url = "https://www.dextools.io/app/en/solana/pair-explorer/A6k5YJk3ALuSMrZjLdSz41HRhzMk4v7w8TRCX6LXiKcZ"
        driver.get(url)
        driver.implicitly_wait(30)
        print("[+] Go to Dextools")
    
        sleep(5)

        try:
            driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@sandbox="allow-same-origin allow-scripts allow-popups"]'))
            print('capcha iframe found by xpath')
            sleep(random.randint(3,5))
            try:
                verify=driver.find_element(By.XPATH,'//*[@id="challenge-stage"]/div/label')
                
            except:
                verify=driver.find_element(By.CSS_SELECTOR,'label[class="ctp-checkbox-label"]')
                
            verify.click()
            print('----captcha resolved----')

        except:
            
            print('------No captcha ------')
        
        sleep(10)
        try:
            driver.find_element(By.CLASS_NAME,'card__close').click()
            print('1st close button by class')
        except:
            driver.find_element(By.CSS_SELECTOR,'svg[data-icon="xmark"]').click()
            print('by selector')
        sleep(random.randint(10,15))
        try:
            driver.execute_script("document.querySelector('.close').click();")
            print('2nd close button close')
        except:
            print('noting 2nd found')


        try:
            driver.execute_script("document.querySelector('.favorite-button').querySelector('button').click();")
            print('fav button clicked')
            sleep(2)
        except Exception as e:
            print('no fav button',e)
            
        main_window = driver.current_window_handle
        print('get the main window',main_window)
        sleep(3)

        shareBtn = driver.find_element(By.CSS_SELECTOR,'a[class="shared-button ng-tns-c567420296-2 ng-star-inserted"]')

        shareBtn.click()

        try:
            links_monk = driver.find_element(By.CSS_SELECTOR,'div[class="share-btn"][data-desc="Shared from DEXTools.io"]').find_elements(By.TAG_NAME,'a')
            print('links found')
            for link in links_monk:
                try:
                    print('clicking on the link:',link)
                    link.click()
                    print('clicked')
                    sleep(3)
                    new_window = driver.window_handles[1]
                    print('get the new window')
                    driver.switch_to.window(new_window)
                    print('switched to new window')
                    sleep(3)
                    driver.close()
                    print('new window closes')
                    driver.switch_to.window(main_window)
                    print('back to new window')
                    sleep(2)
                except:
                    print('error in loading the url')
        except:
            print('links not found')


        try:
            driver.find_element(By.CSS_SELECTOR,'button[class="close"]').click()
            print('mondel window closed')
            sleep(3)
        except Exception as e:
            print('error in closing model window')
            pass

        screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
        print('get the screen height',screen_height)
        i = 1
            # scroll one screen height each time
        while True:
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            print(f'scrloing {i} time')
            i += 1
            sleep(3)
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = driver.execute_script("return document.body.scrollHeight;") 
            print(f'setting the now height:',screen_height) 
            # Break the loop when the height we need to scroll to is larger than the total scroll height

            if i>4:
                print('break the loop bcz the scroll window ended...')
                break




        print('complete')
        driver.delete_all_cookies()
        driver.quit()
    

    print('----completed the program----')
    print("-----Change the Proxy Now-----")
        


if __name__=='__main__':
    main()