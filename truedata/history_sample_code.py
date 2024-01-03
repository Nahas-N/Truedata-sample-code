from truedata import TD_hist
import logging
from dateutil.relativedelta import relativedelta        
from datetime import datetime

username = ""
password = ""
td_hist = TD_hist( username , password , log_level= logging.WARNING  )

def main():
    res = td_hist.get_historic_data('BANKNIFTY-I')
    print(res)
    res = td_hist.get_historic_data('BANKNIFTY-I', duration='3 D')
    print(res)
    res = td_hist.get_historic_data('BANKNIFTY-I', bar_size='30 mins')
    print(res)
    res = td_hist.get_historic_data('BANKNIFTY-I', start_time=datetime.now()-relativedelta(days=3))
    print(res)
    res = td_hist.get_historic_data('BANKNIFTY-I', end_time=datetime(2023, 11, 17, 12, 30))
    print(res)
    res = td_hist.get_n_historical_bars('BANKNIFTY-I', no_of_bars=30, bar_size= '5 min')
    print(res)
    res = td_hist.get_historic_data("BANKNIFTY-I", duration='2 D', bar_size='ticks', bidask=True , delivery = True)
    print(res)
    res = td_hist.get_gainers("NSEEQ", topn = 25 )
    print(res)
    res = td_hist.get_losers("NSEEQ", topn = 25 )
    print(res)
    res = td_hist.get_n_historical_bars("BANKNIFTY-I", no_of_bars=10, bar_size= 'ticks')
    print(res)
    bhav = td_hist.get_bhavcopy('EQ' , date=datetime(2023, 11, 16)  )
    print(bhav)
    res = td_hist.get_bhavcopy('FO')
    print(res)
    res = td_hist.get_bhavcopy('MCX')
    print(res)
    res = td_hist.get_bhavcopy('EQ', date=datetime(2023, 11, 30))
    print(res)
    current_BN_Spot = td_hist.get_historic_data("NIFTY BANK", duration='1 D', bar_size='tick')
    print(current_BN_Spot)
    # print(current_BN_Spot.to_dict(orient = 'records'))
    print(current_BN_Spot.iloc[0].timestamp.time() , current_BN_Spot.iloc[0].ltp )


if __name__ == '__main__':
    main()

