class Persons:
 def __init__(self):
  self.persons = []
  
 def add_person(self, person:str):
  self.persons.append({
   'name':person,
   'amount':''
  })
  
 def get_persons(self) -> list:
  return self.persons
 
 def delete_person(self, person: str):
  if person in self.persons:
   self.persons.remove(person)
  else:
   print('Person does not exist')
   

person = Persons()

addPersonPrompt = "Enter Person name (enter 'exit' to stop): "
personName = ''

while True:
 personName = input(addPersonPrompt)
 if personName == 'exit':
  break;
 
 try:
  person.add_person(personName)
 except:
  print("Error Occured")
  
for p in person.get_persons():
  print(p)