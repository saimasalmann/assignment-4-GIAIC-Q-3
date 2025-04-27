BOLD_ITALICS = "\033[1;3m"
GREEN_COLOR = "\033[32m"
RESET = "\033[0m"

def seconds_in_a_year():
    """
    Calculate the number of seconds in a year.
    """
    days_in_a_year = 365
    hours_in_a_day = 24
    minutes_in_an_hour = 60
    seconds_in_a_minute = 60

    # Calculate total seconds in a year
    total_seconds = (days_in_a_year * hours_in_a_day *
                     minutes_in_an_hour * seconds_in_a_minute)
    
    print(f"\n{BOLD_ITALICS}Total seconds in a year {RESET}: {GREEN_COLOR}{total_seconds}{RESET} seconds")    


if __name__ == "__main__":
    seconds_in_a_year()    