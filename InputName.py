class Person:

     def __init__(self, firstname, lastname):
         self.firstname = firstname
         self.lastname = lastname

     def show_full_name(self):
         return self.firstname + ' ' + self.lastname

     @classmethod
     def get_user_input(self):
         while 1:
             try:
                 firstname = input('Enter first name: ')
                 lastname = input('Enter last name')
                 return self(firstname,lastname)
             except:
                 print('Invalid input!')
                 continue


person3 = Person.get_user_input()
person3.show_full_name()
