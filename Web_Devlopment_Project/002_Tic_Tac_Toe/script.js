const cells = document.querySelectorAll(".cell");
const resetButton = document.getElementById("reset");
let currentPlayer = "X";
let board = ["", "", "", "", "", "", "", "", ""];
let gameActive = true;

// Check for win conditions
function checkWinner() {
    const winningPatterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6] // Diagonals
    ];

    for (let pattern of winningPatterns) {
        const [a, b, c] = pattern;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            alert(`${board[a]} wins!`);
            gameActive = false;
            return;
        }
    }

    if (!board.includes("") && gameActive) {
        alert("It's a draw!");
        gameActive = false;
    }
}

// Handle cell clicks
cells.forEach(cell => {
    cell.addEventListener("click", () => {
        const index = cell.getAttribute("data-index");
        if (!board[index] && gameActive) {
            board[index] = currentPlayer;
            cell.textContent = currentPlayer;
            checkWinner();
            currentPlayer = currentPlayer === "X" ? "O" : "X";
        }
    });
});

// Reset game
resetButton.addEventListener("click", () => {
    board.fill("");
    gameActive = true;
    currentPlayer = "X";
    cells.forEach(cell => cell.textContent = "");
});

