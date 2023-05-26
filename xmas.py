from datetime import datetime


def get_days_before_xmas():
    """
    Returns days before xmas.
    """

    today = datetime.today()
    xmas_day = 25
    xmas_month = 12
    year_now = datetime.today().year
    xmas_date = f'{year_now}-{xmas_month}-{xmas_day}'
    # str -> date object: strptime
    # date object -> str: strftime
    xmas_day_in_dateobj = datetime.strptime(xmas_date, '%Y-%m-%d')
    days_before_xmas = (xmas_day_in_dateobj - today).days
    return days_before_xmas


if __name__ == '__main__':
    days_before_xmas = get_days_before_xmas()
    print(days_before_xmas)
    print("Happy New Year")
