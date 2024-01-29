const time_box = document.getElementById('time_default')
var current_time = time_box.textContent

setInterval(timer, 1000)

const re = new RegExp(/(\d{2})\.(\d{2})\.(\d{4})/)

var current_format = current_time.replace(re);

var segundo = current_format.substring(current_format.length-2, current_format.length)
var minuto = current_format.substring(current_format.length-5, current_format.length-3)
var hora = current_format.substring(0,1)
time_box.innerHTML = ''

function timer(){
    segundo--
    if (segundo == 0){
        minuto--
        segundo = 60
        if(minuto == 0){
            hora--
            minuto = 60
        }
    }
    time_box.innerHTML = `${hora}:${minuto}:${segundo}`
}