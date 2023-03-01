# Tradev Development Strategy

KISS: Keep It Simple Stupid
YAGNI: You Aint Going To Need It

## Phase One: Simple Implementation

0. Set up Virtual Environment first - DONE
1. Obtain & Clean FTSE data - DONE
2. First Trading Strategy: Use simple classification neural network to predict movements in the market - DONE
3. Implement SMA, Momentum and Mean-Reversion trading strategies
4. Implement basic historical simulation backstesting - DONE
5. Implement optimal bet sizing strategy
6. Implement feature importance analysis
7. Implement various different backtesting methods and compare
8. Implement the Meta-Strategy: mass produce models and pick the best performers by sharpe ratio and other metrics.
9. Generate trading order
10. Connect to brokerage and make a paper trade using predictions

- Once complete this forms version zero in main branch, after which a dev branch will be created for further development

## Phase Two and Beyond


1. Obtain different dataset types to explore different investment universes: ETF, Options,...
2. Expand corpus of trading strategies from one to many
    - Strategies listed below
    - Take into account transaction costs
    - Take into account trading capacity
    - Take into account computing time
3. Implement rigorous handling of potential biases(not sure how to do this yet)
4. Implement rigorous backtesting framework
5. Create method to find optimal trading order from the ensemble of signals generated from trading strategies
6. Automate the pipelines action so it can run on daily live data: 
    - Use a server
    - Data extraction, cleaning and input into strategies
    - Generate buy and sell orders
    - Interact with brokerage to complete order
7. Trade with real capital
8. Operations:
    - Add user guide: Installation, set-up, basic tutorial
    - Docs: Sphinx
    - Workflow: Github Actions
    - Virtual Environment
    - Unit Tests

# Tradev

Algorithmic trading pipeline. From data to trade order.

The Meta-Strategy:
"Amateurs develop individual strategies, believing that there is such a thing as a magical formula for riches. In contrast, professionals develop methods to mass-produce strategies. The money is not in making a car, it is in making a car factory."-Advances in Financial Machine Learning, Marcos Lopez De Prado

## 1. Data Extraction & Cleaning

- pandas
- numpy
- json?
- source?

## 2. Trading Srategies

- numpy
- sklearn
- keras, tensorflow

- Apply a range of trading strategies to data, to generate buy and sell orders
    - Neural Network Classification
    - Momentum
    - Mean Reversion
    - SMA
    - Linear Regression
    - Logistic Regression
    - Statistical Arbitrage
    - Sentiment Analysis
    - Market Making
        - Trading Execution Algorithms
        - Sniffing Algorithms(High Frequency Trading)

## 3. Feature Importance

## 4. Bet Sizing

## 5. Backtesting

- BACKTEST using multiple paradigms
 - Combinatorial Purged Cross-Validation
 - Backtesting on synthetic data

## 3. Portfolio

- Create an optimal portfolio over the trading strategy results

## 4. Brokerage

- Automate interaction with brokerage, sending order

## 5. Process Automation

- Automate the process to execute buy and sell orders

