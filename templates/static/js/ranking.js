

function obtenerParalelos() {
	var url = "http://localhost:3000/ejercicios/mejores"
	$.get(url, function( data ) {
		console.log(data);
		for (i = 0 ; i < data.length ; i++){
			$('#ranking').append(
				"<div class='row'>" + 
					"<div class='col-xs-12 col-sm-12 col-md-12 col-lg-12'>" +
						"<div>" + 
							"<h3> Paralelo " + data[i].paralelo + "</h3>" +
						"<div>" +
						"<table>" + 
							"<thead>" + 
								"<tr>" +
									"<th> Posicion </th>" +
									"<th> Nombres </th>" +
									"<th> Nota </th>" +
								"</tr>" +
							"</thead>" +
							"<tbody>" +
								"<tr>" +
									"<td> 1 </td>" +
									"<td>" + data[i].estudiantes.estudiante1.nombres + "</td>" +
									"<td>" + data[i].estudiantes.estudiante1.nota + "</td>" +
								"</tr>" +
								"<tr>" +
									"<td> 2 </td>" +
									"<td>" + data[i].estudiantes.estudiante2.nombres + "</td>" +
									"<td>" + data[i].estudiantes.estudiante2.nota + "</td>" +
								"</tr>" +
								"<tr>" +
									"<td> 3 </td>" +
									"<td>" + data[i].estudiantes.estudiante3.nombres + "</td>" +
									"<td>" + data[i].estudiantes.estudiante3.nota + "</td>" +
								"</tr>" +
							"</tbody>" +
						"</table>" +
					"</div>" + 
				"</div>"
				)
		}
	});
}

$(document).ready(function(){
    obtenerParalelos();

});