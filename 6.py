def is_leap(year):
   
    
    # Write your logic here
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap=False
        else:
             leap=True
    else:
        leap=False

    return leap



year = int(input())
