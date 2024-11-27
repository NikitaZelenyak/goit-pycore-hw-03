from datetime import datetime,timedelta

users = [
    {"name": "John Doe", "birthday": "1985.11.28"},
    {"name": "Jane Smith", "birthday": "1990.11.30"},
    {"name": "Alice Johnson", "birthday": "1992.11.27"},
    {"name": "Bob Brown", "birthday": "1988.11.25"},
]
def get_upcoming_birthdays(users):
    current_date =  datetime.today().date()
    end_day = current_date + timedelta(days = 7)
    pattern = "%Y.%m.%d"
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], pattern ).date()
        birthday_this_year  = birthday.replace(year=current_date.year)
        # print(birthday_this_year)
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year= current_date.year + 1)
            print(birthday_this_year)
        if current_date <= birthday_this_year <= end_day:
            if birthday_this_year.weekday() in (5,6):
               days_to_monday = 7 - birthday_this_year.weekday()
               cong_date = birthday_this_year + timedelta(days= days_to_monday)
            else:
                cong_date = birthday_this_year
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": cong_date.strftime(pattern),
            })
        return upcoming_birthdays

            

     




upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
