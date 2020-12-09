// var CAMERA=function(){
// //	$('button').click(function(){
// //		var user = $('#inputUsername').val();
// //		var pass = $('#inputPassword').val();
// 		$.ajax({
// 			url: 'video_feed',
// 			data: $('form').serialize(),
// 			type: 'GET',
// 			success: function(response){
// 				console.log(response);
// 				var data=JSON.parse(response);
// //				document.getElementById("demo").innerHTML = data.result;
// 				$("#demo").html('<img src='+ data.result +'>');
//                 CAMERA();
// 			},
// 			error: function(error){
// 				console.log(error);
// 			}
// 		});
// 	}
// 	CAMERA();

// $("#recopilacionfotos").click(function(){
// 	console.log("helli")
// 	$.ajax({
// 		url: 'video_feed',
// 		data: $('form').serialize(),
// 		type: 'GET',
// 		success: function(response){
// 			console.log("entraste")
// 			console.log(response);
// 			var data=JSON.parse(response);
// 			console.log(data)
// //			document.getElementById("demo").innerHTML = data.result;
// 			$("#demo").html('<img src="{{url_for("video_feed")}}" >');
// 			// CAMERA();
// 		},
// 		error: function(error){
// 			console.log(error);
// 		}
// 	});
// });

// $("#reconocimiento").click(function(){
// 	alert("Hola");
// });