#!/usr/bin/env python3
import eventlet
import faulthandler

print('Monkey Patching Eventlet')
eventlet.monkey_patch()
print('Enable faulthandler')
faulthandler.enable()

from flask import Flask, render_template, jsonify, request
from google.ads.googleads.client import GoogleAdsClient

CUSTOMER_ID = ''
LOGIN_CUSTOMER_ID = ''  # if using a client account under a manager account, the manager account id goes here
DEVELOPER_TOKEN = ''
CLIENT_ID = ''
CLIENT_SECRET = ''
REFRESH_TOKEN = ''

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/test')
def test():
    credentials = {
        'developer_token': DEVELOPER_TOKEN,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN,
        'use_proto_plus': True,
    }
    if LOGIN_CUSTOMER_ID:
        credentials['login_customer_id'] = LOGIN_CUSTOMER_ID

    client = GoogleAdsClient.load_from_dict(credentials)

    query = """
            SELECT metrics.cost_micros
            FROM age_range_view
            WHERE segments.date DURING LAST_30_DAYS
            """

    google_ads_service = client.get_service('GoogleAdsService')
    result = google_ads_service.search_stream(customer_id=CUSTOMER_ID, query=query)
    for batch in result:
        for row in batch.results:
            pass
    i = request.args.get('i')
    print(f'request {i} OK')

    return jsonify({})


if __name__ == '__main__':
    app.run(debug=True)
