# investment data scrapper and analyzer


## installation
```
pipenv shell
pipenv install
```

## getInvestingData.py
this program scraps `https://www.investing.com/commodities/` for gold/silver pricing and stores the data as csv ('|' separated).

How to run
```
python3 getInvestingData.py
```


## getCommodityPrice.py
this program reads from `gold.csv` and `silver.csv` and outputs the mean price and price variance between the input date range 



Example Input:
```
python3 getCommodityPrice.py 2019-04-01 2019-04-20 gold
python3 getCommodityPrice.py 2019-04-01 2019-04-20 silver
```