from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import random
import requests
import json

# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# driver = webdriver.Chrome()



def login_with_token(driver, auth_token):
    driver.get("https://twitter.com")
    print('Without cookie')

    # Add your auth_token to the browser cookies
    driver.add_cookie({'name': 'auth_token', 'value': auth_token, 'path': '/', 'domain': '.twitter.com'})
    print('Adding cookie')

    driver.get("https://twitter.com")  # Navigate again to load the page with the auth token
    print('Success')

def login_to_twitter(driver,login_username, login_password):
    try:
        driver.get("https://twitter.com/i/flow/login")
        driver.implicitly_wait(15)
        driver.maximize_window()
        time.sleep(random.randint(5,10))
    # Enter username and submit
        input_element = driver.find_element(By.TAG_NAME, 'input')
        input_element.send_keys(login_username)
        print('Username Entered')
        time.sleep(random.randint(2,3))
        input_element.send_keys(Keys.RETURN)
    # Wait for password field and submit
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'password')))
        password_element = driver.find_element(By.NAME, 'password')
        # time.sleep(3)
        password_element.send_keys(login_password)
        print('Password Entered')
        time.sleep(random.randint(2,5))
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(1,3))
    except Exception as e:
        print('Login error:',e)

def get_posts_by_bot(bot_id):
    url = f"http://localhost:3000/posts/by-bot/{bot_id}"
    headers = {}
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse response as JSON
        data = response.json()
        # Print the JSON response
        return data
    else:
        # If the request was not successful, print the status code and error message
        print(f"Error: {response.status_code} - {response.text}")
        return None


def scrolling_func(driver):

        driver.implicitly_wait(10)
        # time.sleep(random.randint(1,5))
        height = driver.execute_script('return document.body.scrollHeight')
        print(height)
        i = 0
        scroll_limit= random.randint(3,5)
        while True:
            driver.execute_script(f'window.scrollTo(0,document.body.scrollHeight)')
            print(f'{i}.scrolling.....')
            i+=1
            time.sleep(random.randint(2,5))
            if i==scroll_limit:
                 print('Scroll Limit Completed..')
                 break
        print('Out of Scroll Loop')
        # time.sleep(random.randint(10,15))

def log_out(driver):
     print('logging Out')
     driver.get('https://twitter.com/logout')     
     time.sleep(random.randint(1,3))
     logout_button = driver.find_element(By.CSS_SELECTOR, "#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-1kihuf0.r-xr3zp9.r-1awozwy.r-1pjcn9w.r-9dcw1g > div.css-175oi2r.r-kemksi.r-pm9dpa.r-1rnoaur.r-1867qdf.r-z6ln5t.r-494qqr.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-eqz5dr.r-1hc659g.r-1n2ue9f.r-11c0sde.r-13qz1uu > div:nth-child(1) > div")
     print('Logout button found By selector')
     logout_button.click()
     print('loged out...')

def post_function(driver,post_link):
     driver.get(post_link)
     print('post loading...')
     time.sleep(random.randint(1,3))
     driver.execute_script(f'window.scrollTo(0,300)')
     print('scroll the post')
    #  time.sleep(random.randint(2,5))
      
def write_send_msg(driver,message):
    time.sleep(2)
    msg_input = driver.execute_script("return document.activeElement;")
    msg_input.click()
    print('Message input found by active cursor')
    time.sleep(random.randint(1,3))
    msg_input.send_keys(message)
    print('Message Entered')
    time.sleep(random.randint(1,3))
    reply = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div')
    reply.click()
    try:
        driver.find_element(By.XPATH,'//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div').click()
    except:
        print('clear')
    print('reply button clicked by xpath')
    # time.sleep(random.randint(8,12))
  
def switch(driver,case_numb):
#  global executed_cases
 case=int(case_numb)
 if case==1:
  print('task 1')
  driver.get('https://twitter.com/ElonMuskAOC')
#   time.sleep(5)
  scrolling_func(driver)
 elif case==2:
  print('task 2')
  driver.get('https://twitter.com/elonmuskusaaaaa')
#   time.sleep(5)
  scrolling_func(driver)
 elif case==3:
  print('task 3')
  driver.get('https://twitter.com/dogeofficialceo')
#   time.sleep(5)
  scrolling_func(driver)
 elif case==4:
  print('task 4')
  driver.get('https://twitter.com/leeneedham81')
#   time.sleep(5)
  scrolling_func(driver)
 elif case==5:
  print('task 5')
  driver.get('https://twitter.com/CW_Insider')
#   time.sleep(5)
  scrolling_func(driver)
 elif case==6:
  print('task 6')
  driver.get('https://twitter.com/elonmusk')
#   time.sleep(5)
  scrolling_func(driver)
 elif case==7:
  print('task 7')  
  driver.get('https://twitter.com/cb_doge')
#   time.sleep(5)
  scrolling_func(driver)
 elif case==8:
  print('task 8')
  driver.get('https://twitter.com/X_BEBEeth')
#   time.sleep(5)
  scrolling_func(driver)
 elif case==9:
  print('task 9')
  driver.get('https://twitter.com/Bybit_Official')
