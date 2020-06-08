
import sys
import time


def check ():
    count = 11
    massiv = ["[", 9, 19, 29, 39, 49, 59, 69, 79, 89, "]"]
    for i in massiv:

        if i == "[" :
            print("[",end="")


        elif i == "]" :
            print("]", end="")
            break

        else:
            time.sleep(0.3)
            print(count+i ,end="% ")

def programm():
    cout = input()


def main_program ():
    #programm()
    check()

main_program()


