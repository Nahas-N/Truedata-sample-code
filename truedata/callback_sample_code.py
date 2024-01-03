from truedata import TD_live
import time
import logging

username = ""
password = ""

port = 8088
url = "pushbeta.truedata.in"

td_obj = TD_live(username , password , live_port = port, log_level= logging.DEBUG )
# td_obj = TD_live(username , password , url = url , live_port = 8088, log_level= logging.WARNING, full_feed = True )

symbols = [ "BANKNIFTY-I" , "SBIN-I" , "SBIN" , "NIFTY-I"]
td_obj.start_live_data(symbols)
time.sleep(1)

@td_obj.full_feed_trade_callback
def full_feed_callback( tick_data):
    print(f"full feed tick> {tick_data}")

@td_obj.full_feed_bar_callback
def new_min_bar_data( bar_data):
    print(f"full feed bar > {bar_data}")

@td_obj.trade_callback
def strategy_callback( tick_data):
    print(f"Tick > {tick_data}")

@td_obj.bidask_callback
def new_bidask( bidask_data):
    print(f"Bidask data > {bidask_data}")

@td_obj.one_min_bar_callback
def new_min_bar_data( bar_data):
    print(f"one min > {bar_data}")

@td_obj.five_min_bar_callback
def new_five_min_bar( bar_data):
    print(f"five min > {bar_data}")

@td_obj.greek_callback
def mygreek_bidask( greek_data):
    print(f"greek > " , greek_data)

# Keep your thread alive
while True:
    time.sleep(120)
