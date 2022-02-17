import os
import json
import time
import requests
from dataclasses import dataclass, field

ETHERSCAN_FORCE_FEATCH_DATA = True
ETHERSCAN_DATA_FILE = "etherscan_data.json"
TRANSACTIONS_COUNT_FROM = 2
TRANSACTIONS_COUNT_TO   = 3

class EtherscanNFTTX():

   @dataclass
   class EtherscanNFTTXStats():
      transactions                   : int  = 0
      tokens                         : int  = 0
      only_minted                    : int  = 0
      only_minted_owners             : set  = field(default_factory=set)
      total_owners                   : set  = field(default_factory=set)
      tansactions_over_counters      : dict = field(default_factory=dict)
   
   @dataclass
   class TokenData():
      token_id     : int = 0
      transactions : int = 0
      owner        : str = ""

   def __init__(self, contract_address: str):
      self.contract_address = contract_address
      self.data             = self._get_contract_token_data_from_etherscan()
      self.tokens_data      = self._process_data()
   
   def _get_contract_token_data_from_etherscan(self) -> list:
      data = []
      startblock = 0
      if not os.path.isfile(ETHERSCAN_DATA_FILE) or ETHERSCAN_FORCE_FEATCH_DATA:
         while True:
            get_data = {
               "module": "account",
               "action": "tokennfttx",
               "contractaddress": self.contract_address,
               "startblock": startblock,
               "endblock"  : "latest"
            }
            
            r = requests.get("https://api.etherscan.io/api", data=get_data)
            res_json = r.json()

            if len(res_json["result"]) != 0:
               data.extend(res_json["result"])
               startblock = int(res_json["result"][-1]["blockNumber"]) + 1
               time.sleep(6)
            else:
               break

         with open(ETHERSCAN_DATA_FILE, "w") as f:
            f.write(json.dumps(data))
      else:
         with open(ETHERSCAN_DATA_FILE, "r") as f:
            data = json.loads(f.read())
      return data
   
   def _process_data(self) -> dict:
      tokens_data = {}
      # Count specific tokenID transaction and se current owner
      for d in self.data:
         if d["tokenID"] not in tokens_data:
            tokens_data[d["tokenID"]] = self.TokenData(token_id = d["tokenID"])
         tokens_data[d["tokenID"]].transactions += 1
         tokens_data[d["tokenID"]].owner = d["to"]
      return tokens_data
   
   def get_stats(self) -> EtherscanNFTTXStats:
      stats = self.EtherscanNFTTXStats()

      stats.transactions = len(self.data)
      stats.tokens       = len(self.tokens_data)

      for tokenID, token_data in self.tokens_data.items():
         stats.total_owners.add(token_data.owner)
         
         if token_data.transactions == 1:
            stats.only_minted += 1
            stats.only_minted_owners.add(token_data.owner)
         
         for i in range(TRANSACTIONS_COUNT_FROM, TRANSACTIONS_COUNT_TO + 1):
            if token_data.transactions > i:
               if i not in stats.tansactions_over_counters:
                  stats.tansactions_over_counters[i] = 0
               stats.tansactions_over_counters[i] += 1
      
      return stats
