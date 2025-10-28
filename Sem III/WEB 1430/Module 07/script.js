// 🎉 Celebration messages embedded directly (no XHR)
const messages = [
  "Congratulations — you did it!",
  "Hats off to your hard work!",
  "The tassel was worth the hassle!",
  "Your future is bright — shine on!",
  "Cheers to your amazing journey!",
  "Well done, graduate!",
  "You made it to the finish line!",
  "Here’s to new beginnings!",
  "Keep reaching for the stars!",
  "Celebrate — this moment is yours!"
];

let countdownInterval = null;

// Return a Date object for the next graduation (June 1 this year or next)
function getGraduationDate() {
  const now = new Date();
  // month index: 5 -> June (0 = Jan)
  let grad = new Date(now.getFullYear(), 5, 1, 0, 0, 0, 0);
  if (now >= grad) {
    // if it's already June 1 or later this year, use next year
    grad = new Date(now.getFullYear() + 1, 5, 1, 0, 0, 0, 0);
  }
  return grad;
}

function initializeCountdown() {
  const app = document.getElementById("app");

  // clear in case of re-init
  app.innerHTML = "";

  const title = document.createElement("h1");
  title.textContent = "Graduation Countdown Timer";

  const countdownDisplay = document.createElement("p");
  countdownDisplay.id = "countdown-display";
  countdownDisplay.textContent = ""; // will be filled by updater

  // Buttons
  const controls = document.createElement("div");
  controls.className = "controls";

  const startBtn = document.createElement("button");
  startBtn.textContent = "Start Countdown";
  startBtn.addEventListener("click", startCountdown);

  const stopBtn = document.createElement("button");
  stopBtn.textContent = "Stop Countdown";
  stopBtn.className = "secondary";
  stopBtn.addEventListener("click", stopCountdown);

  const zeroBtn = document.createElement("button");
  zeroBtn.textContent = "Set Countdown to Zero";
  zeroBtn.addEventListener("click", setCountdownToZero);

  controls.append(startBtn, stopBtn, zeroBtn);

  const messageEl = document.createElement("div");
  messageEl.id = "congrats-message";
  messageEl.className = "message";
  messageEl.style.display = "none";

  app.append(title, countdownDisplay, controls, messageEl);

  // auto-start
  startCountdown();
}

function formatRemaining(distance) {
  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);
  return `${days}d ${hours}h ${minutes}m ${seconds}s`;
}

function getRandomMessage() {
  const idx = Math.floor(Math.random() * messages.length);
  return messages[idx];
}

function startCountdown() {
  const display = document.getElementById("countdown-display");
  const msg = document.getElementById("congrats-message");
  msg.style.display = "none";

  const graduationDate = getGraduationDate().getTime();

  // clear any existing interval
  if (countdownInterval) clearInterval(countdownInterval);

  function update() {
    const now = Date.now();
    const distance = graduationDate - now;

    if (distance <= 0) {
      clearInterval(countdownInterval);
      countdownInterval = null;
      display.textContent = "";
      msg.textContent = getRandomMessage();
      msg.style.display = "block";
      return;
    }

    display.textContent = formatRemaining(distance);
  }

  // Immediate update (avoid 1-second initial delay)
  update();
  countdownInterval = setInterval(update, 1000);
}

function stopCountdown() {
  if (countdownInterval) {
    clearInterval(countdownInterval);
    countdownInterval = null;
  }
}

function setCountdownToZero() {
  if (countdownInterval) {
    clearInterval(countdownInterval);
    countdownInterval = null;
  }
  const display = document.getElementById("countdown-display");
  const msg = document.getElementById("congrats-message");
  display.textContent = "";
  msg.textContent = getRandomMessage();
  msg.style.display = "block";
}

/* ---------------------
   XHR Practice Section
   --------------------- */
document.addEventListener("DOMContentLoaded", () => {
  // initialize countdown when DOM ready
  initializeCountdown();

  // XHR practice wiring
  const getInfoBtn = document.getElementById("getInfoBtn");
  const postInput = document.getElementById("postIdInput");
  const postInfo = document.getElementById("postInfo");

  getInfoBtn.addEventListener("click", () => {
    const raw = postInput.value;
    const id = parseInt(raw, 10);

    postInfo.innerHTML = ""; // reset

    if (Number.isNaN(id) || id < 1 || id > 10) {
      postInfo.innerHTML = `<p style="color:crimson;">Please enter a number between 1 and 10.</p>`;
      return;
    }

    // simple XHR fetch from jsonplaceholder
    const xhr = new XMLHttpRequest();
    xhr.open("GET", `https://jsonplaceholder.typicode.com/posts/${id}`, true);
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          try {
            const post = JSON.parse(xhr.responseText);
            postInfo.innerHTML = `<h3>${escapeHtml(post.title)}</h3><p>${escapeHtml(post.body)}</p>`;
          } catch (e) {
            postInfo.innerHTML = `<p style="color:crimson;">Error parsing response.</p>`;
          }
        } else {
          postInfo.innerHTML = `<p style="color:crimson;">Error fetching data (status ${xhr.status}).</p>`;
        }
      }
    };
    xhr.send();
  });
});

// small helper to avoid injecting raw text (basic escape)
function escapeHtml(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}
