from flask import Flask, request, jsonify
from XPosting import login_to_twitter, scrolling_func, post_function, comment_button, write_send_msg, log_out

app = Flask(__name__)

@app.route('/twitter_action', methods=['POST'])
def perform_twitter_action():
    message = request.form.get('message')
    post_link = request.form.get('post_link')
    login_username = request.form.get('login_username')
    login_password = request.form.get('login_password')

    try:
        # Perform login to Twitter
        login_to_twitter(login_username, login_password)
        
        # Scroll through the Twitter feed
        scrolling_func()
        
        # Perform actions on the post
        post_function(post_link)
        
        # Perform a comment action
        comment_button()
        
        # Write and send a message
        write_send_msg(message)
        
        # Logout from Twitter
        log_out()

        return jsonify({'message': 'Actions performed successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
