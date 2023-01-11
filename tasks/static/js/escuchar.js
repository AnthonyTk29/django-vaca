$(document).ready(function() {
    $('body').on('click', '#items_en_uso a', function() {
        var a = document.getElementById($(this).attr('id')).innerHTML;
        poblarLocalStorage(a);
    })

    function poblarLocalStorage(nom) {
        localStorage.setItem("nom_vaca", nom); //src es el nombre por el cual accederemos
    }


})