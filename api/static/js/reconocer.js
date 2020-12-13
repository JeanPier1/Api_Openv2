Lobibox.base.DEFAULTS = $.extend({}, Lobibox.base.DEFAULTS, {
    iconSource: 'fontAwesome'
});
Lobibox.notify.DEFAULTS = $.extend({}, Lobibox.notify.DEFAULTS, {
    iconSource: 'fontAwesome'
});


var defaults = {
	calendarWeeks: true,
	showClear: true,
	showClose: true,
	allowInputToggle: true,
	useCurrent: true,
	ignoreReadonly: true,
	minDate: new Date(),
	toolbarPlacement: 'top',
	locale: 'nl',
	icons: {
		time: 'fa fa-clock-o',
		date: 'fa fa-calendar',
		up: 'fa fa-angle-up',
		down: 'fa fa-angle-down',
		previous: 'fa fa-angle-left',
		next: 'fa fa-angle-right',
		today: 'fa fa-dot-circle-o',
		clear: 'fa fa-trash',
		close: 'fa fa-times'
	}
};

$(function() {

	var optionsTime1 = $.extend({}, defaults, {format:'HH:mm'});
	var optionsTime2 = $.extend({}, defaults, {format:'HH:mm'});

    
    $('.timepickerinicio').datetimepicker(optionsTime1);
    $('.timepickerfinzaliar').datetimepicker(optionsTime2);
});


$('#enviar').click(function () {
	var inicio = $('#timeinicio').val();
    var fin = $('#timefin').val();

    inicioMinutos = parseInt(inicio.substr(3,2));
    inicioHoras = parseInt(inicio.substr(0,2));
    
    finMinutos = parseInt(fin.substr(3,2));
    finHoras = parseInt(fin.substr(0,2));

    transcurridoMinutos = finMinutos - inicioMinutos;
    transcurridoHoras = finHoras - inicioHoras;
    
    if (transcurridoMinutos < 0) {
        transcurridoHoras--;
        transcurridoMinutos = 60 + transcurridoMinutos;
    }
    
    horas = transcurridoHoras.toString();
    minutos = transcurridoMinutos.toString();
    
    if (horas.length < 2) {
        horas = "0"+horas;
    }
    
    if (horas.length < 2) {
        horas = "0"+horas;
    }
	
	//document.getElementById("resta").value = horas+":"+minutos;
	//Tip: 1000 ms = 1 second.
	Lobibox.confirm({
		msg: "¿Esta bien los datos?",
		callback: function ($this, type) {
			if (type === 'yes') {
				// Lobibox.notify('success', {
				// 	msg: 'Se ha enviado correctamente'
				// });
			
				$('#enviar').prop('disabled', true);
				if(inicio!=fin){
					timereaload=minutos*60000;
					Lobibox.notify('info', {
						msg: 'El tiempo restante sera '+minutos+' minutos'
					});
					$.ajax({
					url:"/tiempo",
					type:"POST",
					dataType: 'json',
					contentType: "application/json; charset=utf-8",
					data : JSON.stringify({"tiempo":timereaload}),
					headers: { "Authorization": 'Bearer '+localStorage.getItem("token")+''},
					success:function(response){
						
						if(response!=null){
							$("#demo").html(`<img src="/video_recono/${response}" width='100%' class="figure-img img-fluid rounded" >`);
						}
						setTimeout(function(){ location.reload(); }, timereaload);
						
					}
				});
				}else{
					timereaload = 1*60000;
					$.ajax({
						url:"/tiempo",
						type:"POST",
						dataType: 'json',
						contentType: "application/json; charset=utf-8",
						data : JSON.stringify({"tiempo":timereaload}),
						headers: { "Authorization": 'Bearer '+localStorage.getItem("token")+''},
						success:function(response, httpObj){
							if(response!=null){
								$("#demo").html(`<img src="/video_recono/${response}" width='100%' class="figure-img img-fluid rounded" >`);
								Lobibox.notify('info', {
									msg: 'El tiempo inicio y fin iguales. Sera 1 minuto'
								});
							}
							setTimeout(function(){ location.reload(); }, timereaload);
						},
						error:function(jqXHR, textStatus, errorThrown){
							Lobibox.notify('error', {
								msg: 'No se realizo el expiracion Token o valores erroneos. Estado: '+textStatus+''
							});
						}
					});
				}
			} else if (type === 'no') {
				Lobibox.notify('error', {
					msg: 'No se realizo el enviado'
				});
			}
		}
	});
});
	