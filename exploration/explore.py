import random
import os
import json
import playsound
from time import sleep

portscanner = "https://github.com/mortalcoder/port-scanner/"

easypaths = []
paths = []

home = os.getcwd()

settings = os.path.join(os.getcwd(),'settings.json')

with open('Data\\easypath.txt', 'r') as f:
    easypaths = f.readlines()

with open('Data\\path.txt','r') as p:
    paths = p.readlines()



def select_filename():
    
    with open('Data\\filenames.txt') as f:
        name = random.choice(f.read().splitlines())
        
    return name
        

def select_path():

    with open(settings, 'r') as f:

        data = json.load(f)

        if data["dificulty"] == 1:

            with open('Data\\path.txt', 'r') as f:
                path = random.choice(f.read().splitlines())
            
            return path

        elif data["dificulty"] == 0:

            with open('Data\\easypath.txt', 'r') as f:
                path = random.choice(f.read().splitlines())
            
            return path

def select_enemy_path(player):
    path = os.getcwd()
    os.chdir(home)

    with open(settings, 'r') as f:

        data = json.load(f)

        if data["dificulty"] == 1:
            thing =  os.path.join(home,random.choice(paths))
            if thing != player:
                os.chdir(path)
                return thing
            else: select_enemy_path(player)

        elif data["dificulty"] == 0:
            thing =  os.path.join(home,random.choice(easypaths))
            if thing != player:
                os.chdir(path)
                return thing
            else: select_enemy_path(player)
                

def hide(name,path):
    try:
        os.chdir(path)
        with open(name,'w') as f:
            
            f.close()

        os.chdir(home)
    except :
        hide(name,path)

def shoot(name):
    
    path = os.getcwd()
    if ".txt" in name:
        path = os.path.join(path, name)

        os.remove(path)

    elif ".txt" not in name:
        path = os.path.join(path, name+'.txt')

        os.remove(path)

def Feture_shoot(path,name):
    try:

        path = os.path.join(path, name)

        os.remove(path)

    except : pass

def applause():

    with open(settings,'r') as f:
        data = json.load(f)

        if data["applauseOnWin"] == False:

            pass

            
        elif data["applauseOnWin"] == True:

            path = os.getcwd()

            os.chdir(home)
            
            playsound.playsound("soundEffects\\applause.wav")
            os.chdir(path)

def change_settings(setting,value):

    if setting == "dificulty" and int(value) in range(2):
        with open(settings,'r') as f:
            data = json.load(f)
            
            f.close()

        data[setting] = int(value)

        with open('settings.json','w') as w:
            json.dump(data, w)
            w.close
        
        print("Setting changed successfully!")
    

    elif setting == "timelimit":
        with open(settings,'r') as f:
            data = json.load(f)
            
            f.close()

        data[setting] = float(value)

        with open(settings,'w') as w:
            json.dump(data, w)
            w.close
        
        print("Setting changed successfully!")

    elif "music" in setting:
        
        with open('settings.json','r') as f:
            data = json.load(f)
            
            f.close()

        data[setting] = value

        with open('settings.json','w') as w:
            json.dump(data, w)
            w.close

        print("Setting changed successfully!")
    
    elif setting == "applauseOnWin":
        with open('settings.json','r') as f:
            data = json.load(f)
            
            f.close()

        if value == 'false':
            value = False

        elif value == 'true':
            value = True

        data[setting] = value

        with open('settings.json','w') as w:
            json.dump(data, w)
            w.close
        
        print("Setting changed successfully!")

    else:
        print("error")
        
def music_path(name):

    with open('settings.json','r') as f:
        data = json.load(f)

        return data[name]

def list_music():
    print("music lists>")
    print("[0]: music\\Background_music.mp3")
    print("[1]: music\\Game-music.mp3")
    print("[2]: music\\Waiting-Music.mp3")
            
def name():
    with open('profile.json','r') as f:
        data = json.load(f)

        return data["name"]

def time_limit():

    with open('settings.json','r') as f:
        data = json.load(f)

    return data["timelimit"]

def Prize(link,name):

    print("Thank you for playing , here's a gift for you")
    print("you will get a tool that i made\n")
    print(f'''
 ________________________________________________________________________
|        Name         |         link                                     |
|     {name}    |   {link}   |
|_____________________|__________________________________________________|
    ''')
    

# hide(select_filename(),select_path())
# shoot('why','directories\\15\\a')

# download(first_win_gift[0],'port-scanner')
# download(first_win_gift[],'port-scanner')
# Prize(portscanner,'portscanner')
# change_settings("dificulty",1)
# while True:
#     print(select_path())
#     time.sleep(0.4)
# applause()
# change_settings('applauseOnWin','false')
# Prize(portscanner ,'port-scanner')