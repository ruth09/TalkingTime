def time_talking(time):
    hours, minute = map(int, time.split(":"))

    if hours > 12:
        state = "pm"
        hours -= 12
    else:
        state = "am"
        pass

    talking_hours = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve')
    time_in_hours = talking_hours[hours - 1]

    print("it's " + time_in_hours, end=" ")

    minut = ""
    ones = ("one", "two", "three",
                "four", "five", "six",
                "seven", "eight", "nine")

    twos = ("ten", "eleven", "tweleve", "thirteen",
                 "fourteen", "fifteen", "sixteen",
                 "seventeen", "eighteen", "nineteen")

    tens = ("", "ten", "twenty", "thirty", "forty", "fifty")

    if minute in range(1,10):
        minut = "oh "+ones[minute-1]

    elif minute in range(10,20):

        minut = twos[minute-10]

    elif minute in range(20,60):
        on = minute % 10
        tw = minute // 10

        if tw in range(1, 10):
            minut = tens[tw]
        if on in range(1, 10):
            minut += ones[on-1]

    print(minut, state, sep=" ")


if __name__ == "__main__":
    sr = input("24hrs format eg: '12:00'")
    time_talking(sr)