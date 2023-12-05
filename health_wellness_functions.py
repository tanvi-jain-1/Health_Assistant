# health_wellness_functions.py

import schedule
import time
from plyer import notification


def get_health_tip():
    # Replace this with your health tip fetching logic
    return "Remember to stay hydrated and eat a balanced diet."

def remind_medication():
    notification.notify(
        title="Medication Reminder",
        message="It's time to take your medication.",
        app_icon=None,
        timeout=10,
    )

if __name__ == "__main__":
    # Schedule medication reminder every day at 8:00 AM
    schedule.every().day.at("08:00").do(remind_medication)

    while True:
        schedule.run_pending()
        time.sleep(1)
