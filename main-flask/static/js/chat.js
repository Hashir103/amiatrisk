// Collapsible
var coll = document.getElementsByClassName("collapsible");

for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");

        var content = this.nextElementSibling;

        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }

    });
}

function getTime() {
    let today = new Date();
    hours = today.getHours();
    minutes = today.getMinutes();

    if (hours < 10) {
        hours = "0" + hours;
    }

    if (minutes < 10) {
        minutes = "0" + minutes;
    }

    let time = hours + ":" + minutes;
    return time;
}

// Gets the first message
function firstBotMessage() {
    let firstMessage = "How's it going?"
    document.getElementById("botStarterMessage").innerHTML = '<p class="botText"><span>' + firstMessage + '</span></p>';

    let time = getTime();

    $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);
}

firstBotMessage();

// Retrieves the response
async function getHardResponse(userInput) {

    const data = JSON.stringify({ userInput })

    document.getElementById("chat-bar-bottom").scrollIntoView(true);
    var response = await fetch(`http://127.0.0.1:5000/test`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: data
    })
    const finalResponse = await response.text()

    let userHtml = '<p class="botText"><span>' + finalResponse + '</span></p>';
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);


    // console.log("response", response)
    // let bottHtml = '<p class="botText"><span>' + response + '</span></p>';
    // $("#chatbox").append(bottHtml);
    // console.log("resoponse", await response)

    // $.ajax({
    //     url:"/",
    //     type:"POST",
    //     contentType:"application/json",
    //     data: JSON.stringify(userInput)
    // });

    // let botResponse = getBotResponse(data);
    // let botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
    // $("#chatbox").append(botHtml);

    // document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

//Gets the text text from the input box and processes it
async function recieveInput() {
    const userInput = document.getElementById("textInput").value;
    let userHtml = '<p class="userText"><span>' + userInput+ '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);
    await getHardResponse(userInput);

}

// Handles sending text via button clicks
// function buttonSendText(sampleText) {
//     let userHtml = '<p class="userText"><span>' + sampleText + '</span></p>';

//     $("#textInput").val("");
//     $("#chatbox").append(userHtml);
//     document.getElementById("chat-bar-bottom").scrollIntoView(true);

//     setTimeout(() => {
//         getHardResponse(sampleText);
//     }, 1000)
// }

// function sendButton() {
//     recieveInput();
// }

// Press enter to send a message
$("#textInput").keypress(function (e) {
    console.log("asd")
    if (e.which == 13) {
        console.log("asd")
        recieveInput();
    }
});