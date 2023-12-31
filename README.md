# Ethereum DEX Data

This repository conducts research using data from Decentralized Exchange(DEX), with a particular focus on UniSwap V3. We are interested in the market microstructure of DEXs, specifically on how the beliefs and risk aversion of liquidity providers affects the price of the traded asset.

## Arbitrage Index

This folder contains the code to build an arbitrage index, that indicates the expected profit of executing arbitrage trading between DEXs. However, this does not take into account many factors such as competition and price imapct of trade. This is simply an index that captures the difference in price of a single pair from different DEXs.

## Data Scraping and Cleaning

This folder contains the code to extract DEXs data from FlipSide Crypto APIs. This file also contains the code for cleaning the data and enriching it, such as adding liquidity parameter to liquidity provision and withdrawal actions. The **Swaps Data Cleaning.ipynb** contains the code for combining all the csv files we scrape from FlipSide Crypto online interface into one single parquet file.

## Harvard Paper Simulation

This folder contains a paper, "Differential Liquidity Provision in Uniswap v3 and Implications for Contract Design" by Zhou Fan, Francisco Marmolejo-Coss, Ben Altschuler, He Sun, Xintong Wang, and David C. Parkes, on optimising liquidity provision for liquidity providers using projected gradient descent. In **Functions.ipynb**, we adapted the logic of Uniswap V3 into Python and did the same optimisation problem by solving it through reinforcement learning (q-learning) and acheived similar results. We plan to move forward to lifting some of the main assumptions made in the optimisation problem and trying to solve it with reinforcement learning to see results

## Old Crawlers Codes
This folder contains the file that scrapes data using Selenium in the following steps:

1. Opening a chrome site
2. Login in into FlipSide Crypto
3. Enter the necessary SQL
4. Download the as csv files
5. Read the latest data and modify SQL code accordingly and repeat Step 4

However, this method cannot be use now as FlipSide Crypto has updated their website and the crawler is no longer able to use the online API interface. The code is still kept here for reference. We should use the codes from the "Data Scraping and Cleaning" folder to scrape data.

## Others

We have other files that explores the behaviour of current liquidity providers and traders, **LP Data Descriptions.ipynb** and **Trader Data Descriptions.ipynb**. **Python_Implementation_of_UniSwap_V3.ipynb** defines several functions that mimic the actions of the UniSwap V3 Protocol. **FTX Case Study.ipynb** aim to look at investment behaviour of investors that were affect by the collapse of FTX. **History of USDC-WETH 500 10 Pool.ipynb** aims to replay all the trader and LP action of the pool history using our written functions in Python, there is still some existing errors from the actual data that can be because of missing trading or provision data or rounding errors from our function. Our final aim is to compare current actions with optimal actions proposed by our model.





