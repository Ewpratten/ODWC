
class Coordinator(object):
	""" Finds the best jobs for each driver """
	def __init__(self, locations: list, drivers: list):
		self.locations = locations
		self.drivers = drivers
		self.driver_count = len(drivers)
	
	
