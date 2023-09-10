from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Get current UTC time
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Construct GitHub URLs
    github_repo_url = "https://github.com/username/repo"
    github_file_url = f"{github_repo_url}/blob/main/file_name.ext"

    # Create the response JSON
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
