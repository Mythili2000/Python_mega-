class date():


    @classmethod
    def is_valid_date(cls,year,month,day):
        if year < 1 or month < 1 or month > 12 or day < 1:
            return False
        else:
            return True

print(date.is_valid_date(2000,12,89))

