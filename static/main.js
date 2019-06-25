function detalhes(numero)
{
    console.log(numero)
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