import pyfiglet
import random
import explore
import keyboard
import time
from colorama import Fore
import os
import pygame
import json
from playsound import playsound
from threading import Thread

Reset = Fore.RESET
colors = [Fore.RED,Fore.GREEN,Fore.LIGHTGREEN_EX,Fore.BLUE,Fore.YELLOW]

paht = ''
joined_path = ''
trap = ''
over = False

def enemy():
    while True:
        global over
        if over == False:
            
            global joined_path
            path = os.getcwd()
            os.chdir(explore.home)
            joined_path = os.path.join(explore.home,explore.select_path())
            # print(joined_path)
            os.chdir(path)
            time.sleep(7)
        elif over == True:
            break


t = Thread(target=enemy)
t.start()

def chk():
    global joined_path
    global paht

    paht = os.getcwd()

    if paht == joined_path:
        print("you were shot by jhonny")
        return True
    
    else: return False


pygame.mixer.init()

TENSED = explore.music_path("music1")
Game = explore.music_path("music2")
WAITING = explore.music_path("music3")

playsound('soundEffects\\startup.wav')


def music_on_off(is_paused):

    if is_paused == False:
        
        pygame.mixer.music.stop()
    else :
        path = os.getcwd()
        os.chdir(explore.home)
        playsound('soundEffects\\Audio transition.wav')
        pygame.mixer.music.play(-1)
        os.chdir(path)
        
print("---x---"*20)
logo = "FUSIUC"
sublogo = "|||| Find US If U Can ||||"
random_color_1 = random.choice(colors)

print(random_color_1 + pyfiglet.figlet_format(logo,font='graffiti') + Reset)
print(random_color_1 + pyfiglet.figlet_format(sublogo,font='digital') + Reset)

print("---x---"*20)
print(f"Hello {explore.name()}")

os.chdir(explore.home)

pygame.mixer.music.load(Game)

music_on_off(True)



