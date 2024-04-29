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
        else if(!(/^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/.test($('.txtEmail').val())))
        {
            alert('El formato del correo no es válido');
        }
        else if($('.txtClave').val() == "")
        {
            alert('No especificó la clave');
        }else if(!(/[a-zA-Z][d]/.test($('.txtClave').val())))
        {
            alert('El formato de la clave no es válido');
        }
        else
        {
            alert("Los datos enviados son: " + 
                    $('.txtEmail').val() + '\n' + 
                    $('.txtClave').val()             
                );
        }
    })

})