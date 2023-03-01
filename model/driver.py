from BacktestBase import *
from BacktestLongOnly import *
from BacktestLongShort import *

if __name__ == '__main__':
    bb = BacktestBase('AAPL.O', '2010-1-1', '2019-12-31', 10000) 
    print(bb.data.info())
    print(bb.data.tail())
    bb.plot_data()
    
    def run_strategies():
        lsbt.run_sma_strategy(42, 252)
        lsbt.run_momentum_strategy(60)
        lsbt.run_mean_reversion_strategy(50, 5)
    
    #lobt = BacktestLongOnly('AAPL.O', '2010-1-1', '2019-12-31', 10000, verbose=False)
    
    #run_strategies()
    
    # transaction costs: 10 USD fix, 1% variable
    #lobt = BacktestLongOnly('AAPL.O', '2010-1-1', '2019-12-31', 10000, 10.0, 0.01, False)
    #run_strategies()
    
    lsbt = BacktestLongShort('AAPL.O', '2010-1-1', '2019-12-31', 10000, 10.0, 0.01, False)
    run_strategies()