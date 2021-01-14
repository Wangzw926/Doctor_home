 document.getElementById("field").addEventListener("change", function(){
	  	var files = this.files;
	  	var file;
	  	if (files && files.length) {
	  	  file = files[0];
	  	  if (/^image\/png$|jpeg$/.test(file.type)) {
	  	    document.getElementById('view').src = URL.createObjectURL(file);
	  	  } else {
	  	    alert("请选择一张照片(jpg/jpeg/png.)");
	  	  }
	  	} else {
	  	  alert("请选择照片文件");
	  	}
	    }, false);