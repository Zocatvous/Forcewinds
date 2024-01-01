#usage is commented in the main method:
#1. call the class 
#2. pass a string message of your choice
#3. choose a valid color
# NO ERROR HANDLING!
class Colorprint:
	def __init__(self, message,**kwargs):
		self.message = message
		self._flags = {"white":"\033[0;37;40m","blue":"\033[1;34;40m","green":"\033[1;32;40m","grey":"\033[1;30;40m","red":"\033[1;31;40m","bright_blue":"\033[1;34;40m"}
		self.colorflag = self._flags[kwargs.get('color','white')]
		self.revert = kwargs.get("revert",None)
		self.t_flag=""
		if self.revert == None:
			self.t_flag = self._flags["white"]
		print(f"{self.colorflag}{self.message}{self.t_flag}")

# if __name__ == "__main__":
# 	Colorprint("bluestring",color="blue")
# 	Colorprint("greenstring",color="green")
# 	Colorprint("whitestring")
