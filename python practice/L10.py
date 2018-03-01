#Robert Schreibman
#csci250 - sensors
#2-27-18
#L10

#Creates a class called fox
class Fox:
        #constructor with default parameters "male", "white", 6, 11, False
	def __init__(self, gender="male", color="white", age=6, size=11, hungry=False):
		self.gender=gender
		self.color=color
		self.age=age
		self.size=size
		self.hungry=hungry

	#member function that will print the member variables of a Fox instance
	def print_profile(self):
		print("gender:",self.gender)
		print("color:",self.color)
		print("age:",self.age)
		print("size:",self.size)
		print("hungry:",self.hungry)

        #member function that returns the member variable hungry of an instance
	def is_fox_hungry(self):
		return self.hungry

	#member function that returns a boolean to see if fox is a female
	def is_fox_female(self):
		if self.gender=="male":
			return False
		else:
			return True

        #changes member variable age (of an instance) according to number of years given
	def update_age(self, years):
                self.age = self.age + years

               
tommy = Fox("male", "blue", 8, 12, True)        #create instance of Fox class called tommy 
                                                #while initializing member variables

tommy.print_profile()                           #access member functions of instance tommy
tommy.is_fox_hungry()
tommy.is_fox_female()
tommy.update_age(2)
print()
tommy.print_profile()
print()

natalie = Fox("Female","white", 7)              #create another instance of Fox class called natlie
                                                #setting 3 member variables & using the default values
                                                #for the rest
natalie.print_profile()
