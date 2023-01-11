$(document).ready(function() {
    //obtenemos el valor de los input

    $('#adicionar').click(function() {
        var fecha = document.getElementById("fecha").value;
        var nombre = document.getElementById("matu").value;
        var apellido = document.getElementById("kilos").value;
        var cedula = document.getElementById("libras").value;
        var i = 1; //contador para asignar id al boton que borrara la fila
        var fila = '<tr id="row' + i + '"><td name="fecha' + i + '">' + fecha + '</td><td name="horario' + i + '">' + nombre + '</td><td name="kilo' + i + '">' + apellido + '</td><td name="libra' + i + '">' + cedula + '</td><td><button type="button" name="remove" id="' + i + '" class="btn btn-danger btn_remove">Quitar</button></td></tr>'; //esto seria lo que contendria la fila

        i++;

        $('#mytable tr:first').after(fila);
        $("#adicionados").text(""); //esta instruccion limpia el div adicioandos para que no se vayan acumulando
        var nFilas = $("#mytable tr").length;
        $("#adicionados").append(nFilas - 1);
        //le resto 1 para no contar la fila del header
        document.getElementById("apellido").value = "";
        document.getElementById("cedula").value = "";
        document.getElementById("nombre").value = "";
        document.getElementById("nombre").focus();
    });
    $(document).on('click', '.btn_remove', function() {
        var button_id = $(this).attr("id");
        //cuando da click obtenemos el id del boton
        $('#row' + button_id + '').remove(); //borra la fila
        //limpia el para que vuelva a contar las filas de la tabla
        $("#adicionados").text("");
        var nFilas = $("#mytable tr").length;
        $("#adicionados").append(nFilas - 1);
    });
    obtenerlocal();

    function obtenerlocal() {
        document.getElementById("vaca").innerHTML = localStorage.getItem("nom_vaca");
    }

    function enviarget() {
        var fecha = document.getElementById("fecha").value;
        var hora = document.getElementById("matu").value;
        var kilos = document.getElementById("kilos").value;
        var libra = document.getElementById("libras").value;
        var b = document.getElementById("vaca").innerHTML;
        alert("pilas1");
        url = "lechetotal.html/" + b.toString() + "/" + fecha.toString() + "/" + hora.toString() + "/" + kilos.toString() + "/" + libra.toString();

        alert("pilas");
    }

    function enviarpost() {
        let data = new FormData($('#formu').get(0));
        $.ajax({
            url: "lechetotal.html",
            type: "post",
            dataType: "json",
            data: { data },
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

    function enviarget() {

        $.ajax({
            url: "lechetotal.html",
            type: "get",
            dataType: "json",
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    }
});