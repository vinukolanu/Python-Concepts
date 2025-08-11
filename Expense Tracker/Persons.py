class Persons:
 def __init__(self):
  self.persons = []
  
 def add_person(self, person:str, phone:int):
  self.persons.append({
   'name':person,
   'amount':'',
   'mobile':phone
  })
  
 def get_persons(self) -> list:
  return self.persons
 
 def delete_person(self, phone: str):
  if person in self.persons:
   self.persons.remove(phone)
  else:
   print('Person does not exist')
   

person = Persons()

addPersonPrompt = "Enter Person name (enter 'exit' to stop): "
addPersonPhoneNumber = "Enter phone number: "
personName = ''
personPhoneNumber = 0
while True:
 personName = input(addPersonPrompt)
 personPhoneNumber = int(input(addPersonPhoneNumber))
 if personName == 'exit' or personPhoneNumber == 0:
  break;
 
 try:
  person.add_person(personName, personPhoneNumber)
 except:
  print("Error Occured")
  
for p in person.get_persons():
  print(p)