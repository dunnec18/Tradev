from BacktestBase import *

if __name__ == '__main__':
    bb = BacktestBase('AAPL.O', '2010-1-1', '2019-12-31', 10000) 
    print(bb.data.info())
    print(bb.data.tail())
    bb.plot_data()