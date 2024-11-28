
class DAOException(Exception):
	def __init__(self, exc, message = None, data = None):
		self.exc = exc
		self.message = message
		self.data = data