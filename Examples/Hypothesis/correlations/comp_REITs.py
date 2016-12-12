'''
Created on 12/11/2016

@author: SpringForward
@contact: SpringForward
@summary: Compare REITs performance among ["$SPX", "VNQ", "O", "ROIC", "DLR", "HCN", "KIM"]
'''

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

print "Pandas Version", pd.__version__


def main():
    ''' Main Function'''

    # List of symbols
    ls_symbols = ["$SPX", "VNQ", "O", "ROIC", "DLR", "HCN", "KIM"]

    # Start and End date of the charts
    dt_start = dt.datetime(2016, 1, 1)
    dt_end = dt.datetime(2016, 12, 9)

    # We need closing prices so the timestamp should be hours=16.
    dt_timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

    # Creating an object of the dataaccess class with Yahoo as the source.
    c_dataobj = da.DataAccess('Yahoo')

    # Keys to be read from the data, it is good to read everything in one go.
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    # Filling the data for NAN
    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method='ffill')
        d_data[s_key] = d_data[s_key].fillna(method='bfill')
        d_data[s_key] = d_data[s_key].fillna(1.0)

    # Getting the numpy ndarray of close prices.
    na_price = d_data['close'].values

    # Plotting the prices with x-axis=timestamps
    plt.clf()
    plt.plot(ldt_timestamps, na_price)
    plt.legend(ls_symbols)
    plt.ylabel('Adjusted Close')
    plt.xlabel('Date')
    plt.savefig('adjustedclose.pdf', format='pdf')

    # Normalizing the prices to start at 1 and see relative returns
    na_normalized_price = na_price / na_price[0, :]

    # Plotting the prices with x-axis=timestamps
    plt.clf()
    plt.plot(ldt_timestamps, na_normalized_price)
    plt.legend(ls_symbols)
    plt.ylabel('Normalized Close')
    plt.xlabel('Date')
    plt.savefig('normalized.pdf', format='pdf')

    # Copy the normalized prices to a new ndarry to find returns.
    na_rets = na_normalized_price.copy()

    # Calculate the daily returns of the prices. (Inplace calculation)
    # returnize0 works on ndarray and not dataframes.
    tsu.returnize0(na_rets)


    # ["$SPX", "VNQ", "O", "ROIC", "DLR", "HCN", "KIM"]
    # Plotting the plot of daily returns
    plt.clf()
    plt.plot(ldt_timestamps[0:60], na_rets[0:50, 0])  # $SPX 60 days
    plt.plot(ldt_timestamps[0:60], na_rets[0:50, 2])  # O 60 days
    plt.axhline(y=0, color='r')
    plt.legend(['$SPX', 'O'])
    plt.ylabel('Daily Returns')
    plt.xlabel('Date')
    plt.savefig('rets_SPXvsO.pdf', format='pdf')

    # Plotting the scatter plot of daily returns between XOM VS $SPX
    plt.clf()
    plt.scatter(na_rets[:, 0], na_rets[:, 2], c='blue')
    plt.ylabel('O')
    plt.xlabel('$SPX')
    plt.savefig('scatterSPXvsO.pdf', format='pdf')

    # Plotting the scatter plot of daily returns between O VS ROIC
    plt.clf()
    plt.scatter(na_rets[:, 2], na_rets[:, 3], c='blue')  # ROIC v O
    plt.ylabel('ROIC')
    plt.xlabel('O')
    plt.savefig('scatterROICvsO.pdf', format='pdf')

if __name__ == '__main__':
    main()
