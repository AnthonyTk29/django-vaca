function validar() {
    var cad, nombre, telefono, expresion, direccion, email, expresion;
    cad = document.getElementById("demo-cedula").value;
    nombre = document.getElementById("demo-name").value;
    telefono = document.getElementById("demo-telefono").value;
    direccion = document.getElementById("demo-direccion").value;
    email = document.getElementById("demo-email").value;
    expresion = /\w+@\w+\.+[a-z]/;
    expresion1 = /([A-Z][a-z]+) ([A-Z][a-z]+){1,3}/

    var total = 0;
    var longitud = cad.length;
    var longcheck = longitud - 1;

    if (nombre === "" || cad === "" || telefono === "" || direccion === "" || email === "") {
        alert("Todos los campos son obligatorios");
        return false;
    } else if (!expresion1.test(nombre)) {
        alert("El Nombre no es valido");
        return false;
    } else if (cad !== "" && longitud === 10) {
        for (i = 0; i < longcheck; i++) {
            if (i % 2 === 0) {
                var aux = cad.charAt(i) * 2;
                if (aux > 9) aux -= 9;
                total += aux;
            } else {
                total += parseInt(cad.charAt(i)); // parseInt o concatenará en lugar de sumar
            }
        }

        total = total % 10 ? 10 - total % 10 : 0;

        if (cad.charAt(longitud - 1) == total) {
            alert("Cedula Válida");
        } else {
            alert("Cedula Inválida");
            return false
        }
    } else {
        alert("Esto no es un número de cedula");
        return false
    }
    if (telefono.length > 11) {
        alert("El numero de telefono es muy largo");
        return false;
    } else if (isNaN(telefono)) {
        alert("El telefono ingresado no es un numero");
        return false;
    } else if (!expresion.test(email)) {
        alert("El Email no es valido");
        return false;
    } else if (empty(nombre)) {
        alert("El nombre no es valido");
        return false;
    }

}