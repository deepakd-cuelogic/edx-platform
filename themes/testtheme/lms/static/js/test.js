/**
 * custom js utility.
 */

(function($, _) {
    'use strict';

    $(document).ready(function() {
	console.log("Called inside test.js file!!!")

	$("#global-navigation").on("click", "#btn-3", function () {
	    alert("Hi You Clicked on PressButton-3!!!");
	    console.log("Inside!!!!!!! BTN-3!!!!")
	});

	$("#global-navigation").on("click", "#btn-4", function () {
	    alert("Hi You Clicked on PressButton-4!!!");
	    console.log("Inside!!!!!!! BTN-4!!!!")
	});

	$("#global-navigation").on("click", "#btn-5", function () {
	    alert("Hi You Clicked on PressBtn-5 Button!!!");
	    console.log("Inside!!!!!!! BTN-5!!!!")
	});

    });

})(jQuery, _);
