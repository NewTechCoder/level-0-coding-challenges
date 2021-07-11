def number_to_time(number):
    hour = number // 60
    minute = number % 60

    if hour == 1 and minute == 1:
        print(f"{hour} hour, {minute} minute.")
    elif hour > 1 and minute > 1:
        print(f"{hour} hours, {minute} minutes.")
    elif hour == 1 and minute > 1:
        print(f"{hour} hour, {minute} minutes.")
    elif hour > 1 and minute == 1:
        print(f"{hour} hours, {minute} minute.")

if __name__ == "__main__":
    number_to_time(71)
    number_to_time(133)
