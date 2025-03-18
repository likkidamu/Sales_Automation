from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Your HubSpot API Key (Private App Key)
API_KEY = 'your_hubspot_api_key'

# HubSpot Contacts API URL
HUBSPOT_API_URL = 'https://api.hubapi.com/contacts/v1/lists/all/contacts/all'

@app.route('/get_contacts', methods=['GET'])
def get_contacts():
    # Make a request to HubSpot's Contacts API
    response = requests.get(HUBSPOT_API_URL, params={'hapikey': API_KEY})

    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()
        # Return the contacts in JSON format
        return jsonify(data), 200
    else:
        # Return an error if something goes wrong
        return jsonify({"error": "Failed to fetch data from HubSpot"}), 500

if __name__ == '__main__':
    app.run(port=5000)
