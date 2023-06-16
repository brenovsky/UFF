days = int(input("input days: "))
hours = int(input("input hours: "))
minutes = int(input("input minutes: "))
seconds = int(input("input seconds: "))
hours = days * 24 + hours
minutes = hours * 60 + minutes
seconds = minutes * 60 + seconds
print(f'{seconds} seconds')