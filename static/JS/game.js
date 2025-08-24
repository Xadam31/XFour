let score = 0;
let time = 30;

const btn = document.getElementById('game-btn');
const scoreDisplay = document.getElementById('score');
const timerDisplay = document.getElementById('timer');
const container = document.getElementById('game-container');
const audio = document.getElementById('game-audio');

function moveButton() {
    const maxX = container.clientWidth - btn.offsetWidth;
    const maxY = container.clientHeight - btn.offsetHeight;
    const x = Math.random() * maxX;
    const y = Math.random() * maxY;
    btn.style.left = x + 'px';
    btn.style.top = y + 'px';
}

btn.addEventListener('click', () => {
    // Start audio on first click
    if (audio.paused) {
        audio.loop = true;
        audio.play();
    }

    score++;
    scoreDisplay.textContent = `Score: ${score}`;
    moveButton();

    // Easter egg
    if (score === 15) {
        alert("You're a neon pro! 🌟");
    }
});

const interval = setInterval(() => {
    if (audio.paused) return; // wait for game start
    time--;
    timerDisplay.textContent = `Time: ${time}s`;
    if (time <= 0) {
        clearInterval(interval);
        audio.pause();
        alert(`Time's up! Your final score: ${score}`);
        btn.disabled = true;
    }
}, 1000);

moveButton();
