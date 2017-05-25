from flask import Flask, request, render_template, redirect
import os
import shelve

app=Flask(__name__)
@app.route('/file', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        return render_template('file_1.html')

    if request.method == 'POST':
        book_data = {
            'name': request.form['book_name'],
            'writer': request.form['book_writer'],
            'price': request.form['book_price'],
        }
        with shelve.open(DBNAME) as db:
            if 'books' in db:
                db['books'] += [product_data]
            else:
                db['books'] = [product_data]

        file = request.files['book_image']
        file.save(os.path.join(app.config['MEDIA_BOOK'], os.path.basename(file.filename)))

        return redirect('/list-book')


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
    app.run(debug=True)
