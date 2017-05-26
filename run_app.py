import os
import shelve
import subprocess

#TODO:
#1)download all python packages
#2)Create emypty storage if it need it
#3)Create database file to track changes

def download_dependences():
    #check if dependencies not installed->install it
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])


def initialize_env():
    #create directory, where we will save storage
    #create db file->shelve lib
    if os.path.isdir('media'):
        print('directory "media" created')
    else:
        os.mkdir('media')


def run_application():
    from web_app import application
    application.app.run()

if __name__ == "__main__":
    download_dependences()
    initialize_env()
    run_application()
