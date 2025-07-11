server = "http://leds1.enkycode.com"

function sendRequestBlink() {
    const r = parseInt(document.getElementById("r").value);
    const g = parseInt(document.getElementById("g").value);
    const b = parseInt(document.getElementById("b").value);
    const speed = parseFloat(document.getElementById("speed").value);

    const data = {
        color: [r, g, b],
        speed: speed
    };

    fetch(server + '/leds/animate/blink_fill', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
}

function sendRequestClear() {
    fetch(server + '/leds/animate/none', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: "{}"
    });
}