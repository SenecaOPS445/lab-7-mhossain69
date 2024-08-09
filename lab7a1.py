#!/usr/bin/env python3

from lab7a import Time, sum_times, format_time

def main():
    t1 = Time(8, 0, 0)
    t2 = Time(8, 55, 0)
    t3 = Time(9, 50, 0)
    td = Time(0, 50, 0)

    tsum1 = sum_times(t1, td)
    tsum2 = sum_times(t2, td)
    tsum3 = sum_times(t3, td)

    print(f"Time 1: {format_time(t1)}")
    print(f"Time 2: {format_time(t2)}")
    print(f"Time 3: {format_time(t3)}")
    print(f"Time Difference: {format_time(td)}")
    print(f"Sum 1: {format_time(tsum1)}")
    print(f"Sum 2: {format_time(tsum2)}")
    print(f"Sum 3: {format_time(tsum3)}")

if __name__ == "__main__":
    main()
