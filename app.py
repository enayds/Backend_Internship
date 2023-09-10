from flask import Flask, request, jsonify
import datetime
import pytz
import time

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current time in Nigeria timezone
    timezone = pytz.timezone("Africa/Lagos")
    current_time = datetime.datetime.now(timezone).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Get current day of the week
    current_day = datetime.datetime.now().strftime("%A")



    # Construct GitHub URLs
    github_repo_url = "https://github.com/enayds/Backend_Internship"
    github_file_url = f"{github_repo_url}/blob/master/app.py"


    # Create the response JSON
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
        "current_time": current_time
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


    
