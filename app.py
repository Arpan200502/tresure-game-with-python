from flask import Flask, render_template, request

app = Flask(__name__)


# Function to handle game logic based on user input
def game_logic(stage, user_input):
    if stage == "start":
        if user_input.lower() == "left":
            return "lake", "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across."
        else:
            return "end", "You fell into a hole. Game Over."

    elif stage == "lake":
        if user_input.lower() == "wait":
            return "doors", "You arrive at the island unharmed. There is a house with 3 doors: red, yellow, and blue. Which colour do you choose?"
        else:
            return "end", "You got attacked by an angry trout. Game Over."

    elif stage == "doors":
        if user_input.lower() == "yellow":
            return "end", "CONGRATS! You found the treasure. You Win!"
        elif user_input.lower() == "red":
            return "end", "It's a room full of fire. Game Over."
        elif user_input.lower() == "blue":
            return "end", "You enter a room of beasts. Game Over."
        else:
            return "end", "You chose a door that doesn't exist. Game Over."

    return "end", "Invalid choice. Game Over."


@app.route("/", methods=["GET", "POST"])
def game():
    stage = "start"
    output = "You're at a crossroad, where do you want to go? Type 'left' or 'right'."

    if request.method == "POST":
        stage = request.form.get("stage", "start")
        user_input = request.form.get("user_input", "").strip()
        stage, output = game_logic(stage, user_input)

    return render_template("index.html", output=output, stage=stage)


if __name__ == "__main__":
    app.run(debug=True)
