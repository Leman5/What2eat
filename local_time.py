from datetime import datetime

def get_local_time():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    time_of_day = "morning" if 5 <= hour < 12 else \
                  "afternoon" if 12 <= hour < 17 else \
                  "evening" if 17 <= hour < 21 else "night"
    print(f"Time now: {hour:02d}:{minute:02d} ({time_of_day})")
    return {
        "hour": hour,
        "minute": minute,
        "time_of_day": time_of_day
    }

# time_data = get_local_time()
# print(time_data)