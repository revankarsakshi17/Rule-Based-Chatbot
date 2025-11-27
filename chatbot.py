# import tkinter as tk
# from tkinter import scrolledtext
# import random

# # --- Chatbot responses ---
# responses = {
#     "hello": ["Hi there!", "Hello!", "Hey! How’s it going?"],
#     "hi": ["Hello!", "Hi! What can I do for you?", "Hey there!"],
#     "how are you": ["I'm doing great, thanks!", "Feeling chatty today!"],
#     "your name": ["You can call me ChatBot!", "I'm ChatBot, your virtual assistant."],
#     "who are you": ["I'm a simple rule-based chatbot.", "Just a chatbot created using Python!"],
#     "time": ["Time is an illusion for me, but always time to chat!"],
#     "weather": ["I’m not connected to weather data, but I hope it's nice outside!"],
#     "bye": ["Goodbye!", "See you soon!", "Bye! Have a nice day!"]
# }

# # --- Chatbot logic ---
# def get_response(user_input):
#     user_input = user_input.lower()
#     for key in responses:
#         if key in user_input:
#             return random.choice(responses[key])
#     return "I'm not sure I understand. Can you rephrase?"

# # --- Send message function ---
# def send_message():
#     user_input = entry.get()
#     chat_box.insert(tk.END, "You: " + user_input + "\n")
#     entry.delete(0, tk.END)
    
#     if "bye" in user_input.lower():
#         chat_box.insert(tk.END, "ChatBot: Goodbye! 👋\n")
#         root.after(1000, root.destroy)
#         return
    
#     bot_response = get_response(user_input)
#     chat_box.insert(tk.END, "ChatBot: " + bot_response + "\n\n")

# # --- GUI Setup ---
# root = tk.Tk()
# root.title("ChatBot")
# root.geometry("400x500")

# chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='normal', width=50, height=20)
# chat_box.pack(pady=10)

# entry = tk.Entry(root, width=40)
# entry.pack(side=tk.LEFT, padx=10, pady=10)

# send_button = tk.Button(root, text="Send", command=send_message)
# send_button.pack(side=tk.LEFT)

# root.mainloop()


from flask import Flask, render_template, request
import random

app = Flask(__name__)

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How’s it going?"],
    "hi": ["Hello!", "Hi! What can I do for you?", "Hey there!"],
    "how are you": ["I'm doing great, thanks!", "Feeling chatty today!"],
    "your name": ["You can call me ChatBot!", "I'm ChatBot, your virtual assistant."],
    "who are you": ["I'm a simple rule-based chatbot.", "Just a chatbot created using Python!"],
    "bye": ["Goodbye!", "See you soon!", "Bye! Have a nice day!"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure I understand. Can you rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    return get_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)
