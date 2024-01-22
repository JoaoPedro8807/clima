var box = document.querySelectorAll('.confirm');

var cancelBtn = document.querySelectorAll('.cancelbtn')

window.onclick = function(event){
    box.forEach(e =>{
        if (event.target == e){
            e.style.display =  "none";
    }
    })

}

cancelBtn.forEach(botao =>{
    botao.addEventListener("click", function (e){
        box.forEach(caixa =>{
            caixa.style.display = "none";
        })
    })
})



