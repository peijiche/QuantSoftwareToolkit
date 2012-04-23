'''
(c) 2011, 2012 Georgia Tech Research Corporation
This source code is released under the New BSD license.  Please see
http://wiki.quantsoftware.org/index.php?title=QSTK_License
for license details.

Created on 1/1/2011

@author: Drew Bratcher
@contact: dbratcher@gatech.edu
@summary: Contains utility functions for fund time series
'''

import qstkutil.tsutil as tsu

def get_winning_days(fund_ts):
    """
    @summary Returns percentage of winning days in fund time series
    @param fund_ts: pandas time series of daily fund values
    @return Percentage of winning days over fund time series
    """
    return tsu.get_winning_days(tsu.daily(fund_ts))

def get_max_draw_down(fund_ts):
    """
    @summary Returns max draw down of fund time series (in percentage)
    @param fund_ts: pandas time series of daily fund values
    @return Max draw down of fund time series
    """
    return tsu.get_max_draw_down(tsu.daily(fund_ts))

def get_sortino_ratio(fund_ts):
    """
    @summary Returns daily computed Sortino ratio of fund time series
    @param fund_ts: pandas time series of daily fund values
    @return Sortino ratio of fund time series
    """
    return tsu.get_sortino_ratio(tsu.daily(fund_ts))

def get_sharpe_ratio(fund_ts):
    """
    @summary Returns daily computed Sharpe ratio of fund time series
    @param fund_ts: pandas time series of daily fund values
    @return  Sharpe ratio of  fund time series
    """
    return tsu.get_sharpe_ratio(tsu.daily(fund_ts))



