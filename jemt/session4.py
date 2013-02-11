
import requests
import getpass
from dateutil import parser
from pandas import Series
from pandas import DataFrame
#import datetime

user  = raw_input('Username: ')
password = getpass.getpass()
    
repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=(user, password))
repos_data = repos.json()

date_list = []
message_list = []
for repo in repos_data:
    commit_url = repo[u'commits_url'][:-6]
    urls = requests.get(commit_url, auth=(user, password))
    urls_data = urls.json()
    for url in urls_data:
        try:
            date = parser.parse(url[u'commit'][u'author']['date'])
            date_list.append(date)
            message = url[u'commit'][u'message']
            message_list.append(message)
        except TypeError: continue
        
s = Series(message_list, index=date_list, name="Bubbelibubb")
df = DataFrame(s)
    
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
    

print 'Most common weekday:', weekday_of_commits(df)
print 'Most common hour:', hour_of_commits(df)