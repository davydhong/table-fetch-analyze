import sys
from datetime import datetime, timedelta
import csv
from statistics import mean, variance

_, startDate, endDate, resource = sys.argv
startDate = datetime.strptime(startDate, '%Y-%m-%d')
endDate = datetime.strptime(endDate, '%Y-%m-%d')

pricesWithinRage = []

# with open(f'{resource}.csv', 'w', newline='') as csvfile:
with open(f'{resource}.csv', newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter='|')

    rowNum = 0
    for row in dataReader:
        if rowNum != 0:
            rowDate = datetime.strptime(row[0], '%b %d, %Y')
            if startDate <= rowDate <= endDate:
                # NOTE: turn on the print to check the correct dates are analyzed (I checked)
                # print(row[0])
                pricesWithinRage.append(float(row[1].replace(',', '')))
        rowNum += 1


# output clean-up
meanPrice = float(f'{mean(pricesWithinRage):.2f}')
priceVariance = float(f'{variance(pricesWithinRage):.4f}')
print({
    'resource': resource,
    'mean':  meanPrice,
    'variance': priceVariance
})
