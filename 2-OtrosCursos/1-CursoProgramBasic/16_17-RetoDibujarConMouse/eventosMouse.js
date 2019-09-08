var z = document.getElementById("area_de_dibujo");
z.addEventListener("mousemove", rayando);
z.addEventListener("mouseup", noclick);
z.addEventListener("mousedown", click);
var pantalla = z.getContext("2d");

var x1, y1, x2, y2;
var mouse = false;
var tinte = "Green";

function dibujarLinea(color, xini, yini, xfin, yfin, lienzo)
{
  lienzo.beginPath();
  lienzo.strokeStyle = color;
  lienzo.lineWidth = 2;
  lienzo.moveTo(xini, yini);
  lienzo.lineTo(xfin, yfin);
  lienzo.stroke();
  lienzo.closePath();
}

function rayando(evento)
{
  if (mouse)
  {
    x2 = evento.offsetX;
    y2 = evento.offsetY;

    dibujarLinea(tinte, x1, y1, x2, y2, pantalla)
    x1 = x2;
    y1 = y2;
  }

  else
  {
    x1 = undefined;
    y1 = undefined;
  }
}

  function noclick(evento)
  {
    mouse = false;
  }

  function click(evento)
  {
    mouse = true;
  }