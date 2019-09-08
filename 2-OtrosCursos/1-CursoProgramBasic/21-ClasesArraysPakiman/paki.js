var imagenes = [];
imagenes["Cauchin"] = "vaca.png";
imagenes["Pokacho"] = "pollo.png";
imagenes["Tocinauro"] = "cerdo.png";

var coleccion = [];
coleccion.push( new Pakiman("Cauchin", 100, 30) );
coleccion.push(new Pakiman("Pokacho", 80, 50));
coleccion.push(new Pakiman("Tocinauro", 120, 40));


//una forma de recorrer el array extrayendo el objeto completo
// for(var freddito of coleccion)
//   freddito.mostrar();


//La misma forma que la anterior pero mas pro
coleccion.forEach(pakiman => {
    
    pakiman.mostrar();
});

//Iteración de un array estrayendo el indice
for(var x in coleccion)
{
  console.log(x);
}