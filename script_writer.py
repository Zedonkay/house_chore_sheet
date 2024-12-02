import pandas
import datetime
def get_sundays(start_date, end_date):
        sundays = []
        current_date = start_date
        while current_date <= end_date:
            if current_date.weekday() == 6:  # Sunday
                sundays.append(current_date)
            current_date += datetime.timedelta(days=1)
        return sundays
def write_datasheet():
    Upper_floor_names = ["Ishayu", "Jackson"]
    lower_floor_names = [ "Aidan", "Dan", "Hamza"]
    start_date = datetime.date(2024, 12, 1)
    end_date = datetime.date(2025, 5, 4)
    sundays = get_sundays(start_date, end_date)
    dict = {}
    index = 0
    for sunday in sundays:
        dict[sunday] = {}
        
def main():
    write_datasheet()
if __name__ == "__main__":
    main()