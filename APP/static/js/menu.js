const time_box = document.getElementById('time_default')
var current_time = time_box.textContent

const re = new RegExp(/(\d{1,2}):(\d{1,2}):(\d{1,2})/)

var current_format = re.exec(current_time);

var segundo = current_format[3]
var minuto = current_format[2]
var hora = current_format[1]


setInterval(timer, 1000)

function timer(){
    if (minuto && segundo && hora === '0'){
        return 0
    }
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