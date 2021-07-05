import os
import json

path = os.path.join(os.getcwd(),"dicts")
name1 = 'a'
name2 = 'b'

for i in range(21):
    try:
        os.makedirs(os.path.join(os.path.join(path,str(i)),name1))
        os.makedirs(os.path.join(os.path.join(path,str(i)),name2))
    except :
        pass

name = input("kindly enter your game name: ")

with open('profile.json','r') as f:

    data = json.load(f)
    f.close()
data["name"] = name

with open('profile.json','w') as w:
    json.dump(data,w)
    w.close

print(f"Name assigned as {name}")