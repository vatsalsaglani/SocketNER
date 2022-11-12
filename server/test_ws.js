const { exit } = require("process");
const WebSocket = require("ws");

const ws = new WebSocket("ws://localhost:8000/ws/get-entities")

const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout
})

let is_read = true;
const send_message = (ws) => {
    console.log("\nSEND TEXT")
    readline.question("\nEnter your Text: ,", (msg) => {
        ws.send(msg);
    })

    ws.on("message", (data) => {
        console.log(data.toString())
        send_message(ws)
    })
}

ws.on("open", () => {
    if (is_read) {
        send_message(ws)
    } 
})