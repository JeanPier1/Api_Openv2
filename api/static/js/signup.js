Lobibox.base.DEFAULTS = $.extend({}, Lobibox.base.DEFAULTS, {
    iconSource: 'fontAwesome'
});
Lobibox.notify.DEFAULTS = $.extend({}, Lobibox.notify.DEFAULTS, {
    iconSource: 'fontAwesome'
});

$(function(){
	$('.get-started-btn').click(function(){
		var user = $('#correo').val();
        var pass = $('#Contraseña').val();

		if(user!= null && pass!= null && user!= undefined && pass!= undefined && user!= "" && pass!= "" ){

			if($("#correo").val().indexOf('@', 0) == -1 || $("#correo").val().indexOf('.', 0) == -1) {
				Lobibox.notify('error', {
					msg: 'Error en el campo de correo'
				});
			}else{
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
							setTimeout(function(){ inicir_login(response.token); }, 8000);
							Lobibox.notify('success', {
								msg: 'Iniciaste Session'
							});
						}else{
							Lobibox.notify('error', {
								msg: 'Contraseña o Correo Incorrecto'
							});
						}	
					},
					error: function(error){
						Lobibox.notify('error', {
							msg: 'Erro'
						});
					}
				});
			}
			
		}else {
			Lobibox.notify('error', {
				msg: 'Campos Incompletos para iniciar sesion'
			});
		}
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