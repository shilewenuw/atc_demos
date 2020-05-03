from yahoo_fin.stock_info import get_data
from trade_stat_logger.logger import SimpleLogger
import pandas as pd
import matplotlib.pyplot as plt


# x = pd.DataFrame([[100, 500], [200, 400], [50, 10]], columns=['jail time served', 'weight'])
# print(x)
# x.index = ['5/2', '5/3', '5/4']
# print(x)

logger = SimpleLogger()

ticker = 'AAPL'



aapl_data = get_data(ticker=ticker, start_date='01/01/2018', end_date='01/02/2020')
# create strategy to buy 100 shares AAPL on open, sell on close, for Tuesdays.
# for Fridays, short 100 shares, buy back on close
# -logger.log(security=ticker, shares=100, share_price=some_date)
# -logger.log(security=ticker, shares=-100, share_price=some_date
# -for loop + aapl_data.index
# -column indexing

# 0-Monday, 1-Tuesday, 2-Wednesday, 3-Thursday, 4-Friday

for date in aapl_data.index:
    d = date.to_pydatetime()
    weekday = d.weekday()
    open_price = aapl_data.loc[date]['open']
    # row_dataframe = aapl_data[date]
    # open = row_dataframe['open']
    close_price = aapl_data.loc[date]['close']
    if weekday == 1: # Tuesday
        logger.log(security=ticker, share_price=open_price, shares=100)
        logger.log(security=ticker, share_price=close_price, shares=-100)
    elif weekday == 4: # Friday
        logger.log(security=ticker, share_price=close_price, shares=-100)
        logger.log(security=ticker, share_price=open_price, shares=100)

logger.graph_statistics()