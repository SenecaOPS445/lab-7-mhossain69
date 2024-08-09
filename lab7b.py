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

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time(0, 0, 0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum
