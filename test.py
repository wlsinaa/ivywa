def solve(haab_date: str) -> str:
    ddmmyyyy_L = haab_date.split()
    # day
    ddmmyyyy_L[0] = int(ddmmyyyy_L[0][0:-1])
    # month
    month_conv = {"pop":0, "no":1, "zip":2, "zotz":3, "tzec":4, "xul":5, "yoxkin":6, "mol":7, "chen":8, "yax":9, "zac":10, "ceh":11, "mac":12, "kankin":13, "muan":14, "pax":15, "koyab":16, "cumhu":17,"uayet":18}
    # year
    ddmmyyyy_L[2] = int(ddmmyyyy_L[2])
    passed_day = dayPass(ddmmyyyy_L[0], ddmmyyyy_L[1],ddmmyyyy_L[2],month_conv)
    print(passed_day)
    year_reminder = passed_day % (20*13)
    year_multiplier = passed_day // (20*13)
    month_reminder = year_reminder % 20
    month_multiplier = year_reminder // 20

    day_reminder = year_reminder % 13 + 1

    day_names_conv ={0: "imix", 1: "ik", 2: "akbal", 3: "kan", 4: "chicchan", 5: "cimi", 6: "manik", 7: "lamat", 8: "muluk", 9: "ok", 10: "chuen", 11: "eb", 12: "ben",13:  "ix", 14: "mem", 15: "cib", 16: "caban",17:  "eznab", 18: "canac", 19: "ahau"}
    year = year_multiplier
    month = day_names_conv.get(month_reminder)
    day = day_reminder
    print(str(day) + " " + month + " " + str(year))
    return str(day) + " " + month + " " + str(year)
def dayPass(dd,mm,yyyy, mm_conversion):
    day = dd
    mm = mm_conversion.get(mm) * 20
    yyyy = yyyy*365
    return dd + mm + yyyy

solve("10. zac 0")