### This is a calculator that improves on the initial leap year calc by returning the days in a select month within a year using a function. ###


def is_leap(year):
    #calculate whether the input (year) is a leap year across 3 checks
    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          return(True)
        else:
          return(False)
      else:
        return(True)
    else:
      return(False)

def days_in_month(year_input, month_input):
    #considers leap year to calculate days in a chosen month of a chosen year
    year_rtn = is_leap(year)
    if year_rtn == True:
        month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return(month_days_leap[(month-1)])
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return(month_days[(month-1)])
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
