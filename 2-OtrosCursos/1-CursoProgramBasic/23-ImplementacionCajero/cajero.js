class Billete{

    constructor(valor, cantidad){

        this.valor = valor,
        this.cantidad = cantidad
    }
}

function entregarDinero() {

    dinero = parseInt(document.getElementById("dinero").value);
    
    caja.forEach(billete => {
        
        if(dinero > 0){

            div = Math.floor(dinero / billete.valor);

            if(div > billete.cantidad) papeles = billete.cantidad;
            else papeles = div;

            entregado.push(new Billete(billete.valor, papeles));
            dinero -= billete.valor * papeles;
        }

    });

    if(dinero > 0){
        resultado.innerHTML = "Soy un cajero pobre y no tengo dinero :( ";
    }
    else{
        entregado.forEach(billeteEntregado => {

            if(billeteEntregado.cantidad > 0)
                resultado.innerHTML += billeteEntregado.cantidad +" billetes de $"+billeteEntregado.valor + "<br />";
            
        });
    }
}

var caja = [];
var entregado = [];
caja.push(new Billete(50, 3));
caja.push(new Billete(20, 2));
caja.push(new Billete(10, 2));
var dinero = 0;
var div = 0;
var papeles = 0;

var button = document.getElementById("extraer");
button.addEventListener("click", entregarDinero);
var resultado = document.getElementById("resultado");
