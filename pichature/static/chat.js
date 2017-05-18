window.addEventListener('load',load);

function load(){
    setSocket();
}

/*function setSocket() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);
    
    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        var chat = $("#chat")
        var elem = $('<tr></tr>')

        elem.append(
            $("<td></td>").text(data.timestamp)
        )
        elem.append(
            $("<td></td>").text(data.user)
        )
        elem.append(
            $("<td class=\"messagePicture\"></td>").append("<img class=\"pictureText\" src=\"" + data.message_picture + "\" >")
        )
        
        chat.append(elem)
    };

    $("#chatform").on("submit", function(event) {
        var message = {
            user: 0, //getCookie("userId"),
            message: $('#message').val(),
        }
        chatsock.send(JSON.stringify(message));
        $("#message").val('').focus();
        return false;
    });
}*/

function getCookie(name) {
    var cookies = document.cookie.split(';');
    for(var i=0 ; i < cookies.length ; ++i) {
        var pair = cookies[i].trim().split('=');
        if(pair[0] == name)
            return pair[1];
    }
    return null;
};