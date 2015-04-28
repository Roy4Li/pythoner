class MyClass:
	name = 'Sam'
	def sayHi(self):
		print 'Hello %s' % self.name
		
class car:
	speed = 1
	def drive(self,distance):
		time = distance / self.speed
		print 'it takes %.1f hour to drive' % time

car1 = car()
car1.speed = 60
car1.drive(120.0)

