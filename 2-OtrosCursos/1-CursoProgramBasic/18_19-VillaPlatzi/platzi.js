var villaPlatzi = document.getElementById("villaPlatzi");
var papel = villaPlatzi.getContext("2d");
var cantAnimals = aleatorio(1, 10);

document.addEventListener("keyup", moverCerdito);

var teclas = {
    UP : 38,
    DOWN: 40,
    LEFT: 37,
    RIGHT: 39
};

var fondo = {
    url: "tile.png",
    cargaOk: false
}

var vaca = {
    url : "vaca.png",
    cargaOk: false
}

var cerdo = {
    url : "cerdo.png",
    cargaOk: false,
    xi: 0,
    yi: 0
}

var pollo = {
    url : "pollo.png",
    cargaOk: false
}

fondo.imagen = new Image();
fondo.imagen.src = fondo.url;
fondo.imagen.addEventListener("load", cargarFondo);

vaca.imagen = new Image();
vaca.imagen.src = vaca.url;
vaca.imagen.addEventListener("load", cargarVacas);

cerdo.imagen = new Image();
cerdo.imagen.src = cerdo.url;
cerdo.imagen.addEventListener("load", cargarCerdos);

pollo.imagen = new Image();
pollo.imagen.src = pollo.url;
pollo.imagen.addEventListener("load", cargarPollos);

function cargarFondo(){
    fondo.cargaOk = true;
    dibujar();
}

function cargarVacas(){
    vaca.cargaOk = true;
    dibujar();
}

function cargarCerdos(){
    cerdo.cargaOk = true;
    dibujar();
}

function cargarPollos(){
    pollo.cargaOk = true;
    dibujar();
}

function dibujar(){

    if(fondo.cargaOk) papel.drawImage(fondo.imagen, 0, 0);
    
    for (var i = 0; i < cantAnimals; i++) {

        var position = generateAleatorianPosition();
        if (vaca.cargaOk) papel.drawImage(vaca.imagen, position.x, position.y);

        position = generateAleatorianPosition();
        if(pollo.cargaOk) papel.drawImage(pollo.imagen, position.x, position.y);
    }

    if(cerdo.cargaOk) papel.drawImage(cerdo.imagen, cerdo.xi, cerdo.yi);


}

function aleatorio(min, max) {
    var resultado;
    resultado = Math.floor(Math.random() * (max - min + 1)) + min;
    return resultado;
}

function generateAleatorianPosition(){

    var position = {
        x: 0,
        y: 0
    }

    var x = aleatorio(0, 7);
    var y = aleatorio(0, 10);
    position.x = x * 60;
    position.y = y * 40;

    return position;
}

function moverCerdito(moverCerditoEvent){

    var movimiento = 10;

    switch (moverCerditoEvent.keyCode) {

        case teclas.UP:    
            cerdo.yi -= movimiento;
            dibujar();          
        break;
        case teclas.DOWN:
            cerdo.yi += movimiento;
            dibujar();          
        break;
        case teclas.LEFT:
            cerdo.xi -= movimiento;
            dibujar();          
        break;
        case teclas.RIGHT:
            cerdo.xi += movimiento;
            dibujar();   
        break;    
        default:
            break;
    }
}

// Nota:
// Cuando dibujamos en canvas tenemos que asegurarnos que la imagen haya cargado, solo despues de
// eso podemos dibujar.
// En este código cada objeto tiene un evento cargar que edita un booleano a true con el
// fin de saverlo en el momento de dibujar

//Se soluciona el reto de mover al cerdo con el teclado.