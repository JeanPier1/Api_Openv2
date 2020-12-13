$(function(){
	$('.get-started-btn').click(function(){
		var user = $('#correo').val();
        var pass = $('#Contraseña').val();
		$.ajax({
			url: '/api/auth/login',
            type: 'POST',
            dataType: "json",
			contentType: "application/json; charset=utf-8",
			data: JSON.stringify({correo: `${user}`, "contrasena":`${pass}`}),
			headers: { Authorization: $`Bearer ${localStorage.getItem("token")}` },
			success: function(response){
				if(response.token!=undefined){
					localStorage.setItem("token",response.token)
					inicir_login(response.token)
				}
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});

function inicir_login(token){
	$.ajax({
		headers: { "Authorization": 'Bearer '+localStorage.getItem("token")+''},
		url : '/app',
		type: 'GET',
		accepts: "application/json",
		success: function(response){
			if(response!=undefined){
				
				window.location=response
			}
		},
	});

}