while True:
    
    def current():
        with open('settings.json','r') as f:
            data = json.load(f)
            print("current settings are(0:easy,false,1:hard,true):\n")
            print("timelimit: ", data["timelimit"])
            print("dificulty: ", data["dificulty"])
            print("applauseOnWin: " + str(data["applauseOnWin"]))
            print("music when in hub: ", data["music1"])
            print("music during gameplay: ", data["music2"])
            print("music during banner: ", data["music3"])
            print("*note* time is in secounds and for music paths u can use 'list music' command")

    com = input(Reset + "$ ").lower()


    if com == "play" :
        
        
        print("So do you want to start the Game?[press y for yes or press n]\n")

        while True:
            if keyboard.is_pressed('n'): exit()

            elif keyboard.is_pressed('y'):  break ; 

            else: continue 
        os.system('cls')

        print("OK")
        print("So let's start the Game")
        
        name = explore.select_filename()
        path = explore.select_path()

        def hint():
                        
            hint = str([int(i) for i in path.split('\\') if i.isdigit()]).replace('[','').replace(']','')

            with open('Data\\hint.txt','r') as f:
                f = f.read().split('\n')
                for i in f:
                    hintlist = i.split(':')
                    numhint = hintlist[0]
                    if hint == numhint:
                        
                        return hintlist[1]
                    
            

        hint = hint()

        explore.hide(name,path)
        os.chdir(explore.home)
        max_time = 60 * explore.time_limit()

        print("---x---"*20)
        print(colors[-1])
        print(f"now a file is hidden inside the directories folder and you have {max_time} secounds to find where it is")
        
        print("so let's start the timmer and now you can search and shoot it(excluding .txt)")
        
        print(Reset)
        print("---x---"*20)
        keyboard.press_and_release('backspace')
        
        start_time = time.time()

        pygame.mixer.music.load(TENSED)

        music_on_off(True)
        
        win = 'False'
        
        while time.time() < start_time + max_time:
            if chk() == True:
                win = 'ded'
                break
            else:
                # print(joined_path)
                command = input((colors[0] +"Command> " + colors[2]).lower())
                
            
                if command == 'quit' or command == 'exit':
                    print("Imagine quiting...")
                    print("          -must be you")
                    win = 'quited'
                    break

                elif command == 'ls':
                    print("Output> \n")
                    print(os.system('dir'))

                elif 'cd' in command:
                    try:
                        path = command.split(' ')[1]
                        os.chdir(path)
                        
                    except : print("Error")
                
                elif command == 'back':
                    os.chdir('..')
                
                elif command == 'hint':
                    print(f"Output> {hint}")

                elif command == 'home':
                    os.chdir(explore.home)

                elif command == 'pwd':
                    print(os.getcwd())
                
                elif command == 'music off':
                    music_on_off(False)
                elif command == 'music on':
                    music_on_off(True)

                elif 'shoot' in command:
                    try:
                        explore.shoot(command.split(' ')[1])
                        win = 'True'
                        break
                    except:
                        print("you shot air")
                        win = 'False'
                        continue
                
                elif command=="":
                    continue
                
                elif command=="help":
                    print(
                    '''
        1. cd: change directory
        2. ls: shows the content of the present working directory,remember i have not made it so you can see inside paths because that's not fun
        3. shoot: ofcourse shoots the file
        4. pwd: shows current working directory
        5. help: to ofcourse get help about the commands
        6. back: to step a directory back
        7. hint: to see the hint again incase it's in top
        8. music off: turns off the music
        9. music on: turns the music back on
        10. home: to go directly back to the home directory
        11. quit/exit: to exit the game , remember that u will exit only the game not the hub
                    ''')
                else: print(colors[0] + "#unknown command" + Reset); continue

        explore.Feture_shoot(path,name)

        music_on_off(False)

        if win == 'True':
            print("Congratulations you win")
            os.chdir(explore.home)
            playsound('soundEffects\\win.wav')
            explore.applause()
            pygame.mixer.music.load(Game)
            music_on_off(True)
        elif win == 'quited':
            os.chdir(explore.home)
            playsound('soundEffects\\Leftsound.mp3')
            print("ok no problem you can play afterwards ,or r u just scared to play it again?")
            pygame.mixer.music.load(Game)
            music_on_off(True)
        
        elif win == 'ded':
            os.chdir(explore.home)
            playsound('soundEffects\\game-over.wav')
            print("Gamers don't die they respawn")
            pygame.mixer.music.load(Game)
            music_on_off(True)

        elif win == 'False':
            os.chdir(explore.home)
            playsound('soundEffects\\game-over.wav')
            print("HAHA timeout , better luck next time sloth!")
            pygame.mixer.music.load(Game)
            music_on_off(True)
    elif com == 'quit' or com == 'exit':
        print("Thanks for playing")
        playsound('soundEffects\\Leftsound.mp3')
        over = True
    
        break
        

    elif com == 'banner':
        print("use ctrl+c to quit banner mode")
        time.sleep(2)
        os.chdir(explore.home)
        music_on_off(False)
        pygame.mixer.music.load(WAITING)
        music_on_off(True)
        try:
            os.system('python banner.py')

        except : os.system('cls') ; pygame.mixer.music.load(Game); music_on_off(True)

    elif com == 'gift' or com == 'prize':
        explore.Prize(explore.portscanner,'port-scanner')

    elif com == 'settings':
        current()
        print("To change the settings you can either edit the settings.json file or use 'change settings' command")
    
    elif com == 'list music':
        explore.list_music()

    elif com == 'change settings':
        current()
        setting = input("Enther the settings name: ")
        if 'music' in setting:
            explore.list_music()
            value = input("Enter your path")
            explore.change_settings(setting,value)
        
        else:
            def chki():
                if setting == "timelimit":
                    return "use minutes not secounds"
                elif setting == "dificulty":
                    return "either hard or easy i.e either 0 for easy or 1 for hard"
                elif setting == "applauseOnWin" :
                    return "either true or false"
                
            value = input(f"what value do you want to set ({chki()}):")

            explore.change_settings(setting,value)
    elif com == 'clear' :
        os.system('cls')
    
    elif com == 'credits':
        print("The creator of this Game is none other than mortalcoder")

    elif com == 'help game':

        print('''
    The Game is pretty simple, a file with a uncommon name will be hidden
    inside the subdirectories and directoriers in side the master directory 'dicts'
    and you need to find it and shoot it like a hunter

    the commands available inside the cli when the Game starts are as follows:

    1. cd: change directory
    2. ls: shows the content of the present working directory,remember i have not made it so you can see inside paths because that's not fun
    3. shoot: ofcourse shoots the file
    4. pwd: shows current working directory
        ''')


    elif com == 'help':
        
        print('''
    banner:to see my amazing banner
    quit/exit: to exit the cli
    play: ofcourse to play the Game
    credits: to see the credits
    settings: to see the settings 
    change settings: to change the settings
    list music: to see the music available with there respective path

        ''')

    
