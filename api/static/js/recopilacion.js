$("#enviar").click(function(){
	var nombre= $('input#nombreuni').val();
    var codigo_uni=$('input#codigo_uni').val();

	$.ajax({
		url:"/datos",
		type:"POST",
		dataType: 'json',
		contentType: "application/json; charset=utf-8",
		data : JSON.stringify({"nombre":nombre, "codigo_uni":codigo_uni}),
		headers:{"Authorization":'Bearer '+localStorage.getItem("token")+''},   
		success:function(response){
			$("#demo").html(`<img src="/guardar_rostro/${response['codigo_uni']}/${response['nombre']}" width='100%' class="figure-img img-fluid rounded">`);
			setTimeout(function(){ location.reload(); }, 35067);
		}
		// beforeSend: function(){
		// 	$("#demo").html(`<img src="/guardar_rostro/${codigo_uni}/${nombre}" width='100%' class="figure-img img-fluid rounded">`);
		// },
	});
});