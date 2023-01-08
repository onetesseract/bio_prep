total_mod = 24 * 60

out = []

record_hours = -1

a = 0
for a in range(0, 60):
    for b in range(0, 60):
        a_time = 0
        b_time = 0

        a_time += 60 + a
        b_time += 60 + b
        a_time = a_time % total_mod
        b_time = b_time % total_mod

        hours = 1

        while a_time != b_time:
            a_time += 60 + a
            b_time += 60 + b
            a_time = a_time % total_mod
            b_time = b_time % total_mod
            hours += 1
        
        record_hours = max(hours, record_hours)

        from math import floor

        hours = str(floor(a_time / 60))
        hours = hours if len(hours) == 2 else "0" + hours
        mins = str(a_time % 60)
        mins = mins if len(mins) == 2 else "0" + mins

        q = hours + ":" + mins
        if q != "00:00": out.append(b)

print(record_hours)