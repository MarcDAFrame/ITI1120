def is_eligible(age, citizen, prison):
     if age >=18 and citizen.lower() in ["canada", "canadian"] and prison.lower() == "no":
          return True
     else:
          return False
     
name=input("What is your name? ")
age= int(input("How old are you? "))
citizen = input("where are you a citizen of? ")
prison = input("are you currently in prison convicted for a criminal offence.? (yes or no) ")


if is_eligible(age, citizen, prison):
     print(name, ", you are eligible to vote")
else:
     print(name, ", you are ineligible to vote") 
    



          