#   time.sleep(5)
  scrolling_func(driver)
 else:
  print('numb out of limit')

def like_button(driver):
    # time.sleep(random.randint(5,6))
    print('finding like button')    
    try:
        like_button= driver.find_element(By.xpath,'//*[@data-testid="like"][1]')
    except:
        try:
            like_button= driver.find_element(By.xpath,'//div[@data-testid="like" and @role="button"][1]')
        except:
            try:
                like_button= driver.find_element(By.xpath,'//div[@id="id__nuyabbf1zgb"]/div[@data-testid="like"][1]')
            except:
                like_button = driver.find_elements(By.CSS_SELECTOR,'div[data-testid="like"]')[1]
    print('like button found by special selector')
    time.sleep(random.randint(1,3))
    like_button.click()
    try:
        driver.find_element(By.XPATH,"//*[@data-testid='app-bar-close']").click()
    except:
        print('clear home page')

    print('Like button clicked by special selector')
    

def repost_button(driver):
    # time.sleep(random.randint(5,8))
    try:
        repost_button = driver.find_elements(By.CSS_SELECTOR,'div[data-testid="retweet"]')[1]
        repost_button.click()     
        time.sleep(random.randint(1,2))
        try:
            driver.find_element(By.CSS_SELECTOR,'div[data-testid="app-bar-close"]').click()
        except:
            print('repost clear')
        fi_click = driver.find_element(By.CSS_SELECTOR,'div[data-testid="retweetConfirm"]')
        print('found by xpath')
        fi_click.click()
        time.sleep(random.randint(1,3))
        try:
            driver.find_element(By.CSS_SELECTOR,'div[data-testid="app-bar-close"]').click()
        except:
            print('repost clear')

        print('Final repost button clicked ')
    except:
        print('ALready Reposted')
        # time.sleep(random.randint(4,6))
    finally:
        print('repost  Done')

def comment_button(driver):
    # time.sleep(random.randint(3,6))
    try:

        element = driver.find_elements(By.CSS_SELECTOR,'div[data-testid="reply"]')[1]
        print('found by special selector')
    except:
        print('failed by special selector')
       
        element = driver.find_element(By.CSS_SELECTOR,'#id__6w9o1amibzy > div:nth-child(1) > div')
        print('found by selector')
       
    
    element.click()
    print('Commment Button clicked by manual Xpath')
    # time.sleep(random.randint(3,5))

def read_env_file(file_path):
    variables = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Ignore lines that are empty or start with a comment character
            if not line.strip() or line.strip().startswith('#'):
                continue
            key, value = line.strip().split('=', 1)  # Split key and value by the first '=' character
            variables[key.strip()] = value.strip()
    return variables


def read_credentials(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def main():


    # Retrieve username and password from env variables
    
    credentials_list = read_credentials('updateData.json')
    
    i = 0

    for credentials in credentials_list:

        

        driver = webdriver.Chrome()  # Initialize the driver for each user
        msg = credentials['content']
        username = credentials['user']
        password = credentials['pass']
        auth_token = credentials['auth']
        link = 'https://twitter.com/SkyPegasusIO/status/1777441096726913134?t=FYYQdW2ZwJTBqAPkVN_NmA&s=19'

        i+=1
        try:
            try:
                login_with_token(driver,auth_token)
                driver.implicitly_wait(10)
                driver.execute_script(f'window.scrollTo(0,300)')
                print('scroll the post')
                driver.find_element(By.CSS_SELECTOR,'div[data-testid="retweet"]')
                print('repost button found by special selector')
                driver.maximize_window()
                print('login by token',i) #loging twitter with the given username and password
                time.sleep(random.randint(1,4))
            except:
                login_to_twitter(driver,username,password)
                print('login by user:password',i)
                driver.execute_script(f'window.scrollTo(0,300)')
                print('scroll the post')
            
            try:
                driver.find_element(By.XPATH,"//*[@data-testid='app-bar-close']").click()
            except:
                print('clear home page')

            try:
                driver.find_element(By.CSS_SELECTOR,'div[class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-1mnahxq r-19yznuf r-64el8z r-1dye5f7 r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"]').click()
            except:
                print('clear')
            time.sleep(2)  
            # after login and scrolling the home page innitializing the infinite loop 
            scrolling_func(driver)
            try:
                post_function(driver,link)
                time.sleep(2)
                # driver.execute_script(f'window.scrollTo(0,300)')
            except Exception as e:
                print('error:',e)
                driver.quit()
                continue
            if i>7:
                try:
                    like_button(driver)
                except:
                    print('already liked or some error')
                repost_button(driver)
            comment_button(driver)
            try:
                write_send_msg(driver,msg)
                print('comment send')
                time.sleep(2)
            except:
                print('comment sending error')
            
            # time.sleep(random.randint(1,4)) 
            # print('doning random job ')  
            # case_numb = random.randint(1,9)          
            # switch(driver,case_numb)
            # print('loging out')
            # log_out(driver)
            print('Done',i)
            driver.quit()
             

                
        except Exception as e:
            print('login failed:',e)



       
if __name__ == '__main__':
    
    main() 
       