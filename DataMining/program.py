# -*- coding: utf-8 -*-
"""
Data Mining app... 
Created on Wed Nov  1 16:34:25 2017
@author: glrulon
"""
import os
import csv
try:
    import statistics
except:
    import statistics_standin_for_py2 as statistics  
    
    
from data_types import Purchase





def main():
    print_header()
    filename = get_data_file()
    
    data = load_file(filename)
    
    query_data(data)



def print_header():
    print('-----------------------------------------')    
    print('      REAL ESTATE DATA MINING APP')    
    print('-----------------------------------------')
    
    
def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'Data', 
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    # with open(filename, 'r', encoding='utf-8') as fin:  encoding no good with py 2
    with open(filename, 'r') as fin:    
        reader = csv.DictReader(fin)  
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)
            
        #print(purchases[0].__dict__)
        
        return purchases
        
'''
This is better, but you still have to know indexes to summarize        
        header = fin.readline().strip()
        reader = csv.reader(fin, delimiter=',')  #could use other things like | as delimiter
        for row in reader:
            print(row)   #type(row) is a list
            beds = row[4]
            
 '''   
    

'''
def load_file(filename):  #basic way use this if we had to define filetype 
    with open(filename, 'r', encoding='utf-8', errors='ignore') as fin:
        header = fin.readline().strip()
        print('found header: ' + header)
        
        lines = []
        for line in fin:
            line_data = line.strip().split(',')
            bed_count = line_data[4]   # would need to convert from string if doing this way
            lines.append(line_data)
            
        print(lines[:5])
 '''       

#def get_price(p):  since function is small we can use lambda
#     return p.price

def query_data(data):
    
    # if data was sorted by price:
#    data.sort(key=get_price)
    data.sort(key=lambda p: p.price)
    
    # most expensive house?
    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths'.format(
          high_purchase.price, high_purchase.beds, high_purchase.baths))
    
    # least expensive house?
    low_purchase = data[0]
    print('The least expensive house is ${:,} with {} beds and {} baths'.format
          (low_purchase.price, low_purchase.beds, low_purchase.baths))
    
    # average price of house?
    #prices = []  # same as list()
    #for pur in data:
    #    prices.append(pur.price)
    
    prices = [
              p.price # projection or items like sql select use () for more than 1 item
              for p in data  #set to process
              
              ]
    
              
    avg_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(avg_price)))
    
    
    # average price of 2 bedroom houses?
    #prices = []
    #baths = []  
    #for pur in data:
    #    if pur.beds == 2:
    #        prices.append(pur.price)
    #       prices.append(pur.baths)
    
    two_bed_homes = [  # use () instead of [] to create generator expression
             p # projection or items like sql select use () for more than 1 item
             for p in data  #set to process
             if p.beds == 2  # test / conditions
              ]
              
              
    avg_price = statistics.mean([p.price for p in two_bed_homes])
    avg_baths = statistics.mean([p.baths for p in two_bed_homes])
    avg_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])
    print('Average 2 bedroom home is ${:,}, baths={}, sq ft={:,}'
          .format(int(avg_price), round(avg_baths), round(avg_sqft)))    
    


    
if __name__ == '__main__':
    main()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    