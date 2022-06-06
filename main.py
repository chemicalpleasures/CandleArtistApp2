import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import openpyxl
import numpy as np

artist_name_skus = ['reub', 'sculp', 'srsq', 'se', 'sacred', 'spilgrim', 'weekend', 'boan', 'fossil', 'oldmoon', 'sculpture', 'calebnichols', 'fearing', 'gelset', 'Topographies', 'window']
candle_cut = {
    "reub": 0,
    "sculp": 17.5,
    "srsq": 17.5,
    "se": 0,
    "sacred": 20,
    "spilgrim": 17.5,
    "weekend": 17.5,
    "boan": 17.5,
    "fossil": 17.5,
    "oldmoon": 20,
    "sculpture": 17.5,
    "calebnichols": 17.5,
    "fearing": 20,
    "gelset": 17.5,
    "Topographies": 20,
    "window": 20

}

df_list = []
orders = pd.read_csv('candlepayout.csv')
shirt_costs = pd.read_excel('shirtcosts.xlsx')
orders_cols = ['Title', 'SKU', 'Quantity', 'Unit Price', 'Order Total', 'Buyer', 'Order Date', 'Item Classification', 'Shipment Status Date', 'Payment Type']
df = pd.DataFrame(data=orders)
df['Pick & Pack Fee'] = 0.30

merge = pd.merge(df, shirt_costs, how="left", on="SKU")
print(merge.head())

blank_cost = merge['Blank Cost']
print_cost = merge['Print Cost']

def create_frame(artist):
    filt = (merge[merge['SKU'].str.contains(artist) == True])
    filt['Blank Cost'] = blank_cost
    filt['Print Cost'] = print_cost
    filt['Candle Cut'] = candle_cut[artist]
    filt['Unit Price'] = filt['Unit Price'].replace('[\$,]', '', regex=True).astype(float)
    net_sales = filt['Unit Price'].sum()       # df.assign(Percentage = lambda x: (x['Total_Marks'] /500 * 100))
    print(str(artist) + " Net Sales: " + str(net_sales))
    pick = filt['Pick & Pack Fee'].sum()
    print(str(artist) + " Total Pick & Pack Fees: " + str(pick))
    # filt['Candle Total Cut']
    # filt['Total Printing Fees']
    # filt['Payout to Band']

    # print(filt)
    filt.to_excel(artist + '.xlsx')
    return filt

for x in artist_name_skus:
    create_frame(x)
