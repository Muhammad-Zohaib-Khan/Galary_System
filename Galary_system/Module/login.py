import json
import os
import sys
sys.path.insert(1,os.getcwd())
from definition import *

class Login:
    def __init__(self):
        pass

    def get_credientail(self):
        with open("data/crediential.json","r") as f:
            data=json.load(f)
        return data["credentials"]
    
    def login(self,username,password):
        credentail=self.get_credientail()
        for user,values in credentail.items():
            if (values["user"]==username and values['password']==password):
                return {"type":values["type"],"result":True}
        return False
    def logout(self):
        return True
   
b=Login()
print(b.login("user","user"))