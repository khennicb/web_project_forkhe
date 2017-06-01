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
    receiveTimeout = setInterval( receiveMessage, 3000 );
    //setSocket();
    scrollDown();
}

function scrollDown(){
    var elem = document.getElementById('srcollBox');
    elem.scrollTop = elem.scrollHeight;
}

function sendMessage() {
    if($('#message').val().length > 0) {
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
            receiveMessage
        })
        .fail(function() {
            alert("Erreur : Votre message n'a pu être envoyé.")
        });
    }
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
        if(typeof data["new_msg"] !== 'undefined' && data["new_msg"].length != 0) {
            data= data["new_msg"];
            console.log(data)
            for(var i in data) {
                addMessageInRoom(data[i]);
            }
            scrollDown();
        }
    })
    .fail(function() {
        alert("no new msg can be receive withour refresh.")
        clearInterval(receiveTimeout);
    });
}

function addMessageInRoom (message) {

    var htmlToFill = "<tr>";
    htmlToFill += "<td hidden class=\"id\">"+ message.id  +"</td>";
    htmlToFill += "<td class=\"time_message col-md-1 col-xs-2\"><i>"+ message.timestamp  +"</i></td>";
    htmlToFill += "<td class=\"sender col-md-1 col-xs-2\"><Strong>"+ message.user  +"</Strong></td>";
    htmlToFill += "<td class=\"messagePicture col-md-10 col-xs-8\">"+ message.message_picture  +"</td>";
    htmlToFill += "</tr>";
    $(".msg_list").append($(htmlToFill))
    
}

function getLastMsgId(){
    console.log("last id : " + $(".msg_list > tr:last-child > .id").text())
    return $(".msg_list > tr:last-child > .id").text();
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