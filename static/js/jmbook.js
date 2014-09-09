$(function() {
	$(".content table").each(function() {
		var e = $(this);
		if(!e.hasClass("plain"))
			e.addClass("table table-striped");
	});
	// addClass("table-striped");
	// $(".content table").addClass("table");
});
