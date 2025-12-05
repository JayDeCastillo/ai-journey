import datetime
import random

quotes = [
    "The best way to predict the future is to invest in it.",
    "Code is like humor. When you have to explain it, its bad.",
    "First, solve the problem. Then, write the code.",
    "Make it work, make it right, make it fast",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."
]

today = datetime.date.today().strftime("%B %d, %Y")
quote = random.choice(quotes)

print(f"Date: {today}")
print(f"Daily coding quote for Jay:")
print(f""{quote}"")