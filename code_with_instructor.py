from yahoo_fin.stock_info import get_data
from trade_stat_logger.logger import SimpleLogger

ticker = 'AAPL'

# x is a pandas DataFrame
x = get_data(ticker='AAPL', start_date='01/01/2018', end_date='01/01/2019')

logger = SimpleLogger()

# 0-Monday, 1-Tuesday, 2-Wednesday, 3-Thursday, 4-Friday

for d in x.index:
    date = d.to_pydatetime()
    day_of_week = date.weekday()
    open_price = x.loc[date]['open']
    close_price = x.loc[date]['close']
    if day_of_week == 1:
        logger.log(security=ticker, shares=100, share_price=open_price)
        logger.log(security=ticker, shares=-100, share_price=close_price)
    elif day_of_week == 4:
        logger.log(security=ticker, shares=-100, share_price=open_price)
        logger.log(security=ticker, shares=100, share_price=close_price)

logger.graph_statistics()

