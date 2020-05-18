# import datetime
from datetime import datetime
from datetime import date


# Complete datetime with default formatting
now = datetime.now()
# print(now)

# 
current = date.today()
# print(current)


# Calculate age depending on month of birth.
# If month of birth is >= 6, remove one year form current year
def optimistic_age(birth_year = False, birth_month = False):

    current_year = current.year
    current_month = current.month
    
    if (birth_month - current_month >= 6):
        current_year -= 1
  
    return f"Your optimistic age is: {current_year - birth_year}"



print( optimistic_age(1966, 10) )