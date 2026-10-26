def time_string(hours, minutes, time_format):
    if time_format == '12':
        if hours == 0:
            hours = 12
            period = 'AM'
        elif hours < 12:
            period = 'AM'
        elif hours == 12:
            period = 'PM'
        else:
            hours -= 12
            period = 'PM'
        return f"{hours:02d}:{minutes:02d} {period}"
    elif time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    else:
        raise ValueError("Invalid time format. Use '12' or '24'.")

print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))