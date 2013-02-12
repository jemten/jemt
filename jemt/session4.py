import requests
import getpass
from dateutil import parser
from pandas import Series
from pandas import DataFrame

user  = raw_input('Username: ')
password = getpass.getpass()

def dataframe_builder(user, password):
    repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=(user, password))
    repos_data = repos.json()
    date_list = []
    message_list = []
    user_dict={}
    for repo in repos_data:
        no_commits_check = 0
        repo_name = repo[u'name']
        commit_url = repo[u'commits_url'][:-6]
        commits = requests.get(commit_url, auth=(user, password))
        commits_data = commits.json()
        for commit in commits_data:
            try: 
                date = parser.parse(commit[u'commit'][u'author']['date'])
                date_list.append(date)
                message = commit[u'commit'][u'message']
                message_list.append(message)
            except TypeError:
                no_commits_check = 1
                print repo_name
                print 'NO COMMITS!\n'
                continue
        if no_commits_check == 0:
            try:
                user_dict[repo_name] = Series(message_list, index=date_list, name=repo_name)
            except UnicodeEncodeError:
                print 'ucode error'
    df = DataFrame(user_dict)
    return df

def weekday_of_commits(df):
    commits_day = df.count(1).resample("D", how='sum').fillna(0)
    sort_day = commits_day.index.dayofweek
    sum_day_of_week=commits_day.groupby(sort_day).sum()
    weekday_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return(weekday_list[sum_day_of_week.idxmax()])

def hour_of_commits(df):
    commits_hour = df.count(1).resample("H", how='sum').fillna(0)
    sort_hour = commits_hour.index.hour
    sum_hour=commits_hour.groupby(sort_hour).sum()
    return(sum_hour.idxmax())

df = dataframe_builder(user, password)
print 'Most common weekday:', weekday_of_commits(df)
print 'Most common hour:', hour_of_commits(df)

