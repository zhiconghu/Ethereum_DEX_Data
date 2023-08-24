# Ethereum DEX Data

This repository conducts research using data from Decentralized Exchange(DEX), with a particular focus on UniSwap V3. We are interested in the market microstructure of DEXs, specifically on how 
the beliefs and risk aversion of liquidity providers affects the price of the traded asset.

## Arbitrage Index

This folder contains the code to build an arbitrage index, that indicates the expected profit of executing arbitrage trading between DEXs. However, this does not take into account many factors 
such as competition and price imapct of trade. This is simply an index that captures the difference in price of a single pair from different DEXs.

## Data Scraping and Cleaning

This folder contains the code to extract DEXs data from FlipSide Crypto APIs. This file also contains the code for cleaning the data and enriching it, such as adding liquidity parameter to liquidity
provision and withdrawal actions.

## Harvard Paper Simulation

This folder contains a paper, "Differential Liquidity Provision in Uniswap v3 and Implications for Contract Design" by Zhou Fan, Francisco Marmolejo-Coss, Ben Altschuler, He Sun, 
Xintong Wang, and David C. Parkes, on optimising liquidity provision for liquidity providers using projected gradient descent. In Functions.ipynb, we adapted the logic of Uniswap V3 
into Python and did the same optimisation problem by solving it through reinforcement learning (q-learning) and acheived similar results. We plan to move forward to lifting some 
of the main assumptions made in the optimisation problem and trying to solve it with reinforcement learning to see results

## Others

We have other files that explores the behaviour of current liquidity providers and traders. We aim to compare current actions with optimal actions proposed by our model.





