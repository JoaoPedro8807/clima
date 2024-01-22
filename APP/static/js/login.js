var pass_input = document.getElementById('formGroupExampleInput3')

pass_input.onfocus = function(){
    document.getElementById('message').style.display = 'block';
};
pass_input.onblur = function(){
    document.getElementById('message').style.display = 'none';
};
var elementos = [
    document.getElementById('lower'),
    document.getElementById('upper'),
    document.getElementById('number'),
    document.getElementById('length')
];
var casos = [
    lowerCaseWords = /[a-z]/g,
    upperCaseWords = /[A-Z]/g,
    numberCaseWords = /[0-9]/g,
    lengthCaseWords = /.{8,30}/g
]
pass_input.onkeyup = function(){
    for (i=0; i<=elementos.length; i++){
        verify_case(pass_input, casos[i], elementos[i]);
    }
}
function verify_case(input, caso, elemento){
    if(input.value.match(caso)){
        elemento.classList.remove('invalid');
        elemento.classList.add('valid');
    }
    else{
        elemento.classList.remove('valid');
        elemento.classList.add('invalid');
    }
}


var email_input = document.getElementById('formGroupExampleInput2');

email_input.onfocus = function(){
    document.getElementById('message_email').style.display = 'block';
};
email_input.onblur = function(){
    document.getElementById('message_email').style.display = 'none';
};

regex_email = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/g
valid_element = document.getElementById('message_email_p')

email_input.onkeyup = function(){
    if(email_input.value.match(regex_email)){
        valid_element.classList.remove('invalid');
        valid_element.classList.add('valid');
        valid_element.innerText = "Email válido!"
    }
    else{
        valid_element.classList.remove('valid');
        valid_element.classList.add('invalid');
        valid_element.innerText = "Email inválido!";
    }
}