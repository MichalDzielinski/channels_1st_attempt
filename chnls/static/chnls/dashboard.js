console.log('Hello, this is Tony Hawk');

const dashboardSlug = document.getElementById('dashboard-slug').textContent.trim()
const user = document.getElementById('user').textContent.trim()

const submitBtn = document.getElementById('submit-btn')
const dataInput = document.getElementById('data-input')
const dataBox = document.getElementById('data-box')

const socket = new WebSocket(`ws://${window.location.host}/ws/${dashboardSlug}/`)
console.log(socket);

socket.onmessage = function(e){
    console.log('server' );
    const {sender,  message} = JSON.parse(e.data)
    console.log(message) 
    console.log(sender) 
    dataBox.innerHTML += `<p>${sender}: ${message}</p>`
   
};

submitBtn.addEventListener('click', () => {
    const dataValue = dataInput.value 
    socket.send(JSON.stringify({
        'message': dataValue,
        'sender': user,
    }))

})

