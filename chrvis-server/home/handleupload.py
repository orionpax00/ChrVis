import os
import sys

def userauth(data):
    ##to do
    return None



def maketmplocation(data):
    data = data
    username = data['email'].split("@")[0]
    tmp_folder = "tmp/"+username
    tmp_location = os.path.join(str(os.system("pwd")),str(tmp_folder))


    #false will be repalce with tmp_location
    if False:
        message = {
            'message':"Your data exists",
            'isexist':True
        }
        return(message)
    else:
        # os.mkdir("tmp/"+username)
        # handledata(tmp_location)
        print("sdjsb")
