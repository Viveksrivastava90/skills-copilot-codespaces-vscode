<html lang="en"><head><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="viewport" content="width=device-width, initial-scale=1">


    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VIVEK </title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <canvas id="matrixCanvas"></canvas>

    <div class="container">
        <div class="header">ALL GAME HACK</div>
        
        <button class="btn" id="startScript">VIVEK </button>
        <button class="btn" id="startInjector">START INJECTOR</button>
        <button class="btn">JAB NEXT PERIOD AAYE TAB - TAB ❌ ISKO CLICK KRKE OPEN KARNA HAI</button>

        <div class="footer"><span class="highlight">VIVEK</span></div>
    </div>

    <!-- Floating Injector UI -->
    <div id="injectorBox" class="hidden">
        <div class="injector-header">
            <img src="/IMG.jpg" alt="Itachi Uchiha" class="profile-icon">
            <span>Itachi Uchiha</span>
            <button class="close-btn" onclick="closeInjectorBox()">✖</button>
        </div>

        <div class="injector-content">
            <p>Script V3 Active...</p>
            <p>Executing script...</p>
            <p>Checking for current period</p>
            <p>Period: <span id="period"></span></p>
            <p>Processing...</p>
            <p>Progress: <span id="progress">0%</span></p>
            <p>Prediction - <span id="prediction"></span></p>
            <p>Script execution completed...</p>
        </div>

        <div class="injector-footer">
            <span id="fps">FPS: 62.0</span>
            <span>are using some servers to capture results</span>
        </div>
    </div>

    <script src="script.js"></script>

<style>body, html {
    margin: 0;
    padding: 0;
    overflow: hidden;
    font-family: 'Courier New', monospace;
}

#matrixCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
}

.container {
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 90%;
}

.header, .footer {
    font-size: 22px;
    color: lime;
    padding: 10px;
    border: 2px solid lime;
    margin-bottom: 10px;
}

.btn {
    display: block;
    width: 80%;
    padding: 15px;
    margin: 10px auto;
    background: black;
    border: 2px solid lime;
    color: red;
    font-size: 18px;
    cursor: pointer;
}

.highlight {
    color: lime;
}

.btn:hover {
    background: lime;
    color: black;
}

/* Floating Injector UI */
#injectorBox {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 90%;
    max-width: 400px;
    background: black;
    color: lime;
    border: 2px solid lime;
    padding: 15px;
    z-index: 10;
    box-shadow: 0px 0px 10px lime;
}

.injector-header {
    background: red;
    color: white;
    padding: 10px;
    font-size: 20px;
    text-align: left;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.profile-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
}

.injector-content {
    padding: 10px;
    font-size: 18px;
}

.injector-footer {
    background: red;
    color: white;
    padding: 10px;
    text-align: left;
    font-size: 14px;
}

.close-btn {
    background: black;
    color: white;
    border: none;
    font-size: 18px;
    cursor: pointer;
}

/* Hide elements by default */
.hidden {
    display: none;
}

</style><script>// Matrix Effect
const canvas = document.getElementById("matrixCanvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const letters = "アカサタナハマヤラワ1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const matrix = letters.split("");

const fontSize = 16;
const columns = canvas.width / fontSize;
const drops = Array.from({ length: columns }).fill(1);

function drawMatrix() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0F0";
    ctx.font = `${fontSize}px monospace`;

    drops.forEach((y, index) => {
        const text = matrix[Math.floor(Math.random() * matrix.length)];
        const x = index * fontSize;
        ctx.fillText(text, x, y * fontSize);

        if (y * fontSize > canvas.height && Math.random() > 0.975) {
            drops[index] = 0;
        }
        drops[index]++;
    });

    requestAnimationFrame(drawMatrix);
}

drawMatrix();

// Prediction Logic
const resultsPattern =["SMALL", "BIG", "SMALL", "BIG", "BIG", "SMALL", "BIG","SMALL", "BIG", "BIG", "SMALL",];
let currentPeriodIndex = 0;

function updatePeriodAndTimer() {
    const now = new Date();
    const minutes = now.getUTCHours() * 60 + now.getUTCMinutes();

    const periodNumber = `${now.getUTCFullYear()}${(now.getUTCMonth() + 1).toString().padStart(2, "0")}${now.getUTCDate().toString().padStart(2, "0")}1000${(10001 + minutes).toString()}`;
    document.getElementById("period").textContent = periodNumber;

    displayResult();
}

function displayResult() {
    const resultDisplay = document.getElementById("prediction");
    const progressDisplay = document.getElementById("progress");

    let progress = 0;
    let progressInterval = setInterval(() => {
        if (progress >= 100) {
            clearInterval(progressInterval);
            const currentResult = resultsPattern[currentPeriodIndex];
            resultDisplay.innerHTML = `- ◆◇ ${currentResult} ◇◆ -`;
            currentPeriodIndex = (currentPeriodIndex + 1) % resultsPattern.length;
        } else {
            progress += 20;
            progressDisplay.textContent = `${progress}%`;
        }
    }, 500);
}

// Floating Injector UI
document.getElementById("startInjector").addEventListener("click", () => {
    document.getElementById("injectorBox").classList.remove("hidden");
    updatePeriodAndTimer();
});

function closeInjectorBox() {
    document.getElementById("injectorBox").classList.add("hidden");
}</script>
</body></html>