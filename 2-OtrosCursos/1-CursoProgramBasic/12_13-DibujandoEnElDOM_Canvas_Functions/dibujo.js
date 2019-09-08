var d;
var lienzo;

d = document.getElementById("dibujito");
lienzo = d.getContext("2d"); //getContext metodo de un objeto canvas
console.log(lienzo); //para visualizar el objeto canvas en la consola del navegador

dibujarLinea("pink", 10, 300, 220, 10);
dibujarLinea("yellow", 310, 10, 200, 100);

function dibujarLinea(color, xInicial, yInicial, xFinal, yFinal)
{
    lienzo.beginPath(); //Instrucción para empezar a dibujar
    lienzo.strokeStyle = color; //Color del lápiz
    lienzo.moveTo(xInicial,yInicial); //Metodo de canvas de donde quiero dibujar la linea, parmas(x,y)
    lienzo.lineTo(xFinal,yFinal); //Metodo de canvas que indica hasta donde voy a llevar la linea, parmas(x,y)
    lienzo.stroke(); //Dibuja la linea
    lienzo.closePath(); //Levanta el lápiz o termina el dibujo    
}