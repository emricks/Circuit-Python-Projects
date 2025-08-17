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

function sendRequestSolid() {
    const r = parseInt(document.getElementById("r").value);
    const g = parseInt(document.getElementById("g").value);
    const b = parseInt(document.getElementById("b").value);

    const data = {
        color: [r, g, b]
    }

    fetch(server + '/leds/animate/solid_fill', {
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

function colorChoiceDisplay() {
    document.getElementById("r").style.display = "inline-block"
    document.getElementById("g").style.display = "inline-block"
    document.getElementById("b").style.display = "inline-block"
    document.getElementById("slayerselect").style.display = "none"
    document.getElementById("acceptColor").style.display = "block"
}

let barcolor = [0, 0, 0]
let goal = 0
let current = 0
let aatrox = false
let tier = 0
let diff = 0

function setup() {
    const r = parseInt(document.getElementById("r").value);
    const g = parseInt(document.getElementById("g").value);
    const b = parseInt(document.getElementById("b").value);
    goal = parseInt(document.getElementById("xpgoal").value)
    current = parseInt(document.getElementById("currentxp").value)
    aatrox = document.getElementById("aatrox").checked
    tier = parseInt(document.getElementById("bosstier").value)
    barcolor = [r, g, b]
    switch (tier) {
        case 1:
            diff = 5
            break;
        case 2:
            diff = 25
            break;
        case 3:
            diff = 100
            break;
        case 4:
            diff = 500
            break;
        case 5:
            diff = 1500
            break;
    }
    if (aatrox == true) {
        diff = Math.floor(diff * 1.25)
    }
    document.getElementById("acceptColor").style.display = "none"

    const data = {
        color: barcolor,
        xpgoal: goal,
        xpcurrent: current,
        isaatrox: aatrox,
        bosstier: tier
    }

    document.getElementById("xpdisplay").innerHTML = `${xpqqcurrent}`

    fetch(server + '/leds/animate/bar', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
}

function addBoss() {
    console.log(diff)
    console.log(current)
    current += diff
    document.getElementById("xpdisplay").innerHTML = `${current}`

    const data = {
        color: barcolor,
        xpgoal: goal,
        xpcurrent: current,
        isaatrox: aatrox,
        bosstier: tier
    }

    fetch(server + '/leds/animate/bar', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
}
