import re

def main():
    print(convert(input("Hours: ")))

def convert(time):
                                #1            #2          #3           #4            #5           #6
    matches = re.search(r"^([0-1]?[0-9])(\:[0-5][0-9])? (AM|PM) to ([0-1]?[0-9])(\:[0-5][0-9])? (AM|PM)$", time)

    if matches:
        time_one = get_format(matches.group(1), matches.group(3)) + exist(matches.group(2))
        time_two = get_format(matches.group(4), matches.group(6)) + exist(matches.group(5))
        return time_one + " to " + time_two
    else:
        raise ValueError()

def exist(sub):
    if sub:
        return sub
    else:
        return ":00"

def get_format(time, type):
    # Get conversion list for AM
    AM = {
        "12":"00","1":"01","2":"02","3":"03",
        "4":"04","5":"05","6":"06","7":"07",
        "8":"08","9":"09","10":"10","11":"11"
    }

    # Get conversion list for PM
    PM = {
        "12":"12","1":"13","2":"14","3":"15",
        "4":"16","5":"17","6":"18","7":"19",
        "8":"20","9":"21","10":"22","11":"23",
    }

    if type == "AM":
        return AM[time]
    else:
        return PM[time]

if __name__ == "__main__":
    main()
