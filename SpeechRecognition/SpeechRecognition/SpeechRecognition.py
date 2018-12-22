from Speech_AI import Speech_AI
import os


def main():
    ai = Speech_AI()
    if(ai.start() == True):
        clear = lambda: os.system('cls')
        clear()
        ai.work()

main()
