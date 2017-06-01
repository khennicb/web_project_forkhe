/*global $*/
/*global ReconnectingWebSocket*/
/*global location*/
window.addEventListener('load',load);
var receiveTimeout;

function load(){
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
    $('#chatform').submit(function () {
        sendMessage();
        return false;
    });
    receiveTimeout = setInterval( receiveMessage, 10000 );
    //setSocket();
    setTimeout(scrollDown(), 100 );
}

function scrollDown(){
    var elem = document.getElementById('srcollBox');
    elem.scrollTop = elem.scrollHeight;
}

function sendMessage() {
    $.ajax({
        url: "ajax/send_message/",
        data: {
            'message': $('#message').val(),
        },
        type: "POST",
        dataType: 'json'
    })
    .done(function() {
        $('#message').val("");
        setTimeout(receiveMessage, 1000 );
        location.reload();
    })
    .fail(function() {
        alert("Erreur : Votre message n'a pu être envoyé.")
    });
}

function receiveMessage() {
    $.ajax({
        url: "ajax/receive_message/",
        data: {
            'messageid': getLastMsgId(),
        },
        type: "GET",
        dataType: 'json'
    })
    .done(function(data) {
        console.log(JSON.parse(data.new_msg))
    })
    .fail(function() {
        //alert("no new msg can be receive withour refresh.")
        clearInterval(receiveTimeout);
    });
}

function getLastMsgId(){
    // TODO
    return 3;
}


function setSocket() {
    /*
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
    });*/
}

function getCookie(name) {
    var cookies = document.cookie.split(';');
    for(var i=0 ; i < cookies.length ; ++i) {
        var pair = cookies[i].trim().split('=');
        if(pair[0] == name)
            return pair[1];
    }
    return null;
};