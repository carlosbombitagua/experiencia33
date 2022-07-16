let url = "https://apis.digital.gob.cl/fl/feriados"
$.get(url, function(respuesta)
{

    respuesta.forEach(function(item) {
        console.log(item)
        
    });

    $("#feriado").text(feriado.nombre + " - " + feriado.fecha)

}, "json")