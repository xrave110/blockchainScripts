#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:39:09 2021

@author: anything
"""

max_days = 365 * 10
balance_in_usdt = 300000
token_price = 1
harvest_price = 0.1 / token_price
initial_balance = balance_in_usdt / token_price
farm_apy = 11
compound_interval = [x for x in range(1,101)]
days = [x for x in range(max_days)]
farmed_yield = 0
final_balance = initial_balance
best_balance = 0
best_interval = 0
yields = []
mean_yield = []

'''for day in days:
    final_balance = final_balance + (final_balance * (farm_apy/(100*365)))
    print(final_balance)
    
print('\n' + '{}'.format(final_balance) + '\n\n')'''

def harvest(balance):
    global farmed_yield
    compounded_balance = balance + farmed_yield - harvest_price
    yields.append(farmed_yield)
    farmed_yield = 0
    return compounded_balance

for interval in compound_interval:
    final_balance = initial_balance
    for day in days:
        farmed_yield = farmed_yield + (final_balance * (farm_apy/(100*365)))
        if (0 == (day % interval) or day == max_days-1):
            final_balance = harvest(final_balance)
    if final_balance > best_balance:
        best_interval = interval
        best_balance = final_balance
    mean_yield.append(sum(yields)/len(yields))
    #print('Final balance for interval {} days: {}'.format(interval, final_balance))
print('\nThe most profitable interval {}: {:.2f} with average yield {:.2f}'.format(best_interval, best_balance, mean_yield[best_interval]))

    
    
