
var texto = document.getElementById("idTexto");
var reGex = document.getElementById("idRegex");
var boton = document.getElementById("botoncito");
var d = document.getElementById("dibujito");
var lienzo = d.getContext("2d"); 
var ancho = d.width;
var lineCount = 0;

//Matricular el evento en js
boton.addEventListener("click", dibujoPorClick);

function dibujoPorClick(){

    var regex = new RegExp(reGex.value);
    if(regex.test(texto.value))
        alert("Texto valido para el regex");
    else
        alert("Texto invalido para el regex");
    // var lineas = parseInt(texto.value);
    // dibujoCompleto(ancho/lineas,lineas);
}

function dibujarLinea(color, xInicial, yInicial, xFinal, yFinal){
    lienzo.beginPath(); 
    lienzo.strokeStyle = color; 
    lienzo.moveTo(xInicial,yInicial); 
    lienzo.lineTo(xFinal,yFinal); 
    lienzo.stroke(); 
    lienzo.closePath(); 
}

function dibujoCompleto(space, lineas){

    //Lineas Azules
    while(lineCount < lineas){
        yi = space * lineCount;
        xf = space * (lineCount + 1);
        dibujarLinea("#0F2EF1", 0, yi, xf, 300);
        lineCount++;
    }

    //Lineas rojas
    lineCount = 0;
    do{
        dibujarLinea("#F1200F", (space * lineCount), 0, 150, 300);
        lineCount++;   
    }while(lineCount <= lineas)

    //Lineas Verdes
    for(i = 0; i < lineas; i++){    
        yi = space * i;
        xf = 300 - space * i;
        dibujarLinea("#07A904", 300, yi, xf, 300);
    }

    //Bordes rosa
    dibujarLinea("#F632D2", 1, 1, 1, 299);
    dibujarLinea("#F632D2", 1, 299, 299, 299);
    dibujarLinea("#F632D2", 299, 1, 299, 299);
    dibujarLinea("#F632D2", 1, 1, 299, 1);

}
