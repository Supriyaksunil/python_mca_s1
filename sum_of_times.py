class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour  # Private attribute
        self.minute = minute
        self.second = second

    def __add__(self, other):
        total_seconds = self.second + other.second
        total_minutes = self.minute + other.minute + (total_seconds // 60)
        total_hours = self.hour + other.hour + (total_minutes // 60)

        seconds = total_seconds % 60
        minutes = total_minutes % 60
        hours = total_hours % 24  # Assume a 24-hour clock

        return Time(hours, minutes, seconds)

    def display(self):
        print(f"{self.hour:02}:{self.minute:02}:{self.second:02}")

hour1 = int(input("Enter hours for Time 1: "))
minute1 = int(input("Enter minutes for Time 1: "))
second1 = int(input("Enter seconds for Time 1: "))

hour2 = int(input("Enter hours for Time 2: "))
minute2 = int(input("Enter minutes for Time 2: "))
second2 = int(input("Enter seconds for Time 2: "))

time1 = Time(hour1, minute1, second1)
time2 = Time(hour2, minute2, second2)

time_sum = time1 + time2

print("\nSum of Times:")
time_sum.display()