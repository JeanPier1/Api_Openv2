$("#enviar").click(function(){
	var tiempo= $('input#Tiempo').val();

	$.ajax({
		contentType: "application/json; charset=utf-8",        
		beforeSend: function(){
			$("#demo").html(`<img src="/video_recono/${tiempo}" width='100%' class="figure-img img-fluid rounded" >`);
		},
		dataType: 'json',
	});
});