from flask import Flask, render_template, send_from_directory, send_file, redirect
import boto3
from config import access_key_id, secret_access_key, S3_BUCKET
from pathlib import Path


AWS_S3_SIGNATURE_VERSION = "s3v4"

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/yeah')
def yeah():
    return ('yeah')

@app.route('/filedrop/')
def indexoo():
    p =  Path(app.static_folder, 'files')
    filenames = [x.relative_to(app.static_folder) for x in p.iterdir() if x.is_file()]
    return render_template('files.html', **locals())


@app.route('/rail_mary/')
def hello_mary():
    return render_template('rail_mary.html')

@app.route('/return-files/')
def return_files_tut():
	try:
		return send_file('sean_wayland_oz_2023_chart_mp3.zip')
	except Exception as e:
		return str(e)

@app.route('/return-all_charts/')
def return_all_charts():
	try:
		return send_file('sean_wayland_pdfs_jan26_2022.zip')
	except Exception as e:
		return str(e)

@app.route('/return-skinny-files/')
def return_files_skinny():
        try:
                return send_file('skinny_dennis.zip')
        except Exception as e:
                return str(e)
        
@app.route('/return-plugins/')
def return_plugins():
        try:
                return send_file('plugins_2023.zip')
        except Exception as e:
                return str(e)

@app.route('/return_rail_mary_album/')
def return_rail_mary():
    """ resource: name of the file to download"""
    resource = "rail_mary_album_complete.zip"
    s3 = boto3.client('s3',
                      aws_access_key_id= access_key_id,
                      aws_secret_access_key= secret_access_key,
                      region_name="us-east-2"
                      )
    try:
        url = s3.generate_presigned_url('get_object', Params = {'Bucket': S3_BUCKET, 'Key': resource}, ExpiresIn = 1000)
    except Exception as e:
        return str(e)
    return redirect(url, code=302)

@app.route('/return_expanded_album/')
def return_expanded_ablum():
        try:
                return send_file('expanded_album.zip')
        except Exception as e:
                return str(e)

@app.route('/return-oz-charts/')
def return_oz_charts():
        try:
                return send_file('oz_jan_2024.zip')
        except Exception as e:
                return str(e)

