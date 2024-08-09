#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object with validation"""
        if not self.valid_time(hour, minute, second):
            raise ValueError("Invalid time format")
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def valid_time(hour, minute, second):
        """Check for the validity of the time attributes"""
        if hour < 0 or minute < 0 or second < 0:
            return False
        if minute >= 60 or second >= 60 or hour >= 24:
            return False
        return True

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

def change_time(t, seconds):
    """Change time by adding a number of seconds to the time object"""
    t.second += seconds

    # Handle overflow of seconds
    if t.second >= 60:
        t.minute += t.second // 60
        t.second %= 60

    # Handle overflow of minutes
    if t.minute >= 60:
        t.hour += t.minute // 60
        t.minute %= 60

    # Handle overflow of hours
    if t.hour >= 24:
        t.hour %= 24

    return t

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum_hour = t1.hour + t2.hour
    sum_minute = t1.minute + t2.minute
    sum_second = t1.second + t2.second

    if sum_second >= 60:
        sum_minute += sum_second // 60
        sum_second %= 60

    if sum_minute >= 60:
        sum_hour += sum_minute // 60
        sum_minute %= 60

    return Time(sum_hour, sum_minute, sum_second)
