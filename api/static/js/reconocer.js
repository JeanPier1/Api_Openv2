$("#enviar").click(function(){
	var tiempo= $('input#Tiempo').val();

	$.ajax({
		url:"/tiempo",
		type:"POST",
		dataType: 'json',
		contentType: "application/json; charset=utf-8",
		data : JSON.stringify({"tiempo":tiempo}),
		headers: { "Authorization": 'Bearer '+localStorage.getItem("token")+''},
		success:function(response){
			if(response!=null){
				$("#demo").html(`<img src="/video_recono/${response}" width='100%' class="figure-img img-fluid rounded" >`);
			}
			setTimeout(function(){ location.reload(); }, 65*response);
		}
	});
});