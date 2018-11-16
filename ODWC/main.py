
# Locations:
# [ ["pickup":pickup, "dropoff":dropoff, "time":time], ["pickup":pickup, "dropoff":dropoff, "time":time], ... ]

# Drivers:
# [ ["name":name, "loaciton":location], ["name":name, "loaciton":location], ... ]

# Find student closest in time
# Find driver that is shortest travel away
# assign

class Driver(object):
	""" Stores info about a driver """
	def __init__(self, name: str, start_location: str):
		self.name = name
		self.start_location = start_location
		self.busy = False
	
	def busy(self,value=None):
		if value == None:
			return self.busy
		self.busy = value

class Student(object):
	""" Stores data about a student """
	def __init__(self, pickup_location: str, dropoff_location: str, time_start: str):
		self.pickup = pickup_location
		self.dropoff = dropoff_location
		self.same_location = True if self.pickup == self.dropoff else False
		self.time = time_start

def parseLoactions(locations: list):
	for student in locations:
		yield Student(student["pickup"], student["dropoff"], student["time"])

def parseDrivers(drivers: list):
	for driver in drivers:
		yield Driver(driver["name"], driver["location"])

class Coordinator(object):
	""" Finds the best jobs for each driver """
	def __init__(self, locations: list, drivers: list):
		# Populate the arrays with objects
		self.students     = sorted(parseLoactions(locations))
		self.drivers      = sorted(parseDrivers(drivers))
		self.driver_count = len(drivers)
	
	def calculate(self) -> dict:
		output = {}
		# Fill output with drivers to schedule
		for driver in self.drivers:
			output[driver.name] = []
		
		# Sort students by priority
		self.students.sort(key=lambda x: x.time)
		
		hour = 0 # 0-24
		while hour <= 24:
			
			hour += 1
		return output
	

if __name__ == "__main__":
	locs = [{"pickup":"", "dropoff":"", "time":11}]
	driv = [{"name":"d1", "location":""}]
	t = Coordinator(locs, driv)
	print(t.calculate())