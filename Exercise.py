class bangalore:
    name = ""
    soft_drinks = ""
    fresh_juice = ""
    def party(self):
        print("Lets party......!")
    def siteview(self):
        print("Enjoying the site seeing!!")
mythili = bangalore()
manoj = bangalore()
mythili.name = "Mythili"
manoj.name = "Manoj"
mythili.soft_drinks = "No"
mythili.fresh_juice = "Yes"
manoj.soft_drinks = "Yes"
manoj.fresh_juice = "No"
print(mythili.name)
print("drink fresh_juice:",mythili.fresh_juice)
print(manoj.name)
print("drink fresh_juice:",manoj.fresh_juice)
print(manoj.party())
print(mythili.siteview())
