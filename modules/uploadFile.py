from flask import Blueprint, request

fileUpload_api = Blueprint('fileUpload_api', __name__)


@fileUpload_api.route("/uploadFile", methods = ['POST'])
def upload_file():
    if request.files: #Form data
        f = request.files['myfile']
        print(request.files['myfile'].read())

    elif request.get_data(): #Binary data
        print(request.get_data())

    return 'file uploaded successfully'
