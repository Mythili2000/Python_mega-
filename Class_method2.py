class person():
    @classmethod
    def claculate_age(cls,birth_year):
        cls.today_year = 2023
        cls.age = cls.today_year - cls.birth_year

print(person.claculate_age(2000))
