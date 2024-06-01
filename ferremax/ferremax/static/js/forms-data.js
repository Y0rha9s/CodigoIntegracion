function escucharTeclado(input){
    console.log('texto:', input.value);
}

$("#txt-apellidos").keyup(function(){
    let texto = $("#txt-apellidos").val()
    console.log('texto:', texto);
    console.log('tamaño texto:', texto.length);
    let tamanio = texto.length
    let ultimaLetra = texto.substring(tamanio - 1);
    console.log('ultimaLetra: ', ultimaLetra);
    console.log('isNaN:', isNaN(ultimaLetra));

    if(ultimaLetra === " " || isNaN(ultimaLetra)){
        $("#txt-apellidos").val(texto.toUpperCase());
    }else{
        texto = texto.substring(0, tamanio - 1);
        $("#txt-apellidos").val(texto.toUpperCase());
    }
});

function validarTelefono(){
    let telefono = $("#txt-telefono").val();
    console.log('teléfono: ', telefono);
    const regexp = /([0-9]){9}/;
    console.log('es númerico: ', regexp.test(telefono));
    if(regexp.test(telefono) && telefono.length === 9){
        $("#txt-telefono-error").html(' ');
        $("#txt-telefono-error").addClass("d-none");
    }else{
        $("#txt-telefono-error").html('Télefono inválido .');
        $("#txt-telefono-error").removeClass("d-none");
    }
}

$("#txt-telefono").on("focusout", function() {
    console.log('focusout');    
    validarTelefono();
});

$("#btn-send-forms").on("click", function(){
    console.log('click');
    validarTelefono();
});

