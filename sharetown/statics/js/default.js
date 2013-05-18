(function($) {

	$(function() {
	    if (window.File && window.FileList && window.FileReader) {
    	    Init();
    	}

    	$(".ensure").on('click', function(e) {
    		e.preventDefault();

    		if (confirm('Are you sure want to delete it?')) {
				window.location = $(this).prop('href');
    		}
    	});
	});

	$(document).foundation();

})(jQuery);
