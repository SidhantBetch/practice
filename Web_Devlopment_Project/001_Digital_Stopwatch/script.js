let timer;
let startTime;
let elapsedTime = 0;
let running = false;

const display = document.getElementById("display");
const startButton = document.getElementById("start");
const pauseButton = document.getElementById("pause");
const resetButton = document.getElementById("reset");

function updateDisplay() {
    let time = elapsedTime;
    let hours = Math.floor(time / 3600000);
    let minutes = Math.floor((time % 3600000) / 60000);
    let seconds = Math.floor((time % 60000) / 1000);
    display.textContent = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

startButton.addEventListener("click", function() {
    if (!running) {
        startTime = Date.now() - elapsedTime;
        timer = setInterval(function() {
            elapsedTime = Date.now() - startTime;
            updateDisplay();
        }, 1000);
        running = true;
    }
});

pauseButton.addEventListener("click", function() {
    clearInterval(timer);
    running = false;
});

resetButton.addEventListener("click", function() {
    clearInterval(timer);
    elapsedTime = 0;
    updateDisplay();
    running = false;
});
