from datetime import datetime

def solution_station_2(date_str: str) -> str:
    """
    Takes a date string in 'YYYY-MM-DD' format and returns the day of the week in Japanese.
    """
    # Parse the date
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    
    # English weekday index (Monday=0, Sunday=6)
    weekday_index = date_obj.weekday()
    
    # Map to Japanese days
    japanese_days = {
        0: "月曜日",  # Monday
        1: "火曜日",  # Tuesday
        2: "水曜日",  # Wednesday
        3: "木曜日",  # Thursday
        4: "金曜日",  # Friday
        5: "土曜日",  # Saturday
        6: "日曜日"   # Sunday
    }
    
    return japanese_days[weekday_index]




