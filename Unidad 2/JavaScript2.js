document.getElementById("txtNombre").value = "Diego";


function sumar()
{
    let numero1 = 10;
    let numero2 = 20;
    let resultado = numero1 + numero2;
    alert('El resultado es: ' + resultado)
}
function sumar2(numero1,numero2)
{
    let resultado = numero1 + numero2;
    alert('El resultado es: ' + resultado)
}
function sumar3()
{
    let numero1 = document.getElementById( "txtNumero1" ).value;    
    let numero2 = document.getElementById( "txtNumero2" ).value;    
    let resultado = Number(numero1) + Number(numero2);
    alert('El resultado es: ' + resultado)
}
function restar()
{
    let numero1 = document.getElementById( "txtNumero1" ).value;    
    let numero2 = document.getElementById( "txtNumero2" ).value;    
    let resultado = Number(numero1) - Number(numero2);
    alert('El resultado es: ' + resultado)
}