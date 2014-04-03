$("#add-enlace").on('click', mostrarCuadroEnlace);

function mostrarCuadroEnlace(e){
	e.preventDefault();
	$('#enlace').toggle();
}

$("#add-codigo").on('click', mostrarCuadroCodigo);

function mostrarCuadroCodigo(e){
	e.preventDefault();
	$('#codigo').toggle();
}

$('.dropdown-toggle').dropdown();



$('#negrita').on('click', ponerNegrita);

function ponerNegrita(e){
	e.preventDefault();
	var cont = $('#contenido').val();
	$('#contenido').html('<b>'+cont+'</b>');
	console.log('negritaaaaa!!!!');
}

$('#preguntar').on('click', ponerPregunta);

function ponerPregunta(e){
	e.preventDefault();
	var tituloPregunta = $('#titulo-p').val();
	$('#tit-pregunta').html('<h2>'+tituloPregunta+'</h2>');
}

$('#agregar-enlace-bot').on('click',mostrarEnlace);

function mostrarEnlace(e){
	e.preventDefault();
	var cuadroEnlace = $('#cuadro-enlace').val();
	$('#cont-enlace').html('<a>'+cuadroEnlace+'</a>');
}


