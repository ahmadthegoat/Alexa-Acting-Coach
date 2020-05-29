import os
#import PyAudio
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    i = 5
    tts = gTTS(text=text, lang="en")
    filename = str(i) + "l.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    i+=1 
    os.remove(filename)

    return text





def char_bible(name):
    lines = {}
    V=name.split("\n")
    for index, string in enumerate(V):

        if ">" in string or "<" in string:
            continue
        if string.isupper() and V[index-1] == "" and V[index+1] != "":
            if string not in lines:
                lines[string]= [V[index+1]]
            else:
                lines[string].append(V[index+1])
    for line in lines:
        print(line + "\n")
    question = input(speak(text = "\n \n Which character would you like to follow? "))
    for i in lines[question.upper()]:
        print(i + "\n")
        speak(text = i + "\n")
    path = input(speak(text="\nWould you like to continue?"))
    if path.lower =="yes":
        main()

def scene_bible(name):
    scenes = {}
    count = 0
    food = ""
    V=name.split("\n")
    scenes["SCENE " + str(count)] = []
    for index,line in enumerate(V):
        if "EXT." in line or "INT" in line:
            scenes["SCENE " + str(count) ].append(line)
            count+= 1
            scenes["SCENE " + str(count)] = []
        if "EXT." not in line or "INT" not in line:
            scenes["SCENE " + str(count)].append(line)
    for scene in scenes:
        print(scene + "\n")
    question= input(speak(text= "\n \n Which scene would you like to follow?, Include Scene "))
    print("\n".join(scenes[question.upper()]))
    speak(text="\n".join(scenes[question.upper()]))
    path = input(speak(text="\nwould you like to continue?"))
    if path.lower =="yes":
        main()


def read_screenplay(name):
    """Opens the named screenplay and returns its contents as a string.
    
    name -- String containing the correctly capitalized name of the screenplay.
    """
    filename = name + ".txt"
    f = open(filename)
    option = input(speak(text="Do you want to view a scene's lines or a character's lines? "))
    if option.lower() == "scene":
        scene_bible(name = f.read())
    else:
        if option.lower() == "character":
            char_bible(name = f.read())


def main():
    nem = ""
    speak(text="Hello User. Would You Like To Reherse Big Fish, Brick and Steel, or The Last Birthday Card: ")
    option = input("Hello User. Would You Like To Reherse Big Fish, Brick and Steel, or The Last Birthday Card: ")
    if option.lower() == "big fish":
        nem = read_screenplay(name = "Big Fish")
        
    elif option.lower() == "brick & steel":
        nem = read_screenplay(name = "Brick & Steel")
    else:
        if option.lower() == "the last birthday card":
            nem = read_screenplay(name = "The Last Birthday Card")
    
if __name__ == "__main__":
    main()
    
    
