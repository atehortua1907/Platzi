var teclas = {
    UP : 38,
    DOWN: 40,
    LEFT: 37,
    RIGHT: 39
};

document.addEventListener("keyup", dibujarConTeclado);
var cuadrito = document.getElementById("area_de_dibujo")
var papel = cuadrito.getContext("2d");
var x = 150;
var y = 150;

dibujarLinea("red", 149, 149, 151, 151, papel);

function dibujarConTeclado(eventDetail){

    var colorcito = "blue";
    var movimiento = 10;

    switch (eventDetail.keyCode) {

        case teclas.UP:
            dibujarLinea(colorcito, x, y, x, y - movimiento, papel);
            y -= movimiento;            
        break;
        case teclas.DOWN:
            dibujarLinea(colorcito, x, y, x, y + movimiento, papel);
            y += movimiento;
        break;
        case teclas.LEFT:
            dibujarLinea(colorcito, x, y, x - movimiento, y, papel);
            x -= movimiento;
        break;
        case teclas.RIGHT:
            dibujarLinea(colorcito, x, y, x + movimiento, y, papel);
            x += movimiento;
        break;    
        default:
        break;
    }
    console.log(eventDetail.keyCode)
}

function dibujarLinea(color, xInicial, yInicial, xFinal, yFinal, lienzo){
    lienzo.beginPath(); 
    lienzo.strokeStyle = color;
    lienzo.lineWidth = 3;
    lienzo.moveTo(xInicial,yInicial); 
    lienzo.lineTo(xFinal,yFinal); 
    lienzo.stroke(); 
    lienzo.closePath(); 
}