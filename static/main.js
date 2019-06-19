
document.addEventListener('backbutton', function(){
  if(document.getElementById("sair_detalhes").style.display == "inherit"){
       let box = document.getElementById("cartao_detalhes");
        box.className = "content";
        document.getElementById("sair_detalhes").style.display = "none";
   return false;
  }
  else //nothing is visible, exit the app
  {
    navigator.app.exitApp();
  }
});

function detalhes(numero)
{

    if(document.getElementById("sair_detalhes"+numero).style.display == "none"){
        document.getElementById("sair_detalhes"+numero).style.display = "inherit";
        let box = document.getElementById("cartao_detalhes"+numero);
        box.className += " show";
    }else{
        document.getElementById("sair_detalhes"+numero).style.display = "none";
        let box = document.getElementById("cartao_detalhes"+numero);
        box.className = "content";
    }
}