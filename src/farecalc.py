# system packages
import calendar
from icecream import ic
ic.configureOutput(prefix='dailyfare -> ')
ic.configureOutput(includeContext=True)

# app packages
from src.metrocap import MetroCap

class FareCalc():

    def __init__(self):
        ...

    @staticmethod
    def calc_daily_fare(year, month, date, time, journey, fare_cap):
        weekday = calendar.weekday(year,month,date)
        metcap = MetroCap()
        df_fare_type = metcap.load_faretype()

        df_fare = df_fare_type.loc[(df_fare_type['zones'].str.contains(str(journey))) 
                                        & (df_fare_type['days'].str.contains(str(weekday)))
                                        & (df_fare_type['start_time'] <= time)
                                        & (df_fare_type['end_time'] >= time)]
        ic(df_fare)
        fare = df_fare['fare'].item()
        return fare

    @staticmethod
    def calc_total_daily_fare(df_daily_commute):
        metcap = MetroCap()
        fare_cap = metcap.get_fare_cap(df_daily_commute, 'daily')

        # accumulator to hold total daily fare for a day
        total_daily_fare = 0

        for index, row in df_daily_commute.iterrows():
            ic(fare_cap)
            ic(index, row['year'], row['month'], row['date'], row['time'], 
            row['journey'])
            balance_allowed_fare = fare_cap - total_daily_fare
            ic(index)
            ic(balance_allowed_fare)

            if (balance_allowed_fare <= fare_cap and balance_allowed_fare > 0):
                fare = FareCalc.calc_daily_fare(row['year'], row['month'], row['date'], 
                                row['time'], row['journey'], fare_cap)
                if (total_daily_fare + fare >= fare_cap):
                    fare = fare_cap - total_daily_fare
                    total_daily_fare = total_daily_fare + fare
                elif (fare <= balance_allowed_fare):
                    total_daily_fare = total_daily_fare + fare
            ic(fare)
            ic(total_daily_fare)
        
        return total_daily_fare

    @staticmethod
    def calc_total_weekly_fare(df_daily_commute):
        metcap = MetroCap()
        weekly_fare_cap = metcap.get_fare_cap(df_daily_commute, 'weekly')
        
        # accumulator to hold total daily fare for a week
        # a week is assumed to be a continuous or sparse
        # 7 or lesser calendar days
        total_weekly_fare = 0    
        uniq_days = df_daily_commute.day.unique()

        if (len(uniq_days) <= 7 and len(uniq_days) > 0):
            for day in uniq_days:
                ic(day)
                ic(weekly_fare_cap)
                per_day_fare = 0

                df_per_day_commute = df_daily_commute[0:0]
                df_per_day_commute = df_daily_commute.loc[df_daily_commute['day'] == day]
                ic(df_per_day_commute)

                balance_weekly_allowed_fare = weekly_fare_cap - total_weekly_fare
                ic(balance_weekly_allowed_fare)

                if (balance_weekly_allowed_fare <= weekly_fare_cap and 
                    balance_weekly_allowed_fare > 0):
                    per_day_fare = FareCalc.calc_total_daily_fare(df_per_day_commute)
                    if (total_weekly_fare + per_day_fare >= weekly_fare_cap):
                        per_day_fare = weekly_fare_cap - total_weekly_fare
                        total_weekly_fare = total_weekly_fare + per_day_fare
                    elif (per_day_fare <= balance_weekly_allowed_fare):
                        total_weekly_fare = total_weekly_fare + per_day_fare
                ic(per_day_fare)
                ic(total_weekly_fare)

        return total_weekly_fare