
(() => {
    const choices = ['rock','paper','scissors'];
    const emoji = { rock:'✊', paper:'✋', scissors:'✌️' };
  
    const playerChoiceEl = document.getElementById('playerChoice');
    const computerChoiceEl = document.getElementById('computerChoice');
    const playerScoreEl = document.getElementById('playerScore');
    const computerScoreEl = document.getElementById('computerScore');
    const resultEl = document.getElementById('result');
    const roundNumberEl = document.getElementById('roundNumber');
    const roundTotalEl = document.getElementById('roundTotal');
    const tiesEl = document.getElementById('ties');
    const pickButtons = document.querySelectorAll('.pick');
    const roundsSelect = document.getElementById('rounds');
    const resetBtn = document.getElementById('reset');
    const finalScreen = document.getElementById('finalScreen');
    const finalText = document.getElementById('finalText');
    const newGameBtn = document.getElementById('newGameBtn');
    const highScoreEl = document.getElementById('highScore');
  
    let playerScore = 0;
    let computerScore = 0;
    let ties = 0;
    let roundsPlayed = 0;
    let totalRounds = parseInt(roundsSelect.value, 10);
  
    const HS_KEY = 'rps_highscore';
    function loadHighScore(){
      const s = localStorage.getItem(HS_KEY);
      const val = s ? parseInt(s,10) : 0;
      highScoreEl.textContent = val;
      return val;
    }
    function tryUpdateHighScore(val){
      const current = loadHighScore();
      if(val > current){
        localStorage.setItem(HS_KEY, String(val));
        highScoreEl.textContent = val;
        return true;
      }
      return false;
    }

    function resetUI(){
      playerChoiceEl.textContent = '—';
      computerChoiceEl.textContent = '—';
      playerScoreEl.textContent = '0';
      computerScoreEl.textContent = '0';
      resultEl.textContent = 'Make your move!';
      roundNumberEl.textContent = '0';
      roundTotalEl.textContent = String(totalRounds);
      tiesEl.textContent = '0';
      finalScreen.classList.add('hidden');
      clearHighlights();
    }
  
    function clearHighlights(){
      playerChoiceEl.className = 'choiceBox';
      computerChoiceEl.className = 'choiceBox';
    }
  
    function pickRandom(){
      const i = Math.floor(Math.random()*choices.length);
      return choices[i];
    }
  
    function decide(a,b){
      if(a === b) return 'tie';
      if(a === 'rock' && b === 'scissors') return 'win';
      if(a === 'scissors' && b === 'paper') return 'win';
      if(a === 'paper' && b === 'rock') return 'win';
      return 'lose';
    }
  
    function highlightResult(playerOutcome){
      clearHighlights();
      if(playerOutcome === 'win'){
        playerChoiceEl.classList.add('highlight-win');
        computerChoiceEl.classList.add('highlight-lose');
      } else if(playerOutcome === 'lose'){
        playerChoiceEl.classList.add('highlight-lose');
        computerChoiceEl.classList.add('highlight-win');
      } else {
        playerChoiceEl.classList.add('highlight-lose');
        computerChoiceEl.classList.add('highlight-lose');
      }
      setTimeout(() => clearHighlights(), 700);
    }
  
    function updateScoresUI(){
      playerScoreEl.textContent = String(playerScore);
      computerScoreEl.textContent = String(computerScore);
      tiesEl.textContent = String(ties);
      roundNumberEl.textContent = String(roundsPlayed);
    }
  
    function endGame(){
      const userWon = playerScore > computerScore;
      const text = userWon ? `You win the match ${playerScore} — ${computerScore}! 🎉` :
                   (playerScore < computerScore ? `Computer wins ${computerScore} — ${playerScore}.` : `It's a draw ${playerScore} — ${computerScore}.`);
      finalText.textContent = text;
      finalScreen.classList.remove('hidden');

      tryUpdateHighScore(playerScore);
    }

    function playRound(playerMove){
      if(roundsPlayed >= totalRounds) return; 
      const compMove = pickRandom();
      roundsPlayed += 1;
  
      playerChoiceEl.textContent = emoji[playerMove] || playerMove;
      computerChoiceEl.textContent = emoji[compMove] || compMove;
  
      const outcome = decide(playerMove, compMove);
      if(outcome === 'win'){
        playerScore += 1;
        resultEl.textContent = `You win this round! ${playerMove} beats ${compMove}.`;
      } else if(outcome === 'lose'){
        computerScore += 1;
        resultEl.textContent = `You lose this round. ${compMove} beats ${playerMove}.`;
      } else {
        ties += 1;
        resultEl.textContent = `It's a tie — both chose ${playerMove}.`;
      }
  
      highlightResult(outcome);
      updateScoresUI();
  
      const needed = Math.ceil(totalRounds / 2);
      if(playerScore >= needed || computerScore >= needed || roundsPlayed >= totalRounds){
        setTimeout(() => endGame(), 400);
      }
    }
  
    pickButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        if(roundsPlayed >= totalRounds && (playerScore >= Math.ceil(totalRounds/2) || computerScore >= Math.ceil(totalRounds/2))){
          return;
        }
        const move = btn.dataset.move;
        playRound(move);
      });
    });
  
    roundsSelect.addEventListener('change', () => {
      totalRounds = parseInt(roundsSelect.value, 10);
      roundsPlayed = 0;
      playerScore = 0;
      computerScore = 0;
      ties = 0;
      roundTotalEl.textContent = String(totalRounds);
      resetUI();
    });
  
    resetBtn.addEventListener('click', () => {
      totalRounds = parseInt(roundsSelect.value,10);
      roundsPlayed = 0;
      playerScore = 0;
      computerScore = 0;
      ties = 0;
      roundTotalEl.textContent = String(totalRounds);
      resetUI();
    });
  
    newGameBtn.addEventListener('click', () => {
      roundsPlayed = 0;
      playerScore = 0;
      computerScore = 0;
      ties = 0;
      resetUI();
    });

    (function init(){
      totalRounds = parseInt(roundsSelect.value,10);
      roundTotalEl.textContent = String(totalRounds);
      resetUI();
      loadHighScore();
    })();
  
  })();
  