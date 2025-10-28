
const messages = [
    "Congratulations! You did it!",
    "Hats off to your hard work!",
    "You’ve earned every bit of this success!",
    "The tassel was worth the hassle!",
    "Your future is bright — shine on!",
    "Cheers to your amazing journey!",
    "Well done, graduate!",
    "You made it to the finish line!",
    "Here’s to new beginnings!",
    "Keep reaching for the stars!"
  ];
  
  let countdownInterval;
  
  function initializeCountdown() {
    const app = document.getElementById("app");
  
    const title = document.createElement("h1");
    title.textContent = "Graduation Countdown Timer";
  
    const countdownDisplay = document.createElement("p");
    countdownDisplay.id = "countdown-display";
  
    const startBtn = document.createElement("button");
    startBtn.textContent = "Start Countdown";
    startBtn.onclick = startCountdown;
  
    const stopBtn = document.createElement("button");
    stopBtn.textContent = "Stop Countdown";
    stopBtn.onclick = stopCountdown;
  
    const zeroBtn = document.createElement("button");
    zeroBtn.textContent = "Set Countdown to Zero";
    zeroBtn.onclick = setCountdownToZero;
  
    app.append(title, countdownDisplay, startBtn, stopBtn, zeroBtn);
    startCountdown();
  }
  
  function startCountdown() {
    const graduationDate = new Date("June 1, 2026 00:00:00").getTime(); 
    const display = document.getElementById("countdown-display");
  
    clearInterval(countdownInterval);
  
    countdownInterval = setInterval(() => {
      const now = new Date().getTime();
      const distance = graduationDate - now;
  
      if (distance <= 0) {
        clearInterval(countdownInterval);
        display.textContent = getRandomMessage();
        display.classList.add("message");
        return;
      }
  
      const days = Math.floor(distance / (1000 * 60 * 60 * 24));
      const hours = Math.floor(
        (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
      );
      const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((distance % (1000 * 60)) / 1000);
  
      display.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }, 1000);
  }
  
  function stopCountdown() {
    clearInterval(countdownInterval);
  }
  
  function setCountdownToZero() {
    clearInterval(countdownInterval);
    const display = document.getElementById("countdown-display");
    display.textContent = getRandomMessage();
    display.classList.add("message");
  }
  
  function getRandomMessage() {
    const randomIndex = Math.floor(Math.random() * messages.length);
    return messages[randomIndex];
  }
  
  document.getElementById("getInfoBtn").addEventListener("click", () => {
    const id = document.getElementById("postIdInput").value;
    const postInfo = document.getElementById("postInfo");
    postInfo.innerHTML = "";
  
    if (id < 1 || id > 10) {
      postInfo.innerHTML = `<p style="color:red;">Please enter a number between 1 and 10.</p>`;
      return;
    }
  
    const xhr = new XMLHttpRequest();
    xhr.open("GET", `https://jsonplaceholder.typicode.com/posts/${id}`);
    xhr.onload = function () {
      if (xhr.status === 200) {
        const post = JSON.parse(xhr.responseText);
        postInfo.innerHTML = `
          <h3>${post.title}</h3>
          <p>${post.body}</p>
        `;
      } else {
        postInfo.innerHTML = `<p style="color:red;">Error fetching data.</p>`;
      }
    };
    xhr.send();
  });
  
  window.onload = initializeCountdown;
  