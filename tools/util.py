import random, string, os, os.path

class Tool:
   
   def generatePassword():
        return "".join(random.choices(string.ascii_letters + string.digits, k=15))

