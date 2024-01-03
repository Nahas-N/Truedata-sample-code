from truedata import TD_live
import time
import logging
from datetime import datetime as dt
import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)

username = ""
password = ""

td_obj = TD_live( username , password , log_level= logging.WARNING )
my_symbols = [ "BANKNIFTY-I" , "SBIN-I" , "SBIN" , "NIFTY 50" ]
td_obj.start_live_data(my_symbols)
time.sleep(1)

sbi_chain = td_obj.start_option_chain( 'SBIN' , dt(2023 , 11 , 30) , 20 , greek = True )
nifty_chain = td_obj.start_option_chain('NIFTY' , dt(2023 , 12 , 7 ) , chain_length = 20 , bid_ask = True, greek = True )
bnf_chain = td_obj.start_option_chain('BANKNIFTY' , dt(2023 , 11 , 30) , 100 , bid_ask = True , greek = True )
crudeoil_chain = td_obj.start_option_chain('CRUDEOIL' , dt(2023 , 12 , 14) , 20 , bid_ask = True , greek = True )
time.sleep(1)

@td_obj.bidask_callback
def new_bidask( bidask_data):
    if bidask_data.symbol in my_symbols:
        print( "bidask data >" , bidask_data)

@td_obj.one_min_bar_callback
def new_min_bar_data( bar_data):
    if bar_data.symbol in my_symbols:
        print( "one min >" , bar_data)

@td_obj.five_min_bar_callback
def new_five_min_bar( bar_data):
    if bar_data.symbol in my_symbols:
        print( "five min >" , bar_data)

@td_obj.greek_callback
def mygreek_bidask( greek_data):
    if greek_data.symbol in my_symbols:
        print( "greek >" , greek_data)

@td_obj.trade_callback
def strategy_callback(tick_data):
    if tick_data.symbol in my_symbols:
        print( "Tick >" , tick_data)

while True:
    print(sbi_chain.get_option_chain())
    print(nifty_chain.get_option_chain())
    print(bnf_chain.get_option_chain())
    print(crudeoil_chain.get_option_chain())
    time.sleep(5)

