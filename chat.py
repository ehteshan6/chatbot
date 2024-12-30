from tkinter import*
from datetime import datetime

# GUI setup
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#00008B"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
    user_message = e.get().strip()  # Get input and remove extra spaces
    if not user_message:  # Ignore empty messages
        return
    
    txt.insert(END, f"\nYou ({get_time()}): {user_message}")
    e.delete(0, END)

    # Chatbot responses
    user_message = user_message.lower()

    if user_message in ["hello", "hi", "hii", "hiiii"]:
        bot_response("Hi there, how can I help?")
    elif user_message in ["how are you", "how's it going"]:
        bot_response("I'm just a bot, but I'm doing great! How about you?")
    elif user_message in ["fine", "i am good", "i'm doing good", "i'm fine"]:
        bot_response("That's awesome! How can I assist you?")
    elif user_message in ["thanks", "thank you", "thanks a lot"]:
        bot_response("You're welcome! Let me know if there's anything else.")
    elif user_message in ["what do you sell", "what kinds of items are there", "do you have something"]:
        bot_response("I sell books and pens. Let me know if you'd like more info!")
    elif user_message in ["tell me a joke", "tell me something funny", "crack a joke"]:
        bot_response("What is a room with no walls? A mushroom! 🍄")
    elif user_message in ["goodbye", "bye", "see you later", "see yaa"]:
        bot_response("Goodbye! Have a great day!")
    elif user_message in ["who are you", "what is your purpose"]:
        bot_response("I am Ekari, your personal assistant chatbot.")
    elif user_message in ["your name", "what is your name"]:
        bot_response("I'm Ekari, your friendly chatbot.")
    elif user_message in ["who developed you", "who made you", "who created you"]:
        bot_response("I was developed by Wahid Alam.")
    elif user_message in ["clear chat", "clear", "reset"]:
        txt.delete(1.0, END)
        bot_response("Chat cleared! How can I help you now?")
    else:
        bot_response("Sorry, I didn't understand that. Could you rephrase?")

def bot_response(response):
    """Insert the bot's response into the chat window."""
    txt.insert(END, f"\nBot ({get_time()}): {response}")

def get_time():
    """Return the current time in HH:MM format."""
    return datetime.now().strftime("%H:%M")

def on_enter_key(event):
    """Send message when the Enter key is pressed."""
    send()

# GUI Layout
Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Chatbot - Ekari", font=FONT_BOLD, pady=10, width=20).grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60, height=20, wrap=WORD)
txt.grid(row=1, column=0, columnspan=2, pady=10)

scrollbar = Scrollbar(txt, command=txt.yview)
txt['yscrollcommand'] = scrollbar.set
scrollbar.pack(side=RIGHT, fill=Y)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0, pady=10, padx=10)

Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).grid(row=2, column=1, pady=10)

# Bind Enter key to send messages key val
root.bind("<Return>", on_enter_key)

root.mainloop()
