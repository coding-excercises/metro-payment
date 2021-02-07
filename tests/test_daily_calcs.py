# system packages
import unittest
import pytest
import pandas as pd 

# app packages
from .context import FareCalc

class DailyCalcTestSuite(unittest.TestCase):
    """Test the daily fare calculation for a single day and journey."""

    def test_calc_daily_fare(self):
        farecalc = FareCalc()
        daily_fare = farecalc.calc_daily_fare(2021,2,2,1000,'1 1', 100)
        assert daily_fare == 30, "Daily fare for a 1-1 zone travel is correct"

class TotalDailyCalcTestSuite(unittest.TestCase):
    """Test the total daily fare calculations for multiple journeys."""

    def test_calc_total_daily_fare_case1(self):
        data = [['Monday', 705, '1 1',2021,2,1],
                ['Monday', 1029, '1 1',2021,2,1],
                ] 
        df_daily_commute = pd.DataFrame(data, columns = ['day','time','journey','year','month','date'])
        farecalc = FareCalc()
        daily_fare = farecalc.calc_total_daily_fare(df_daily_commute)
        assert daily_fare == 60, "Daily fare for 1-1 zone travel before fare capping"

    def test_calc_total_daily_fare_case2(self):
        data = [['Monday', 705, '1 1',2021,2,1],
                ['Monday', 800, '1 1',2021,2,1],
                ['Monday', 900, '1 2',2021,2,1],
                ['Monday', 1029, '2 1',2021,2,1],
                ] 
        df_daily_commute = pd.DataFrame(data, columns = ['day','time','journey','year','month','date'])
        farecalc = FareCalc()
        daily_fare = farecalc.calc_total_daily_fare(df_daily_commute)
        assert daily_fare == 120, "Daily fare for multi-zone travel after fare capping"
