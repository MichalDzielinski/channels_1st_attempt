console.log('Hello, this is Tony Hawk');


const socket = new WebSocket('ws://'+window.location.host+'/ws/some-stati/')
console.log(socket);

socket.onmessage = function(e){
    console.log('Server: '+ e.data);
};

socket.onopen = function(e){
    socket.send(JSON.stringify({
        'message': "Hello from client",
        'sender': "test sender",
    }))
}