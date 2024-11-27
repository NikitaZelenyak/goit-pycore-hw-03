from datetime import datetime

def get_days_from_today(date):
    date_format = "%Y-%m-%d"
    days_differences = datetime.today() - datetime.strptime(date, date_format)
    print(days_differences)


get_days_from_today("2020-10-09")