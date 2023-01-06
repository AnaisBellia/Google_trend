from flask import Flask
from pytrends.request import TrendReq
import matplotlib as plt
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
import time

# if bad gateway, requirements may not be completed

pytrends = TrendReq(hl='en-US', tz=360)
app = Flask(__name__)

@app.route('/sfc', methods=["GET"])
def trend():
    search_terms  = ["banana","apple"]

    # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
    pytrends.build_payload(search_terms , cat=0, timeframe='today 5-y', geo='', gprop='')
# Interest Over Time
    trends = pytrends.interest_over_time()
    if all(trends.isPartial == False):
        del trends['isPartial']
    #return str(trends.iloc[0])
    #return str(trends.iloc[4,0]), str(trends.iloc[4,1])
    #return str(trends)


@app.route('/', methods=["GET"])
def trends():
    kw_list = ["chatGPT", "dall e"]
    timeframe = "2018-01-01 2018-03-01"

    pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='', gprop='')
    df = pytrends.interest_over_time()

# delet is partial column
    if all(df.isPartial == False):
        del df['isPartial']

    fig, ax = plt.subplots()
    df.iloc[:,0].plot.line(ax=ax)
    df.iloc[:,1].plot.line(ax=ax)
    plt.xlabel('Date')
    plt.legend(loc='lower left')

# base 64 pour string in format
    encoded = fig_to_base64(fig)
    my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))
    return my_html

def fig_to_base64(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png',
                bbox_inches='tight')
    img.seek(0)
    return base64.b64encode(img.getvalue())

if __name__=='__main__':
    app.run(debug=True)

