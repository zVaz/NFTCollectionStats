# NFTCollectionStats

`NFTCollectionStats` is a NFT collection statistics extractor from [Etherscan](https://etherscan.io/) and [OpenSea](https://opensea.io/)[^1].

## Prerequisites

1. Download chromedriver from https://chromedriver.chromium.org/downloads (Make sure you download the same version as your chrome browser)
2. Move the chromedriver to the project directory
3. Install dependencies 
   ```console
   $ python3 -m pip install -r requirements.txt
   ```

## Usage

Linux
```console
$ python3 NFTCollectionStats.py
usage: NFTCollectionStats.py [-h] -c CONTRACT_ADDRESS -o OPENSEA_COLLECTION_ID

NFT Collection Statistics

optional arguments:
  -h, --help            show this help message and exit
  -c CONTRACT_ADDRESS, --contract_address CONTRACT_ADDRESS
                        Contract Address
  -o OPENSEA_COLLECTION_ID, --opensea_collection_id OPENSEA_COLLECTION_ID
                        Opensea Collection Id
```

## Usage Example

```console
$ python3 NFTCollectionStats.py -c 0xeb6dffb87315a2bdf4dedf72b993adc960773a0d -o metaeagleclub-mec
--------------------
| Token Statistics |
--------------------
17/02/2022 16:16:02
---Etherscan---
Transactions                   : 18078
Tokens                         : 12000
Owners                         : 6917
Transferred                    : 4922
Only Minted                    : 7078
Only Minted Owners             : 4215
Tokens transferred over 2 times: 1009
Tokens transferred over 3 times: 133
---OpenSea---
Buy Now             : 497 items
Buy Now under 0.6ETH: 24 items
Buy Now under 0.7ETH: 88 items
Buy Now under 0.8ETH: 167 items
Buy Now under 0.9ETH: 197 items
Buy Now under 1.0ETH: 221 items
Total Volume        : 2773.737ETH
Average Price       : 0.611ETH
Floor Price         : 0.550ETH
```

[^1]: I used selenium in order to avoid the API key request from OpenSea