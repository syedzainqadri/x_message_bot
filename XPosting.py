# import mysql.connector
# from mysql.connector import Error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import random
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


def scrolling_func():

        time.sleep(15)
        height = driver.execute_script('return document.body.scrollHeight')
        print(height)
        i = 0
        scroll_limit= random.randint(3,5)
        while True:
            driver.execute_script(f'window.scrollTo(0,document.body.scrollHeight)')
            print(f'{i}.scrolling.....')
            i+=1
            time.sleep(random.randint(10,15))
            if i==scroll_limit:
                 print('Scroll Limit Completed..')
                 break
        print('Out of Scroll Loop')
        time.sleep(random.randint(10,15))

def log_out():
     print('logging Out')
     driver.get('https://twitter.com/logout')     
     time.sleep(random.randint(8,12))
     logout_button = driver.find_element(By.CSS_SELECTOR, "#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-1kihuf0.r-xr3zp9.r-1awozwy.r-1pjcn9w.r-9dcw1g > div.css-175oi2r.r-kemksi.r-pm9dpa.r-1rnoaur.r-1867qdf.r-z6ln5t.r-494qqr.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-eqz5dr.r-1hc659g.r-1n2ue9f.r-11c0sde.r-13qz1uu > div:nth-child(1) > div")
     print('Logout button found By selector')
     logout_button.click()
     print('loged out...')

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
     like_button()
     repost_button()
     

def like_button():
     time.sleep(random.randint(5,12))
     like_button =  driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div[3]/div')
     print('Like pharr liya')
     time.sleep(random.randint(5,8))
     like_button.click()
     print('Like button clicked by manual 2xpath')


def repost_button():
    time.sleep(random.randint(5,8))
    repost_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div')
    repost_button.click()
    print('Repost button clicked By Xpath')
    time.sleep(random.randint(3,5))
    fi_click = driver.find_element(By.XPATH,'//*[@id="layers"]/div[3]/div/div/div/div[2]/div/div[3]/div/div/div/div')
    fi_click.click()
    print('Final repost button clicked by xpath')
    time.sleep(random.randint(3,12))
    print('repost  Done')
    time.sleep(random.randint(4,6))
   


def comment_button():
     time.sleep(random.randint(3,6))
     element = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div')
     element.click()
     print('Commment Button clicked by manual Xpath')
     time.sleep(random.randint(3,5))
    
         
def write_send_msg(message):
    msg_input = driver.execute_script("return document.activeElement;")
    msg_input.click()
    print('Message input found by active cursor')
    time.sleep(random.randint(8,12))
    msg_input.send_keys(message)
    print('Message Entered')
    time.sleep(random.randint(5,8))
    reply = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div')
    reply.click()
    print('reply button clicked by xpath')
    time.sleep(random.randint(8,12))
  
def switch(case_numb):
#  global executed_cases
 case=int(case_numb)
 if case==1:
  print('task 1')
  driver.get('https://twitter.com/ElonMuskAOC')
  time.sleep(5)
  scrolling_func()
 elif case==2:
  print('task 2')
  driver.get('https://twitter.com/elonmuskusaaaaa')
  time.sleep(5)
  scrolling_func()
 elif case==3:
  print('task 3')
  driver.get('https://twitter.com/dogeofficialceo')
  time.sleep(5)
  scrolling_func()
 elif case==4:
  print('task 4')
  driver.get('https://twitter.com/leeneedham81')
  time.sleep(5)
  scrolling_func()
 elif case==5:
  print('task 5')
  driver.get('https://twitter.com/CW_Insider')
  time.sleep(5)
  scrolling_func()
 elif case==6:
  print('task 6')
  driver.get('https://twitter.com/elonmusk')
  time.sleep(5)
  scrolling_func()
 elif case==7:
  print('task 7')  
  driver.get('https://twitter.com/cb_doge')
  time.sleep(5)
  scrolling_func()
 elif case==8:
  print('task 8')
  driver.get('https://twitter.com/X_BEBEeth')
  time.sleep(5)
  scrolling_func()
 elif case==9:
  print('task 9')
  driver.get('https://twitter.com/Bybit_Official')
  time.sleep(5)
  scrolling_func()
 else:
  print('numb out of limit')
#  executed_cases.add(case)

# executed_cases = set()
def main():
    
    message = 'Discover monkey inside You\n Mface from MonkeysLIST is here Already\n #MLIST\n #MonkeysLIST '
    post_link = "https://x.com/Degen_Corleone/status/1773048050346246375?s=20"
    login_username = '_monkeypm'
    login_password = 'monkeypm@123'
    post_hit = 0


    try:
        login_to_twitter(login_username, login_password)

        while True:
            
               
            if post_hit == 1:  # Ensure to compare with string "False"
                post_function(post_link)
                comment_button()
                try:
                    write_send_msg(message)
                    print('Comment Sent...')
                except:
                    print("Message not sent")
                finally:
                    post_hit = 0
                    time.sleep(random.randint(3, 5))
                    # Update post_hit in the request form
                    continue
            else:
                print('random case')
                case=int(random.randint(1,9))
                switch(case)
                continue
    except:
       print('login failed')
if __name__ == '__main__':
    
    main() 