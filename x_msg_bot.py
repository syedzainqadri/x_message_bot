import mysql.connector
from mysql.connector import Error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import random

# Initialize WebDriver for Chrome
driver = webdriver.Chrome()

# Connect to the MySQL database
def connect_to_database(host_name, user_name, user_password, db_name):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
        return connection
    except Error as err:
        print(f"Error: '{err}'")
        return None

# Fetch usernames from the database
def fetch_usernames(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT id, username FROM x_users WHERE active = 0")
    return cursor.fetchall()

# Update the active status in the database
def update_active_status(connection, user_id):
    cursor = connection.cursor()
    cursor.execute("UPDATE x_users SET active = 1 WHERE id = %s", (user_id,))
    connection.commit()

# Log in to Twitter
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


def read_message_from_file(Msg_file):
    '''reads Message from text file'''
    try:
        with open(Msg_file, 'r', encoding='utf-8') as file:
            return file.read().split('\n')
    except Exception as e:
        print(f"Error reading message file: {e}")
        return "Default message"

def Write_msg_input():
    message = read_message_from_file("Msg.txt")
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[data-testid="dmComposerTextInput"]')))
    msg_input = driver.find_element(By.CSS_SELECTOR,'div[data-testid="dmComposerTextInput"]')
    msg_input.click()
    print('Msg input Found')
    time.sleep(random.randint(2,3))    
    for line in message:
       msg_input.send_keys(line)
       msg_input.send_keys(Keys.SHIFT, Keys.ENTER)
    time.sleep(random.randint(2,4))
    msg_input.send_keys(Keys.ENTER)
    print('Message sent')
    time.sleep(random.randint(3,5))

# Send a message to a user on Twitter
    # ...
def find_DM_button():
   WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div:nth-child(3) > div > div > div > div > div.css-175oi2r.r-1habvwh.r-18u37iz.r-1w6e6rj.r-1wtj0ep > div.css-175oi2r.r-obd0qt.r-18u37iz.r-1w6e6rj.r-1h0z5md.r-dnmrzs > div:nth-child(2) > div')))     
   DM_btn = driver.find_element(By.CSS_SELECTOR,'#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div:nth-child(3) > div > div > div > div > div.css-175oi2r.r-1habvwh.r-18u37iz.r-1w6e6rj.r-1wtj0ep > div.css-175oi2r.r-obd0qt.r-18u37iz.r-1w6e6rj.r-1h0z5md.r-dnmrzs > div:nth-child(2) > div')
   DM_btn.click()
   print('DM Button Found')
   time.sleep(random.randint(10,15))
   
   

# Main function
def main():
    login_username= '_monkeypm'
    login_password = 'monkeypm@123'
    db_connection = connect_to_database('localhost', 'jutt', 'Aw@is@w0rk', 'x_msg')
    
    msg_limit = 3

    if db_connection:
        try:
            login_to_twitter(login_username, login_password)
            
            users = fetch_usernames(db_connection)
            msg_count=0
            for user_id, username in users:
                try:
                    if msg_count>=msg_limit:
                        break
                    time.sleep(random.randint(5,8))
                    print('Loading user:',username)
                    driver.get(f'https://twitter.com/{username}')
                    update_active_status(db_connection,user_id)
                    time.sleep(random.randint(15,25))
                    try:
                        find_DM_button()
                        time.sleep(5)
                        try:
                            Write_msg_input()
                            time.sleep(5)
                        except:
                            print('Msg INput not Found')
                            time.sleep(random.randint(3,5))
                            continue
                    except:
                        print('DM button not Found')
                        continue

                except:
                    print('Error loading user:',username)
                
        except Exception as e :
            print('Error Loging...:',e)
        finally:
            print('finally completed....')
            time.sleep(10)
            db_connection.close()
            driver.quit()

if __name__ == "__main__":
    main()
