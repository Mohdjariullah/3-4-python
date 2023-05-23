class date:
    def __init__(self,a,b,c):
        self.d=a
        self.m=b
        self.y=c
    def day(self):
        print("Day is :",self.d)
    def month(self):
        print("Month is :",self.m)
    def year(self):
        print("Year is :",self.y)
    def monthname(self):
        months=["Unknown","January","Feburay","March","April","May","June","July","august","September","October","Novemnber","December"]
        print("Month name is :",months[self.m])
    def isleapyear(self):
        if self.y%400==0 and self.y%100==0:
            print("Is a leap year")
        elif self.y%4==0 and self.y%100!=0:
            print("IS a leap year")
        else:
            print("It s not a leap year")
d1=date(19,4,2024)
d1.day()
d1.month()
d1.monthname()
d1.year()
d1.isleapyear()
