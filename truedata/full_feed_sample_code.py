from truedata import TD_live
import time
import logging

username = ""
password = ""
td_obj = TD_live(username , password, url = "push.truedata.in", live_port = 9084 ,  log_level= logging.WARNING ,  full_feed = True, dry_run = False )

time.sleep(1)

@td_obj.full_feed_trade_callback
def full_feed_trade( tick_data):
    print( "Tick >" , tick_data)

@td_obj.greek_callback
def mygreek_bidask( greek_data):
    print( "Greek >" , greek_data)

@td_obj.bidask_callback
def new_bidask( bidask_data):
    print( "BidAsk >" , bidask_data)

@td_obj.full_feed_bar_callback
def full_feed_bar( bar_data):
    print( "Bardata >" , bar_data )

# Keep your thread alive
while True:
    time.sleep(120)
