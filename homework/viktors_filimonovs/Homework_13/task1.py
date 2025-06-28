import os
import datetime


# a = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
# new_a = os.path.join(a, "eugene_okulik", "hw_13", "data.txt")
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(
    homework_path, "eugene_okulik", "hw_13", "data.txt"
)


with open(data_file_path, encoding="utf-8") as data_file:
    # print(data_file.read())
    for i, line in enumerate(data_file):
        parts = line.strip().split()
        if len(parts) >= 2:
            datatime_str = parts[1] + " " + parts[2]
            dt = datetime.datetime.strptime(
                datatime_str, "%Y-%m-%d %H:%M:%S.%f"
            )
            print("=" * 20)
            if i == 0:
                print("One weel later: ", dt + datetime.timedelta(weeks=1))
            elif i == 1:
                print("Day of the week: ", dt.strftime("%A"))
            elif i == 2:
                days_ago = (datetime.datetime.now() - dt).days
                print("Days ago: ", days_ago)
