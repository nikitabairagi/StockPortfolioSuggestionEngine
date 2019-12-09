from flask import Flask, render_template, request
from alpha_vantage.timeseries import TimeSeries
from flask_bootstrap import Bootstrap
import time
import os
import requests
import math

# If `data_itempoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__, static_url_path='/static')
Bootstrap(app)

# accept both GET and POST
@app.route('/', methods=['GET', 'POST']) 

def suggestion_engine():
    # display form for user to input investment amount and select strategy
    if request.method == 'GET':
        return render_template('Homepage.html')

    # analyze data    
    elif request.method == 'POST':

        def data_processing(selected_strategy, total_capital, ticker_list):
            # divide invetsment amount to each ticker symbol
            invest_on_each_ticker = total_capital / 3
            history = []
            ticker_info = []

            # buffer for temp data
            day0 = []

            # for storing investment amount in each day 
            day1_fund = 0
            day2_fund = 0
            day3_fund = 0
            day4_fund = 0
            day5_fund = 0

            # for storing historical data
            day1_hist = []
            day2_hist = []
            day3_hist = []
            day4_hist = []
            day5_hist = []

            # extract ticker information for each ticker in each strategy
            for ticker_sym in ticker_list:

                time_series = TimeSeries(key='OjZkMTJlM2YyZjgxMjU5MWUwNzUxNTMwNGVkN2Q5N2Uy')

                # get daily data
                data, rawData = time_series.get_daily_adjusted(ticker_sym)

                if rawData:
                    day = 0
                    # extract data from day 1 to day 5 and push data to an array
                    for item in data:
                        if day <= 4:
                            ticker_info.append(
                                [selected_strategy, ticker_sym, item, data[item]['5. adjusted close']])
                            history.append(item)
                            day = day + 1
                        else:
                            break

            invest_data = []
            historical_data = []

            # analyze ticker data and store analyzed data for day 1
            for data_item in ticker_info:
                if data_item[2] == sorted(set(history))[0]:
                    # calculate number of stock
                    no_of_ticker = math.floor(invest_on_each_ticker / float(data_item[3]))

                    # push data
                    day0.append([data_item[1], data_item[3]])                 
                    day1_hist.append([data_item[1], round(float(data_item[3]), 2), no_of_ticker])
                    day1_fund += no_of_ticker * float(data_item[3])

            invest_data.append([sorted(set(history))[0], round(day1_fund, 2)])

            for data_item in ticker_info:
                
                # analyze ticker data and store analyzed data for day 2
                if data_item[2] == sorted(set(history))[1]:
                    for each_ticker in day1_hist:
                        if each_ticker[0] == data_item[1]:
                            # push data
                            day2_hist.append([data_item[1], round(float(data_item[3]), 2), each_ticker[2]])
                            day2_fund += (float(data_item[3]) * each_ticker[2])

                # analyze ticker data and store analyzed data for day 3
                elif data_item[2] == sorted(set(history))[2]:
                    for each_ticker in day1_hist:
                        if each_ticker[0] == data_item[1]:
                            # push data
                            day3_hist.append([data_item[1], round(float(data_item[3]), 2), each_ticker[2]])
                            day3_fund += (float(data_item[3]) * each_ticker[2])

                # analyze ticker data and store analyzed data for day 4
                elif data_item[2] == sorted(set(history))[3]:
                    for each_ticker in day1_hist:
                        if each_ticker[0] == data_item[1]:
                            # push data
                            day4_hist.append([data_item[1], round(float(data_item[3]), 2), each_ticker[2]])
                            day4_fund += (float(data_item[3]) * each_ticker[2])

                # analyze ticker data and store analyzed data for day 5
                elif data_item[2] == sorted(set(history))[4]:
                    for each_ticker in day1_hist:
                        if each_ticker[0] == data_item[1]:
                            # push data
                            day5_hist.append([data_item[1], round(float(data_item[3]), 2), each_ticker[2]])
                            day5_fund += (float(data_item[3]) * each_ticker[2])

            # push all other historical data in 5 days into an array
            historical_data.append([sorted(set(history))[0], day1_hist])
            historical_data.append([sorted(set(history))[1], day2_hist])
            historical_data.append([sorted(set(history))[2], day3_hist])
            historical_data.append([sorted(set(history))[3], day4_hist])
            historical_data.append([sorted(set(history))[4], day5_hist])

            # push all investment data in 5 days into an array
            invest_data.append([sorted(set(history))[1], round(day2_fund, 2)])
            invest_data.append([sorted(set(history))[2], round(day3_fund, 2)])
            invest_data.append([sorted(set(history))[3], round(day4_fund, 2)])
            invest_data.append([sorted(set(history))[4], round(day5_fund, 2)])          

            # end of data processing
            return invest_data, historical_data

        # get investment amount and strategy from the form
        investment_value = request.form['investment_value']
        investment_strategies = request.form.getlist('strategy')
        # divide investment to each strategy
        total_capital = int(investment_value) / len(investment_strategies)
        
        # define ticker symbol list for each strategy, index tickers are mapped to Vanguard Total Stock Market ETF (VTI)
        ethical_ticker_list = ['AAPL', 'INTC', 'ADBE']
        growth_ticker_list = ['JPM', 'GOOGL', 'PG']
        index_ticker_list = ['AMZN','FB','MSFT']
        quality_ticker_list = ['T', 'INTC', 'KO']
        value_ticker_list = ['C', 'TSLA', 'WMT']

        try:

            # store analyzed investment data
            analyzed_invest_results = []

            # store analyzed historical data
            analyzed_hist_results = []

            for stra in investment_strategies:
                # ethical investment processing
                if stra == 'Ethical Investing':
                    invest_data, historical_data = data_processing('Ethical Investing', total_capital, ethical_ticker_list)
                    analyzed_invest_results.append(['Ethical Investing', invest_data])
                    analyzed_hist_results.append(['Ethical Investing', historical_data])

                # growth investment processing
                elif stra == 'Growth Investing':

                    # Wait for 1 minute before making the API Call
                    time.sleep(60)
                    invest_data, historical_data = data_processing('Growth Investing', total_capital, growth_ticker_list)
                    analyzed_invest_results.append(['Growth Investing', invest_data])
                    analyzed_hist_results.append(['Growth Investing', historical_data])

                # index investment processing
                elif stra == 'Index Investing':
                    # Wait for 1 minute before making the API Call
                    time.sleep(60)
                    invest_data, historical_data = data_processing('Index Investing', total_capital, index_ticker_list)
                    analyzed_invest_results.append(['Index Investing', invest_data])
                    analyzed_hist_results.append(['Index Investing', historical_data])

                # quality investment processing
                elif stra == 'Quality Investing':
                    # Wait for 1 minute before making the API Call
                    time.sleep(60)
                    invest_data, historical_data = data_processing('Quality Investing', total_capital, quality_ticker_list)
                    analyzed_invest_results.append(['Quality Investing', invest_data])
                    analyzed_hist_results.append(['Quality Investing', historical_data])

                # value investment processing
                elif stra == 'Value Investing':
                    # Wait for 1 minute before making the API Call
                    time.sleep(60)
                    invest_data, historical_data = data_processing('Value Investing', total_capital, value_ticker_list)
                    analyzed_invest_results.append(['Value Investing', invest_data])
                    analyzed_hist_results.append(['Value Investing', historical_data])

            # fill data into html page if one strategy is selected
            if len(analyzed_invest_results) == 1 and len(analyzed_hist_results) == 1:
                return render_template("Portfolio_One Strategy.html", fgr=analyzed_invest_results, pgrd=analyzed_hist_results)

            # fill data into html page if two strategies are selected
            elif len(analyzed_invest_results) == 2 and len(analyzed_hist_results) == 2:
                return render_template("Portfolio_Two Strategies.html", fgr=analyzed_invest_results, pgrd=analyzed_hist_results)
            else:
                print("No strategy is selected or selected more than 2 strategies!")

        except ValueError:
            print('Please input correct ticker symbols')

        except requests.ConnectionError:
            print('Connection Error')

#Error handle
@app.errorhandler(404)
def resource_not_found(ex):
    return '''{}'''. format(ex)

@app.errorhandler(500)
def internal_server_error(ex):
    return '''{}'''. format(ex)

@app.errorhandler(AttributeError)
def attribute_error_handler(ex):
    return '''{}'''.format(ex)

@app.errorhandler(ValueError)
def value_error_handler(ex):
    return '''{}'''.format(ex)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `data_itempoint` to app.yaml.
    app.secret_key = os.urandom(12)
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
