# NFTCollectionStats

Get NFT collection statistics from Etherscan and OpenSea[^1].

## Prerequisites

1. Download chromedriver from https://chromedriver.chromium.org/downloads (Make sure you download the same version as your chrome browser)
2. Move the chromedriver to the project directory
3. Install dependencies 
   * Linux: 
      ```shell
      $ python3 -m pip -r requirements.txt
      ```
   * Windows: 
      ```cmd
      > py -3 -m pip -r requirements.txt
      ```

## Usage

Linux
```shell
$ python3 NFTCollectionStats.py -c <CONTRACT_ADDRESS> -o <OPENSEA_COLLECTION_ID>
```

Windows
```cmd
> py -3 NFTCollectionStats.py --c <CONTRACT_ADDRESS> -o <OPENSEA_COLLECTION_ID>
```

## Usage Example

```shell
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