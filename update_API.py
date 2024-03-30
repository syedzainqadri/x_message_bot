from flask import Flask, request, jsonify
from X_posting import login_to_twitter, switch, post_function, comment_button, write_send_msg
import random
import time
app = Flask(__name__)

@app.route('/twitter_action', methods=['POST'])
def perform_twitter_action():
    message = request.form.get('message')
    post_link = request.form.get('post_link') 
    login_username = request.form.get('login_username')
    login_password = request.form.get('login_password')
    post_hit = int(request.form.get('post_hit')) 

    try:
        if(login_to_twitter == 0 )
        # Perform login to Twitter
        login_to_twitter(login_username, login_password)

        while True:
            
            if post_hit==0:
                post_function(post_link)
                comment_button()
                try:
                    write_send_msg(message)
                    print('Comment Sent...')
                except:
                    print("Message not sent")
                finally:
                    time.sleep(random.randint(3, 5))
                    # Update post_hit in the request form
                    request.form['post_hit'] = 1  # Update post_hit in the request form
                    
            else:
                print('random case')
                case = int(random.randint(1, 9))
                switch(case)
                time.sleep(random.randint(3, 5)) # Update post_hit on each iteration
            continue    

        # Optionally, perform other actions here

        return jsonify({'message': 'Actions performed successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
