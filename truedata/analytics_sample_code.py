import logging
from truedata import TD_analytics
from datetime import date as d

username = ""
password = ""

my_analytics = TD_analytics( username , password , log_level= logging.DEBUG )

def main():
    gainer = my_analytics.get_oi_gainer_losers(top = 200 , series = "XX" , sort_by = "OiGainersPriceGainers")
    print(gainer)
    gainer = my_analytics.get_index_gainer_losers(top = 20 ,  segment = "EQ" ,index_name = "NIFTY 500" ,sort_by = "gainers")
    print(gainer)
    gainer = my_analytics.get_industry_gainer_losers(	top = 20 ,  segment = "EQ" , industry = "Information Technology" ,sort_by = "gainers")
    print(gainer)
    chain = my_analytics.get_option_chain(symbol = "NIFTY" , expiry = d(2023 , 12 , 28) , greeks = True)
    print(chain)
    hist_greeks = my_analytics.get_history_greeks(	symbol = "RELIANCE" , expiry = d(2023 , 12 , 28) , strike = 2400 ,series = "CE" )
    print(hist_greeks)
    ltp_greeks = my_analytics.get_history_greeks(	symbol = "RELIANCE" , expiry = d(2023 , 12 , 28) , strike = 2400 ,series = "CE" , ltp = True )
    print(ltp_greeks)

if __name__ == "__main__":
    main()