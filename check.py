import pandas as pd
import mysql.connector
from mysql.connector import Error

def read_csv(file_path):
    """Reads an Excel file and returns a DataFrame with added ID and boolean columns."""
    df = pd.read_csv(file_path)

    # Assuming the first column contains usernames
    first_column = df.columns[0].replace('@','')

    # Add an ID column
    df['ID'] = range(1, len(df) + 1)

    # Add a boolean column 'Active' with default value False
    df['Active'] = False

    return df[first_column],  df['Active']

def connect_to_database(host_name, user_name, user_password, db_name):
    """Establishes a connection to the MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    
    return connection

def insert_user_data(connection, usernames, actives):
    """Inserts user data into the MySQL database."""
    cursor = connection.cursor()
    query = "INSERT INTO customers (username, active) VALUES (%s, %s);"
    try:
        for username, active in zip(usernames, actives):
            cursor.execute(query, (username, active))
        connection.commit()
        print("User data inserted successfully")
    except Error as err:
        print(f"Error: '{err}'")

def main():
    # Path to your Excel file
    file_path = 'twitter_usernames.csv'

    # Database connection parameters
    host_name = 'localhost'
    user_name = 'jutt'
    user_password = 'Aw@is@w0rk'
    db_name = 'x_msg'


    # Read user data from the Excel file
    usernames, actives = read_csv(file_path)

    # Connect to the MySQL database
    connection = connect_to_database(host_name, user_name, user_password, db_name)

    # Insert user data into the database
    if connection is not None:
        insert_user_data(connection, usernames, actives)
        connection.close()
    else:
        print("Failed to connect to the database")

if __name__ == "__main__":
    main()
