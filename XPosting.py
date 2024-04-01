from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import random
import requests
import json

driver = webdriver.Chrome()

def get_postman_data(api_key):
    headers = {
        'X-Api-Key': api_key,
        'Content-Type': 'application/json'
    }

    # Replace 'YOUR_COLLECTION_ID' with the actual collection ID you want to retrieve
    collection_id = '33908320-35644a5b-1ed3-455a-af10-2fffefd24b33'
    url = f'https://api.postman.com/collections/33908320-c42cb38c-fcd7-4601-ba8e-a735d538b52b?access_key=PMAT-01HTDPNRS2X70QE1V4QXBXYWYM'
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an exception for 4xx or 5xx status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_data_list():
  postman_api_key = 'PMAK-660b181737c5cd0001fe771b-5432c38bc681d2e8cb8d34dcfe635bdead'
  postman_data = get_postman_data(postman_api_key)
  if postman_data:
      print("Data retrieved successfully:")
      extracted_data = []
      collection_info = postman_data['collection']
      items = collection_info['item']
      for item in items:
          request = item.get('request', {})
          body = request.get('body', {})
          form_data = body.get('formdata', [])
          data_dict = {}
          for entry in form_data:
              data_dict[entry['key']] = entry['value']
          extracted_data.append(data_dict)
          return extracted_data[0]

def login_to_twitter(login_username, login_password):
    try:
        driver.get("https://twitter.com/i/flow/login")
        driver.maximize_window()
        time.sleep(random.randint(15,30))

    # Enter username and submit
        input_element = driver.find_element(By.TAG_NAME, 'input')
        input_element.send_keys(login_username)
        print('Username Entered')
        time.sleep(random.randint(15,30))
        input_element.send_keys(Keys.RETURN)

    # Wait for password field and submit
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'password')))
        password_element = driver.find_element(By.NAME, 'password')
        time.sleep(3)
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
     driver.execute_script(f'window.scrollTo(0,250)')
     print('scroll the post')
     time.sleep(random.randint(2,5))
     
      
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

def like_button():
    time.sleep(random.randint(5,12))
    print('find like button')
    try:
        like_button= driver.find_element(By.CSS_SELECTOR,'[data-testid="like"]')
        print('like button found by special selector')
        time.sleep(random.randint(2,5))
        like_button.click()
        print('Like button clicked by special selector')
    except:
       print('Already Liked')

def repost_button():
    time.sleep(random.randint(5,8))
    try:
        repost_button = driver.find_element(By.XPATH,"//div[@data-testid='retweet']")
        repost_button.click()     
        time.sleep(random.randint(3,5))
        fi_click = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div')
        print('found by xpath')
        fi_click.click()
        print('Final repost button clicked ')
        time.sleep(random.randint(3,12))
    except:
        print('ALready Reposted')
    
    finally:
        print('repost  Done')
        time.sleep(random.randint(4,6))

def comment_button():
    time.sleep(random.randint(3,6))
    try:

        element = driver.find_element(By.XPATH,'//*[@id="id__6w9o1amibzy"]/div[1]/div')
        print('found by xpath')
    except:
        print('failed by xpath')
        try:
            element = driver.find_element(By.CSS_SELECTOR,'#id__6w9o1amibzy > div:nth-child(1) > div')
            print('found by selector')
        except:
            print('failed by selector')
            try:
                element = driver.find_element(By.CSS_SELECTOR,'div[data-testid="reply"]')
                print('found by special selector')
            except:
                print('failed by special selector')

               
    element.click()
    print('Commment Button clicked by manual Xpath')
    time.sleep(random.randint(3,5))


def main():
    
    login_username = '_monkeypm'
    login_password = 'monkeypm@123'
    new_data = {}

    done_links = []
    done_messages = []

    try:
        login_to_twitter(login_username, login_password)
        
        while True:
            data = get_data_list()
            msg = data['message']
            link = data['post_link']
            if link not in done_links:
                print('link is not available so we raid on:', link)               
                scrolling_func()
                post_function(link)
                like_button()
                comment_button()
                try:
                    write_send_msg(msg)
                    print('Comment Sent...')
                except:
                    print("Message not sent")
                finally:
                    time.sleep(random.randint(3, 5))
                    done_links.append(link)
                    done_messages.append(msg)
                    new_data[link] = msg  # Add the new link and message to the dictionary
                    print('link and msg updated and job is done')
                    with open('new_data.json', 'a') as json_file:
                        json.dump(new_data, json_file, indent=4)
                    print("New data saved to 'new_data.json'")
            else:
                print('link not found so we do RANDOM JOB')
                case = int(random.randint(1,9))
                switch(case)
                
    except:
       print('login failed')



       
if __name__ == '__main__':
    
    main() 
       
