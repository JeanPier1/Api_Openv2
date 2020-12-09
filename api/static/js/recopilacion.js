$("#enviar").click(function(){
	var nombre= $('input#nombreuni').val();
    var codigo_uni=$('input#codigo_uni').val();

	$.ajax({
		contentType: "application/json; charset=utf-8",        
		beforeSend: function(){
			$("#demo").html(`<img src="/guardar_rostro/${codigo_uni}/${nombre}" width='100%' class="figure-img img-fluid rounded">`);
		},
		dataType: 'json',
	});
});