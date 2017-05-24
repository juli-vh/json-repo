from flask import Flask, request, render_template, redirect
import os
import shelve

app=Flask(__name__)
@app.route('/file', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        return render_template('file_form.html')

    elif request.method =='POST':
        file=request.files['file_input']

        print(request.form['filetag'])
        print(file.filename)

        filepath = os.path.join('media', file.filename)
        file.save(filepath)




    return redirect ('/file')

if __name__=='__main__':
    app.run(debug=True)


#TODO:
#1)download all python packages
#2)Create emypty storage if it need it
#3)Create database file to track changes

def download_dependences():
    #check if dependencies not installed->install it
    pass


def initialize_env():
    #create directory, where we will save storage
    #create db file->shelve lib
    pass

def run_application():
    from web_app import application
    application.app.run()

if __name__ == "__main__":
    download_dependences()
    initialize_env()
    run_application()
