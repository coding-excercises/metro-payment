# system packages
import pandas as pd 
from icecream import ic
ic.configureOutput(prefix='metrocap -> ')
ic.configureOutput(includeContext=True)

# app packages

class MetroCap():

    def __init__(self):
        ...

    @staticmethod
    def load_cap():
        ic('Loading fare cap details')
        return pd.read_csv('./data/lookup/cap.csv') 

    @staticmethod
    def load_faretype():
        ic('Loading fare type details')
        df_metro_faretype = pd.read_csv('./data/lookup/faretype.csv') 
        return df_metro_faretype

    @staticmethod
    def get_fare_cap(df_zones, cap_type):
        df_metro_cap = MetroCap.load_cap()

        # get unique journey/zones
        group = df_zones.groupby('journey')
        df_uniq_zone = group.apply(lambda x: x['journey'].unique())

        # get highest/farthest zone
        df_merged_inner = df_metro_cap.merge(df_uniq_zone.to_frame(),
                            left_on='zones', right_on='journey', how='inner')
        df_merged_inner.sort_values([cap_type + '_cap'],ascending=False,inplace=True)
        df_merged_inner = df_merged_inner.head(1)

        # get the daily/weekly fare cap
        fare_cap = df_merged_inner[cap_type + '_cap'].item()
        ic(fare_cap)
        return fare_cap
