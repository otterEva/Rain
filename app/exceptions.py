class DAOException(Exception):
	def __init__(self, message: str) -> None:
		self.message = message
	
	def __str__(self) -> str:
		return self.message
	
	def __repr__(self) -> str:
		return self.message 
	
class ServiceException(Exception):
	def __init__(self, message: str) -> None:
		self.message = message
	
	def __str__(self) -> str:
		return self.message
	
	def __repr__(self) -> str:
		return self.message