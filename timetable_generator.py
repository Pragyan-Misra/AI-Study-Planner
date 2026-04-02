from datetime import datetime, timedelta

def generate_timetable(wake, sleep, study_hours, subjects):

    wake_time = datetime.strptime(wake, "%H:%M")
    sleep_time = datetime.strptime(sleep, "%H:%M")

    available_time = (sleep_time - wake_time).seconds / 3600

    session_time = study_hours / len(subjects)

    timetable = []
    current = wake_time

    for sub in subjects:

        end = current + timedelta(hours=session_time)

        timetable.append({
            "subject": sub,
            "start": current.strftime("%H:%M"),
            "end": end.strftime("%H:%M")
        })

        # Add break
        current = end + timedelta(minutes=15)

    return timetable