from pyscript import document

def compute_average(e):
    # Get user inputs
    score1 = float(document.getElementById("score1").value or 0)
    score2 = float(document.getElementById("score2").value or 0)

    # Compute average
    average = (score1 + score2) / 2

    # Display result with pass/fail message
    if average >= 75:
        message = f"Average: {average:.2f} ✅ You Passed!"
    else:
        message = f"Average: {average:.2f} ❌ You Failed!"

    # Displays the result "message" 
    document.getElementById("result").innerHTML = message
