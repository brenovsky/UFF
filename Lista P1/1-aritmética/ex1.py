seconds = int(input("input seconds: "))
minutes = seconds // 60
seconds = seconds % 60
hours = minutes // 60
minutes = minutes % 60
days = hours // 24
hours = hours % 24
print(f"{days} days, {hours} hours, {minutes} minutes and {seconds} seconds")