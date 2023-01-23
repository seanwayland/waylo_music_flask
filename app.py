from flask import Flask, render_template, send_from_directory, send_file, redirect
import boto3
from config import access_key_id, secret_access_key, S3_BUCKET

AWS_S3_SIGNATURE_VERSION = "s3v4"



app = Flask(__name__)




@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/return-files/')
def return_files_tut():
	try:
		return send_file('sean_wayland_oz_2023_chart_mp3.zip')
	except Exception as e:
		return str(e)

@app.route('/return-skinny-files/')
def return_files_skinny():
        try:
                return send_file('skinny_dennis.zip')
        except Exception as e:
                return str(e)

@app.route('/download_harry/')
def download_image():
    """ resource: name of the file to download"""
    resource = "mixes/funky harry mix 2.wav"
    s3 = boto3.client('s3',
                      aws_access_key_id= access_key_id,
                      aws_secret_access_key= secret_access_key,
                      region_name="us-east-2"
                      )
    try:
        url = s3.generate_presigned_url('get_object', Params = {'Bucket': S3_BUCKET, 'Key': resource}, ExpiresIn = 100)
    except Exception as e:
        return str(e)
    return redirect(url, code=302)

### OSX version 
if __name__ == '__main__':
    app.run(debug=True)

