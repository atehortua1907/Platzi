var johnnyFive = require("johnny-five");
var circuito = new johnnyFive.Board();
var extras=require('./extras.js');
var songs=require('j5-songs');

circuito.on("ready", power);

function power() {
    
    var led = new johnnyFive.Led(12);
    led.blink(100);

    var led2 = new johnnyFive.Led(8);
    led2.blink(300);

    var piezo = new johnnyFive.Piezo(7);
    circuito.repl.inject({
      piezo: piezo
    });

    //"mario-intro","mario-fanfare"
    extras.play_list([],piezo,function(err,tunes){
        //	Play specifics songs
        // test 
        console.log(tunes);
    });
    
    console.log("Mensaje en la consola!!");
}



