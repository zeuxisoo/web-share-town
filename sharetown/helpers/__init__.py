import os
from flask import current_app

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in current_app.config.get('ALLOWED_EXTENSIONS')

def file_extension(filename):
	return '.' + filename.split('.')[-1]

def file_size(file_path):
	size = os.path.getsize(file_path)

	if size < 1024:
		size = str(size) + ".0 B"
	elif size < 1024 * 1024:
		size = "%0.1f KB" % (size/1024.0)
	elif size < 1024 * 1024 * 1024:
		size = "%0.1f MB" % (size/1024.0/1024.0)
	else :
		size = "%0.1f GB" % (size/1024.0/1024.0/1024.0)

	return size

def extension2icon():
	icons = {
		"head.png" : [".h"],
		"cpp.png"  : [".cpp", ".cxx", ".cc"],
		"c.png"    : [".c"],
		"cs.png"   : [".cs"],
		"html.png" : [".html"],
		"js.png"   : [".js"],
		"php.png"  : [".php"],
		"java.png" : [".java"],
		"py.png"   : [".py"],
		"rb.png"   : [".rb"],
		"as.png"   : [".as"],

		"pic.png"  : [".jpeg", ".jpg", ".png", ".gif"],
		"ai.png"   : [".ai"],
		"psd.png"  : [".psd"],

		"music.png": [".mp3"],

		"video.png": [".avi", ".rm", ".rmvb", ".mp4", ".wmv", ".mkv"],

		"word.png" : [".doc", ".docx"],
		"ppt.png"  : [".ppt", ".pptx"],
		"excel.png": [".xls", ".xlsx"],

		"zip.png"  : [".zip", ".tar", ".gz", ".7z", ".rar"],

		"pdf.png"  : [".pdf"],
		"txt.png"  : [".txt"],
		"exe.png"  : [".exe"],
		"apk.png"  : [".apk"]
	}

	ext2icon = dict()
	for icon, extensions in icons.items():
		for extension in extensions:
			ext2icon[extension] = icon

	return ext2icon

