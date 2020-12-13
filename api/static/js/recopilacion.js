Lobibox.base.DEFAULTS = $.extend({}, Lobibox.base.DEFAULTS, {
    iconSource: 'fontAwesome'
});
Lobibox.notify.DEFAULTS = $.extend({}, Lobibox.notify.DEFAULTS, {
    iconSource: 'fontAwesome'
});
$('#enviar').click(function () {
    Lobibox.confirm({
        msg: "¿Tienes los datos correctos?",
        callback: function ($this, type) {
            if (type === 'yes') {
                
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
						if(Object.keys(response).length==0){
							 Lobibox.notify('error', {
								msg: 'Datos enviados son incorrectos no registrados'
							});
						}else{
							Lobibox.notify('success', {
								msg: 'Mire la camara por 1 minuto'
							});
							$("#demo").html(`<img src="/guardar_rostro/${response['codigo_uni']}/${response['nombre']}" width='100%' class="figure-img img-fluid rounded">`);
							Lobibox.progress({
								title: 'Por favor espere',
								label: 'Recopilando para Inteligencia Artificial Facial',
								progressTpl : '<div class="progress lobibox-progress-outer">\n\
											<div class="progress-bar progress-bar-danger progress-bar-striped lobibox-progress-element" data-role="progress-text" role="progressbar"></div>\n\
											</div>',
								onShow: function ($this) {
										var i = 0;
										var inter = setInterval(function () {
											if (i > 100) {
												inter = clearInterval(inter);
											}
											i = i + 0.1;
											$this.setProgress(i);
										}, 90);
									}
								});
							setTimeout(function(){ 
								Lobibox.notify('success', {
									msg: 'Modelo almacenado'
								});
								location.reload(); }, 96000);
						}
					},
					error:function(jqXHR, textStatus, errorThrown){
						Lobibox.notify('error', {
							msg: 'No se realizo el expiracion Token o valores erroneos. Estado: '+textStatus+''
						});
					}					
				});
            } else if (type === 'no') {
                Lobibox.notify('error', {
                    msg: 'Se anulo el enviado'
                });
            }
        }
    });
});