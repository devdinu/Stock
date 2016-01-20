from nsetools import Nse
from flask import Flask, jsonify, request, url_for
from utils import *

available_info = ["highPrice", "lastCorpAnnouncement", "lastCorpAnnouncementDate", "lowPrice", "ltp", "netPrice", "openPrice", "previousPrice", "series", "symbol", "tradedQuantity", "turnoverInLakhs"]

app = Flask(__name__)
nse = Nse()

def html(output):
    jsfiles = ["basic.js"]
    return main_html(output, jsfiles=map(lambda f:url_for('static', filename=f), jsfiles))

def requrested_json():
    json = request.args.get('json')
    return json and json.lower() in ('true', 't')


@app.route('/losers')
def get_losers():
    losers = nse.get_top_losers()
    if requrested_json():
        return jsonify({"losers":losers})
    return html("Top Losers\n" + ordered_list([loser['symbol'] for loser in losers]))


@app.route('/gainers')
def get_gainers():
    gainers = nse.get_top_gainers()
    if requrested_json():
        return jsonify({"gainers":gainers})
    return html("Top Gainers\n"+ ordered_list([gainer['symbol'] for gainer in gainers]))

@app.route('/ping')
def ping():
    return "pong"

@app.route('/information')
def information_of_stocks():
    return html(dropdowns(available_info))

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
