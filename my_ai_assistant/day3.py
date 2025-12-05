from datetime import datetime

print("JayDeCastillo's Personal AI Assistant v0.1")
print(f"Today: {datetime.now().strftime('%B %d, %Y %H:%M')}\n")

# Load what the AI knows about JayDeCastillo
with open("knowledge.txt", encoding="utf-8") as f:
    knowledge = f.read().strip()
print ("JayDeCastillo's Personal AI Assistant is ready!\n")

while True:
    question = input("Ask me anything about JayDeCastillo (or type 'quit'):").strip()

    if question.lower() in ["quit,", "exit", "bye", "q"]: 
        print("See you later, boss!")
        break
    if not question:
        continue
    if question.lower() in knowledge.lower():
        print("Yes - that's 100% true about JayDeCastillo!")
    else:
        print("I don't know that yet... teach me?")