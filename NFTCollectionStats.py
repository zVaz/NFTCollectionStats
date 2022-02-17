import argparse
from datetime import datetime
from OpenSeaCrawler import OpenSeaCrawler
from EtherscanNFTTX import EtherscanNFTTX

# Created to analyze the Meta Eagle Club NFT collection :)
# CONTRACT_ADDRESS      = "0xeb6dffb87315a2bdf4dedf72b993adc960773a0d"
# OPENSEA_COLLECTION_ID = "metaeagleclub-mec"

def main(contract_address, opensea_collection_id) -> None:
   etherscan_stats = EtherscanNFTTX(contract_address).get_stats()

   print("--------------------")
   print("| Token Statistics |")
   print("--------------------")

   print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))	

   print(f"---Etherscan---")
   print(f"Transactions                   : {etherscan_stats.transactions}")
   print(f"Tokens                         : {etherscan_stats.tokens}")
   print(f"Owners                         : {len(etherscan_stats.total_owners)}")
   print(f"Transferred                    : {etherscan_stats.tokens - etherscan_stats.only_minted}")
   print(f"Only Minted                    : {etherscan_stats.only_minted}")
   print(f"Only Minted Owners             : {len(etherscan_stats.only_minted_owners)}")
   for i, tansactions_over_counter in etherscan_stats.tansactions_over_counters.items():
      print(f"Tokens transferred over {i} times: {tansactions_over_counter}")

   print(f"---OpenSea---")
   with OpenSeaCrawler(opensea_collection_id) as osc:
      osc.set_filter_buy_now()
      print(f"Buy Now             : {osc.get_num_of_items_str()}")

      for max_price in [x * 0.1 for x in range(6, 11)]:
         osc.set_filter_eth_max_price(max_price)
         print(f"Buy Now under {max_price:.1f}ETH: {osc.get_num_of_items_str()}")

      opensea_stats = osc.get_opensea_stats()
      print(f"Total Volume        : {opensea_stats['total_volume']:.3f}ETH")
      print(f"Average Price       : {opensea_stats['average_price']:.3f}ETH")
      print(f"Floor Price         : {opensea_stats['floor_price']:.3f}ETH")

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='NFT Collection Statistics')
   parser.add_argument('-c', '--contract_address'     , help='Contract Address'     , required = True)
   parser.add_argument('-o', '--opensea_collection_id', help='Opensea Collection Id', required = True)
   args = parser.parse_args()

   main(args.contract_address, args.opensea_collection_id)
