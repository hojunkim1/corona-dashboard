import pandas as pd


class CoronaData:
    def __init__(self):
        self.daily_df = pd.read_csv('data/daily_reports.csv')
        self.conditions = ['confirmed', 'deaths', 'recovered']

    @staticmethod
    def __make_df_by_condition(country, condition):
        df = pd.read_csv(f'data/time_{condition}.csv')
        if country != 'global':
            df = df.loc[df['Country/Region'] == country]
        df = df.drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long']).sum(axis=0).reset_index(
            name=condition)
        df = df.rename(columns={'index': 'Date'})
        return df

    def __merge_df(self, country):
        df = None
        for condition in self.conditions:
            if country == 'global':
                condition_df = self.__make_df_by_condition('global', condition)
            else:
                condition_df = self.__make_df_by_condition(country, condition)
            if df is None:
                df = condition_df
            else:
                df = df.merge(condition_df)
        return df

    def make_timeline_df_global(self):
        df = self.__merge_df('global')
        return df

    def make_timeline_df_by_country(self, country):
        df = self.__merge_df(country)
        return df

    def make_daily_df_global(self):
        df = self.daily_df[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index(name='count')
        df = df.rename(columns={'index': 'condition'})
        return df

    def make_daily_df_by_country(self):
        df = self.daily_df[['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
        df = df.groupby('Country_Region').sum().sort_values(by="Confirmed", ascending=False).reset_index()
        return df
