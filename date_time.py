import time
import datetime
def ss(D):
    D_list = list(D)
    if(D_list[1]==1):
        return "st"
    elif(D_list[1]==2):
        return "nd"
    elif(D_list[1]==3):
        return "rd"
    else:
        return "th"
def main():
    Y = datetime.date.today().strftime("%Y")
    M = datetime.date.today().strftime("%B")
    D = datetime.date.today().strftime("%d")
    HH = datetime.datetime.now().strftime("%I")
    MM = datetime.datetime.now().strftime("%M")  
    print("Printed on the",D.lstrip('0')+ss(D),"day of",M+",",Y,"at",HH+":"+MM+".")
main()
