from flask import Flask, render_template, request, redirect

app = Flask(__name__)

board = [""] * 9
player = "X"

def check_winner():
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] != "":
            return board[w[0]]
    return None

@app.route("/")
def index():
    winner = check_winner()
    return render_template("index.html", board=board, winner=winner, player=player)

@app.route("/move/<int:pos>")
def move(pos):
    global player
    if board[pos] == "" and not check_winner():
        board[pos] = player
        player = "O" if player == "X" else "X"
    return redirect("/")

@app.route("/reset")
def reset():
    global board, player
    board = [""] * 9
    player = "X"
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)