function DragFileHover(e) {
	e.stopPropagation();
	e.preventDefault();
	e.target.className = (e.type == "dragover" ? "drag-file-hover" : "drag-file");
}

function uploadProgress(evt) {
	if (evt.lengthComputable) {
		var uploaded = Math.round(evt.loaded * 100 / evt.total);
		$("#upload_progress").show();
		$("#upload_progress_bar").attr("style","width:" + uploaded + "%;")
	}else{
	}
}

function FileSelectHandler(e) {
	DragFileHover(e);

	var files = e.target.files || e.dataTransfer.files;
	var xhr   = new XMLHttpRequest();

	xhr.open('post', '/', true);
	xhr.upload.addEventListener("load", function(e) {
		setTimeout(function() {
			window.location.reload()
		}, 800);
	}, false);
	xhr.upload.addEventListener("progress", uploadProgress, false);

	var formData = new FormData();

	for (var i = 0, f; f = files[i]; i++) {
		var entry = e.dataTransfer.items[i].webkitGetAsEntry();
		if (entry.isFile) {
			formData.append('file', f);
		}else{
			alert("Not support upload folder");
			return;
		}
	}

	xhr.send(formData);
}

function Init() {
	var dragfile = $(".drag-file").eq(0)[0];
	var xhr = new XMLHttpRequest();

	if (xhr.upload) {
		dragfile.addEventListener("dragover", DragFileHover, false);
		dragfile.addEventListener("dragleave", DragFileHover, false);
		dragfile.addEventListener("drop", FileSelectHandler, false);
		dragfile.style.display = "block";
	}
}
