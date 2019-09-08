
var d = document.getElementById("dibujito");
var lienzo = d.getContext("2d"); 
var lineas = 30;
var lineCount = 0;

//Lineas Azules
while(lineCount < lineas){
    yi = 10 * lineCount;
    xf = 10 * (lineCount + 1);
    dibujarLinea("#0F2EF1", 0, yi, xf, 300);
    lineCount++;
}

//Lineas rojas
lineCount = 0;
do{
    dibujarLinea("#F1200F", (10 * lineCount), 0, 150, 300);
    lineCount++;   
}while(lineCount <= lineas)

//Lineas Verdes
for(i = 0; i < lineas; i++){    
    yi = 10 * i;
    xf = 300 - 10 * i;
    dibujarLinea("#07A904", 300, yi, xf, 300);
}

//Bordes rosa
dibujarLinea("#F632D2", 1, 1, 1, 299);
dibujarLinea("#F632D2", 1, 299, 299, 299);
dibujarLinea("#F632D2", 299, 1, 299, 299);
dibujarLinea("#F632D2", 1, 1, 299, 1);

function dibujarLinea(color, xInicial, yInicial, xFinal, yFinal){
    lienzo.beginPath(); 
    lienzo.strokeStyle = color; 
    lienzo.moveTo(xInicial,yInicial); 
    lienzo.lineTo(xFinal,yFinal); 
    lienzo.stroke(); 
    lienzo.closePath(); 
}