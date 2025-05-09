# TradingAgentRL/RLlyStocked 

## Overview
Our 2-day hackathon project RLlyStocked utilizes Reinforcement Learning to analyze stock trends and suggest optimal trading actions. We use FinRL which allows users to build, train, and deploy trading agents that can make informed decisions based on market data. 

## To run the real-time portfolio asset and action, follow
1. Open the Jupyter notebook with Google Collab https://github.com/siren7075/TradingAgentRL/blob/main/TradingAgentFinRL.ipynb
2. Run the cells, switch the ticker/index and you will see how the agent performs in the last 60 days using real-time market data from YahooFinance

## To run the UI side, follow the below instructions
On command prompt,  cd into the folder and run the below comments:
1. pip install flash
2. python app.py
3. Navigate to http://localhost:5000/ in a browser
4. Input the ticker and you will see the suggestion on whether to buy/sell the stock and the agent performances
5. It is also designed to integrate FDC3 environment that allows listerning on the ticker indicator and change the results

## Result
### 7%-13% asset value increase in the past 60 days using PPO agent (May 9th), beating NASDAQ 3.25% increase
![image](https://github.com/user-attachments/assets/5a32b6f1-9dc7-453b-9c36-2529c979a041)

### sample action per timestamp AAPL
![image](https://github.com/user-attachments/assets/c87ac42f-9065-41ac-8d26-83cae0bf29bf)

### UI mockup Flask Framework

![image](https://github.com/user-attachments/assets/0be99414-e62e-4ad6-a21f-1729dde7334c)

## Reference
1. FinRL: https://github.com/AI4Finance-Foundation/FinRL
2. Trading Agents: https://github.com/benstaf/FinRL_DeepSeek ](https://huggingface.co/benstaf/Trading_agents/tree/main (mainly use PPO)













