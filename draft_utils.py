import pandas as pd

def load_player_team_year():
    return pd.read_csv('outputs/1_player_team_year.csv')

def load_match_perf_team():
    return pd.read_csv('outputs/1_match-wise_performance.csv')

def load_season_perf():
    return pd.read_csv('outputs/1_season-wise_performance.csv')


def load_batting_impact():
    return pd.read_csv('outputs/2_batting_impact_score.csv')

def load_bowling_impact():
    return pd.read_csv('outputs/2_bowling_impact_score.csv')

def load_merged_impact():
    return pd.read_csv('outputs/2_merged_impact.csv')

print('DONE')