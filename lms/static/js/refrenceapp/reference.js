(function($, _) {
    'use strict';

    $('#btnsubmit').click(function() {
	$.ajax({
	    url: '/reference/create',
	    data: $('form').serialize(),
	    dataType: 'json',
	    type: 'POST',
	    success: function(response) {
			alert(response.msg)
			console.log(response)
			location.href = "http://0.0.0.0:8000/reference/"
	    },
	    error: function(err) {
	    	alert(err.msg)
			console.log(err);
	    }
	});
    });

    $('#btnupdate').click(function() {
	var id = $('#hf').val();
		$.ajax({
	    url: '/reference/edit/'+id,
	    data: $('form').serialize(),
	    dataType: 'json',
	    type: 'POST',
	    success: function(response) {
		alert(response.msg)
			console.log(response)
			location.href = "http://0.0.0.0:8000/reference/"
	    },
	    error: function(err) {
	    	alert(err.msg)
			console.log(err);
	    }
	});


    });

    $('#btnremoveref').click(function() {
	var id = $('#hf').val();
	$.ajax({
	    url: '/reference/delete/'+id,
	    data: $('form').serialize(),
	    type: 'POST',
	    success: function(response) {
		console.log(response);
	    },
	    error: function(error) {
		console.log(error);
	    }
	});
    });

})(jQuery, _);
