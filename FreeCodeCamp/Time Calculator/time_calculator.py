DAYS_OF_THE_WEEK_DICT = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

HALF_DAY = 12
WHOLE_DAY = 24


def get_later_days(days):
    if days == 1:
        return "(next day)"
    elif days > 1:
        return f"({days} days later)"
    return ""


def add_time(start: str, duration: str, day: bool = False):
    days_of_the_week = DAYS_OF_THE_WEEK_DICT.keys()
    string_time, string_day_type = start.split(" ")
    hours, minutes = map(int, string_time.split(":"))
    delta_h, delta_m = map(int, duration.split(":"))
    total_minutes = minutes + delta_m
    total_hours = hours + delta_h
    days_later = 0

    if total_minutes >= 60:
        total_hours += int(total_minutes / 60)
        total_minutes = int(total_minutes % 60)

    if (string_day_type == "PM") and (total_hours > HALF_DAY):
        if total_hours % WHOLE_DAY >= 1:
            days_later += 1
    if total_hours >= HALF_DAY:
        hours_left = int(total_hours / WHOLE_DAY)
        days_later += hours_left

    temp = total_hours
    while True:
        if temp < HALF_DAY:
            break
        if temp >= HALF_DAY:
            if string_day_type == "AM":
                string_day_type = "PM"
            elif string_day_type == "PM":
                string_day_type = "AM"
            temp -= HALF_DAY

    remaining_hours = int(total_hours % HALF_DAY) or hours + 1
    remaining_minutes = int(total_minutes % 60)

    calculated_time = f"{remaining_hours}:{remaining_minutes:02} {string_day_type}"
    if day:
        day = day.strip().title()
        selected_day_index = int(DAYS_OF_THE_WEEK_DICT[day] + days_later % 7)
        current_day = days_of_the_week[selected_day_index]
        calculated_time += f", {current_day} {get_later_days(days_later)}"
    else:
        calculated_time += f" {get_later_days(days_later)}"

    return calculated_time.strip()
