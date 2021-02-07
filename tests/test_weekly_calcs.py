# system packages
import unittest
import pytest
import pandas as pd 

# app packages
from .context import FareCalc

class TotalWeeklyCalcTestSuite(unittest.TestCase):
    """Test the total weekly fare calculations for multiple journeys."""

    def test_calc_total_weekly_fare_case1(self):
        data = [['Monday',1015,'1 1',2021,2,1],
                ['Monday',1615,'1 2',2021,2,1],
                ['Monday',1645,'2 1',2021,2,1],
                ['Monday',1715,'1 2',2021,2,1],
                ['Monday',1815,'2 1',2021,2,1],
                ['Monday',1915,'1 2',2021,2,1],
                ['Tuesday',1015,'1 1',2021,2,1],
                ['Tuesday',1315,'1 1',2021,2,1],
                ['Tuesday',1415,'1 1',2021,2,1],
                ['Tuesday',1515,'1 2',2021,2,1],
                ['Tuesday',1730,'2 1',2021,2,1],
                ['Tuesday',2200,'1 1',2021,2,1],
                ] 
        df_weekly_commute = pd.DataFrame(data, columns = ['day','time','journey','year','month','date'])
        farecalc = FareCalc()
        weekly_fare = farecalc.calc_total_weekly_fare(df_weekly_commute)
        assert weekly_fare == 240, "Weekly fare for 1-1 zone travel before fare capping"

    def test_calc_total_weekly_fare_case2(self):
        data = [['Monday',1015,'1 1',2021,2,1],
                ['Monday',1615,'1 2',2021,2,1],
                ['Monday',1645,'2 1',2021,2,1],
                ['Monday',1715,'1 2',2021,2,1],
                ['Monday',1815,'2 1',2021,2,1],
                ['Monday',1915,'1 2',2021,2,1],
                ['Tuesday',1015,'1 1',2021,2,2],
                ['Tuesday',1315,'1 1',2021,2,2],
                ['Tuesday',1415,'1 1',2021,2,2],
                ['Tuesday',1515,'1 2',2021,2,2],
                ['Tuesday',1730,'2 1',2021,2,2],
                ['Tuesday',2200,'1 1',2021,2,2],
                ['Wednesday',700,'1 1',2021,2,3],
                ['Wednesday',710,'1 1',2021,2,3],
                ['Wednesday',800,'1 1',2021,2,3],
                ['Wednesday',810,'1 2',2021,2,3],
                ['Wednesday',830,'2 1',2021,2,3],
                ['Wednesday',1000,'1 1',2021,2,3],
                ['Thursday',700,'1 1',2021,2,4],
                ['Thursday',710,'1 1',2021,2,4],
                ['Thursday',800,'1 1',2021,2,4],
                ['Thursday',810,'1 2',2021,2,4],
                ['Thursday',830,'2 1',2021,2,4],
                ['Thursday',1000,'1 1',2021,2,4],
                ['Friday',700,'1 1',2021,2,5],
                ['Friday',710,'1 1',2021,2,5],
                ['Friday',800,'1 1',2021,2,5],
                ['Friday',810,'1 2',2021,2,5],
                ['Friday',830,'2 1',2021,2,5],
                ['Friday',1000,'2 2',2021,2,5],
                ['Saturday',700,'1 1',2021,2,6],
                ['Saturday',710,'1 1',2021,2,6],
                ['Saturday',800,'1 1',2021,2,6],
                ['Saturday',810,'1 2',2021,2,6],
                ['Saturday',830,'2 1',2021,2,6],
                ['Saturday',1000,'2 2',2021,2,6],
                ] 
        df_weekly_commute = pd.DataFrame(data, columns = ['day','time','journey','year','month','date'])
        farecalc = FareCalc()
        weekly_fare = farecalc.calc_total_weekly_fare(df_weekly_commute)
        assert weekly_fare == 600, "Weekly fare for 1-1 zone travel before fare capping"
