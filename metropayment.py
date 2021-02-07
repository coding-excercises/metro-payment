# system packages
import pandas as pd 

# set prefix to all debug statements
# include module name and line no in debug
from icecream import ic
ic.configureOutput(prefix='metropayment -> ')
ic.configureOutput(includeContext=True)

# install so that ic is available in builtin modules for all packages
# although below approach is pythonic, it jell with linters
from icecream import install
install()

# app packages
from src.farecalc import FareCalc
from src.metrocap import MetroCap

def load_daily_journey():
    ic('Load journeys for a day')
    return pd.read_csv('./data/journeys/daily_journey.csv') 

def load_weekly_journey():
    ic('Load journeys for a week')
    return pd.read_csv('./data/journeys/weekly_journey.csv') 

def main():
    # enable ic to see debug output in console
    ic.disable()

    df_daily_commute = load_daily_journey()
    ic(df_daily_commute)
    farecalc = FareCalc()
    daily_fare = farecalc.calc_total_daily_fare(df_daily_commute)
    ic(daily_fare)
    df_weekly_commute = load_weekly_journey()
    ic(df_weekly_commute)
    weekly_fare = farecalc.calc_total_weekly_fare(df_weekly_commute)
    ic(weekly_fare)

if __name__ == '__main__':
    main()