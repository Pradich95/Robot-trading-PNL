import json
from typing_extensions import Self


class Pnl():

    def __init__(self, client):
        """
        client is used to issue orders
        """
        self.client = client

    def process_candle(self, candle_msg:str):
        """This function is called when a new candle_msg is received.
            Candle message is a string of the form:
            {'symbol_key' : {'c': [174.3], 'h': [174.3], 'l': [174.19], 'o': [174.19], 's': 'ok', 't': [1643670000], 'v': [1888]}

            Note that there are list, so you can have multiple candles in one message.
        """
        if self.client.money > 300 : 
            self.client.buy('AAPL', 1)
            breakpoint()
        
candle_dict = json.loads(candle_msg)  
for k, v in candle_dict.items():
            if 'AAPL' == k :
                Self.update_aapl_mean(v)

                print(f"Moyenne :{self.total_AAPL/self.count_AAPL}")
                self.sell_if_needed(k, v)
def update_aapl_mean(self, v):                           
        self.count_AAPL += 1
        self.total_AAPL += v['c']

def sell_if_needed(self, k, v):
        if v['c'] < self.previous_price  : 
            self.client.sell(k,1)
        elif self.client.money > v['c']: 
            self.client.buy(k,1)

            print(finnhub_client.technical_indicator(
        symbol="AAPL",
        resolution="D",
        _from=1583098857,
        to=1584308457,
        indicator="rsi",
        indicator_fields={"timeperiod": 3},
    )
)

