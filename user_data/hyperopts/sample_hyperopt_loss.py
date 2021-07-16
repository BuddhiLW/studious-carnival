# coding: utf-8

from datetime import datetime
from math import exp

from pandas import DataFrame

from freqtrade.optimize.hyperopt import IHyperOptLoss


# Define some constants:

# set TARGET_TRADES to suit your number concurrent trades so its realistic
# to the number of days
TARGET_TRADES = 600
# This is assumed to be expected avg profit * expected trade count.
# For example, for 0.35% avg per trade (or 0.0035 as ratio) and 1100 trades,
# self.expected_max_profit = 3.85
# Check that the reported Σ% values do not exceed this!
# Note, this is ratio. 3.85 stated above means 385Σ%.
EXPECTED_MAX_PROFIT = 3.0

# max average trade duration in minutes
# if eval ends with higher value, we consider it a failed eval
MAX_ACCEPTED_TRADE_DURATION = 300


class SampleHyperOptLoss(IHyperOptLoss):
    """
    Defines the default loss function for hyperopt
    This is intended to give you some inspiration for your own loss function.

    The Function needs to return a number (float) - which becomes smaller for better backtest
    results.
    """

    @staticmethod
    def hyperopt_loss_function(results: DataFrame, trade_count: int,
                               min_date: datetime, max_date: datetime,
                               *args, **kwargs) -> float:
        """
        Objective function, returns smaller number for better results
        """
        period=self.max_date - self.min_date
        days_period = period.days

        ## Adding slippage of 0.5% per trade
        total_profit = total_profit - 0.0005
        expected_yearly_return = total_profit.sum()/days_period

        if (np.std(total_profit) != 0.):
            sharp_ratio = expeted_yearly_return/np.std(total_profit)*np.sqrt(365)
        else:
            sharp_ratio=1.

        sharp_ratio = -sharp_ratio
        result = sharp_ratio
        self.resultloss = result
        return result

        # total_profit = results.profit_percent.sum()
        # trade_duration = results.trade_duration.mean()

        # trade_loss = 1 - 0.25 * exp(-(trade_count - TARGET_TRADES) ** 2 / 10 ** 5.8)
        # profit_loss = max(0, 1 - total_profit / EXPECTED_MAX_PROFIT)
        # duration_loss = 0.4 * min(trade_duration / MAX_ACCEPTED_TRADE_DURATION, 1)
        # result = trade_loss + profit_loss + duration_loss
        # return result

    # def calculate_loss(self, total_profit):
