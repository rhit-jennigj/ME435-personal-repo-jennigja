async function sendCommand(command) {
    var response = await fetch(`/api/${command}`)
    var replyText = await response.text();
    console.log(replyText);

    document.querySelector("#replyText").innerHTML = replyText;

    return replyText;
}

function main() {
    console.log("Hello JavaScript!!!!!!!!!!!");
    //document.querySelector("#reset").innerHTML = "hello";          

    document.querySelector("#reset").onclick = () => {
        console.log("You pressed the button");
        sendCommand("RESET");
        }
    
    document.querySelector("#x1").onclick = () => {
        console.log("You pressed the button");
        sendCommand("X-AXIS 1");
        }

    document.querySelector("#x2").onclick = () => {
        console.log("You pressed the button");
        sendCommand("X-AXIS 2");
        }

    document.querySelector("#x3").onclick = () => {
        console.log("You pressed the button");
        sendCommand("X-AXIS 3");
        }

    document.querySelector("#x4").onclick = () => {
        console.log("You pressed the button");
        sendCommand("X-AXIS 4");
        }

    document.querySelector("#x5").onclick = () => {
        console.log("You pressed the button");
        sendCommand("X-AXIS 5");
        }

    document.querySelector("#zExtend").onclick = () => {
        console.log("You pressed the button");
        sendCommand("Z-AXIS EXTEND");
        }
    
    document.querySelector("#zRetract").onclick = () => {
        console.log("You pressed the button");
        sendCommand("Z-AXIS RETRACT");
        }

    document.querySelector("#gOpen").onclick = () => {
        console.log("You pressed the button");
        sendCommand("GRIPPER OPEN");
        }

    document.querySelector("#gClose").onclick = () => {
        console.log("You pressed the button");
        sendCommand("GRIPPER CLOSE");
        }
    
    document.querySelector("#status").onclick = () => {
        console.log("You pressed the button");
        sendCommand("LOADER_STATUS");
        }

    document.querySelector("#move").onclick = () => {
        let startPos = document.querySelector("#moveFrom").value;
        let endPos = document.querySelector("#moveTo").value;
        console.log("You pressed the button");
        sendCommand(`MOVE ${startPos} ${endPos}`);

        }
}


main();