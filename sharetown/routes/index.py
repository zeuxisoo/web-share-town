import os
from datetime import datetime
from urllib import quote
from flask import Blueprint
from flask import current_app
from flask import render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
from ..helpers import allowed_file, file_extension, file_size, extension2icon

blueprint = Blueprint("index", __name__)

@blueprint.route('/', methods=['GET','POST'])
def index():
	upload_root = os.path.join(os.getcwd(), current_app.config.get('UPLOAD_FOLDER'))

	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(upload_root, filename))
			flash('Upload file: {0}'.format(file.filename.encode("utf-8")), 'success')
		else:
			flash('Can not upload file {0}'.format(file.filename.encode("utf-8")), 'error')

		return ""
	else:
		files = []
		items = os.listdir(upload_root)
		items = sorted(items, key=str.lower)

		icons = extension2icon()

		for item in items:
			if item[0] == '.' or os.path.isdir(os.path.join(upload_root, item)):
				continue
			else:
				info = {}
				info["name"]      = item
				info["extension"] = file_extension(item).replace(".", "")
				info['icon']      = icons.get(file_extension(item), "default.png")
				info["time"]      = datetime.fromtimestamp(os.path.getmtime(os.path.join(upload_root, item)))
				info["size"]      = file_size(os.path.join(upload_root, item))
				info["encode"]    = quote(item)

				files.append(info)

		return render_template('index.html', files=files)

@blueprint.route('/download/<filename>')
def download(filename):
	upload_root = os.path.join(os.getcwd(), current_app.config.get('UPLOAD_FOLDER'))
	file_path   = os.path.join(upload_root, filename)

	if os.path.exists(file_path):
		return send_file(file_path, as_attachment=True, attachment_filename=filename.replace("_", " "))
	else:
		flash('Can not found the file {0}'.format(filename), 'error')
		return redirect(url_for('index.index'))

@blueprint.route('/delete/<filename>')
def delete(filename):
	upload_root = os.path.join(os.getcwd(), current_app.config.get('UPLOAD_FOLDER'))
	file_path   = os.path.join(upload_root, filename)

	if os.path.exists(file_path):
		os.remove(file_path)

		flash('Deleted file: {0}'.format(filename), 'deleted')
	else:
		flash('Can not found the file: {0}'.format(filename), 'error')

	return redirect(url_for('index.index'))
