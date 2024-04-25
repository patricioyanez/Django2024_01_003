$(function(){
    
    $('.btnLimpiar').click(function()
    {
        $('.txtEmail, .txtClave').val('');
    })

    $('.btnEnviar').click(function()
    {
        if($('.txtEmail').val() == "")
        {
            alert('No especificó el correo');
        }
        else if($('.txtClave').val() == "")
        {
            alert('No especificó la clave');
        }
        /* tarea validar el formato del correo jquery */
        else
        {
            alert("Los datos enviados son: " + 
                    $('.txtEmail').val() + '\n' + 
                    $('.txtClave').val()             
                );
        }
    })

})