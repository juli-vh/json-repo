from flask import Response
from flask import request, Flask, render_template, redirect
import shelve

app = Flask(__name__)
app.config['MEDIA_FOLDER'] = 'media'

DBNAME='shelve_lib'

def get_project_info():
    response_text = "<b>Hi. It's simple json repository based on Flask. Enjoy it.</b>"
    return Response(response=response_text,
                    status=200)


def get_storage_stat():
    return Response(response=[{'<path_to_file>:<tag>'}],
                    status=200,
                    mimetype="application/json")


def download_file(tag):
    #get file_content from request_obj
    if request.method == 'GET':
        filename = request.files['file_1.html']
        return filename
    if request.method=='POST':



    print(request)
    return Response(response="should be opened dialog to download file",
                    status=200)


@app.route('/upload', methods=['GET', 'POST'])
def upload_files(tag):
     if request.method == 'POST':
         f = request.files['file_1']
         f.save('/json_repository-master/uploads/uploaded_file.txt')

return Response(response="should upload file or files with specific tag")


def update_file(tag):
    #get file_content from request_obj
    return Response(response="should update file by specific tag")
