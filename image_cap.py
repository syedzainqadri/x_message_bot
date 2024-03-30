
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import random
from datetime import datetime
import requests

driver = webdriver.Chrome()

def login_to_twitter(login_username, login_password):
    try:
        driver.get("https://twitter.com/i/flow/login")
        time.sleep(random.randint(15,20))

    # Enter username and submit
        input_element = driver.find_element(By.TAG_NAME, 'input')
        input_element.send_keys(login_username)
        print('Username Entered')
        time.sleep(random.randint(15,20))
        input_element.send_keys(Keys.RETURN)

    # Wait for password field and submit
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'password')))
        password_element = driver.find_element(By.NAME, 'password')
        password_element.send_keys(login_password)
        print('Password Entered')
        time.sleep(random.randint(5,8))
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(5,8))
    except Exception as e:
        print('Login error:',e)

def post_function(post_link):
     driver.get(post_link)
     print('post loading...')
     time.sleep(random.randint(5,10))
     driver.execute_script(f'window.scrollTo(0,300)')
     print('scroll the post')
     time.sleep(random.randint(2,5))
     post_element = driver.execute_script("return document.querySelector('.css-175oi2r')")
     post_element.click()
     print('clicked on the Post')

def post_time():
    time_element = driver.find_element(By.XPATH,"//time[@datetime]")
    print('time found by xpath')
    # Get the text from the time element
    time_text = time_element.text
    return time_text
    

def image_dowload():
    # Find the image element
    time.sleep(random.randint(4,6))
    try:
        image_element = driver.find_element(By.CSS_SELECTOR,"img.css-9pa8cd")
        print('image found by selector')
    except:
        print('not found by selector')
        try:
            image_element = driver.find_element(By.XPATH,"//img[@class='css-9pa8cd']")
            print('found by 1xpath')
        except:
            print('not found by 1xpath')
            try:
                image_element = driver.find_element(By.XPATH,"//img[@alt='Image']")
                print('found by 2xpath')
            except:
                print('Not found by 2xpath')
                try:
                    image_element = driver.find_element(By.XPATH,"//img[contains(@src, 'GJxrAi5WsAASyeu')]")
                    print('found by 3xpath')
                except:
                    print('not found by 3xpath')
                    try:
                       image_element = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div')
                       print('found by manual xpath')
                    except:
                        print('not found by manual xpath')
                        try:
                           image_element = driver.find_element(By.CSS_SELECTOR,'#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-17gur6a.r-1pi2tsx.r-13qz1uu > div > div.css-175oi2r.r-16y2uox.r-1wbh5a2 > div.css-175oi2r.r-1pi2tsx.r-11yh6sk.r-buy8e9.r-13qz1uu > div.css-175oi2r.r-13awgt0.r-184en5c > div > div > div > div > div')
                           print('found by manual selector') 
                        except:
                            print('Not found by manual selector')
    print('image element found')
    time.sleep(random.randint(1,3))
    # Find the time element
    time_element = driver.find_element(By.XPATH,"//time[@datetime]")
    # Get the URL of the image
    image_url = image_element.get_attribute("src")
    # Use requests to download the image
    response = requests.get(image_url)
    time.sleep(3)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Format the time text to remove characters not allowed in filenames
        datetime_value = datetime.strptime(time_element.get_attribute("datetime"), "%Y-%m-%dT%H:%M:%S.%fZ")
        # Format the time as desired for the filename
        formatted_time = datetime_value.strftime("%Y-%m-%d_%H-%M-%S")
        # Save the image with the time of the post as filename
        filename = f"{formatted_time}.jpg"
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Image downloaded successfully as '{filename}'!")
    else:
        print("Failed to download the image.")
    return image_url

def caption_get():
    tweet_text_element = driver.find_element(By.XPATH,"//div[contains(@class, 'css-175oi2r') and contains(@class, 'r-1s2bzr4')]")
    print('cap found by xpath ')
    time.sleep(random.randint(3,5))
    # Get the text from the div element
    tweet_text = tweet_text_element.text
    print(type(tweet_text))
    return tweet_text
    

def main():

    login_username = '_monkeypm'
    login_password = 'monkeypm@123'
    post_link = "https://x.com/Degen_Corleone/status/1773048050346246375?s=20"


    login_to_twitter(login_username,login_password)
    post_function(post_link)
    time.sleep(random.randint(10,15))
    print(post_time())
    try:           
        cap = caption_get()
        print(cap)
        try:
            url = image_dowload()
            print(url)
        except:
            print("image not Found  by url")
        
    except:
        print('download fail')
    finally:
        print('Ending')
        time.sleep(15)
        driver.quit()


main()