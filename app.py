from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Store user state
user_state = {}

# 🔹 Intent Detection
def detect_intent(msg):
    msg = msg.lower()

    if any(word in msg for word in ["job", "career", "placement", "salary"]):
        return "job"
    elif any(word in msg for word in ["beginner", "start", "new", "no idea"]):
        return "beginner"
    elif any(word in msg for word in ["ai", "machine learning", "data"]):
        return "ai"
    elif any(word in msg for word in ["test", "testing", "qa"]):
        return "testing"
    elif "python" in msg:
        return "python"
    else:
        return "unknown"


# 🔹 Course Reply
def get_course_reply(name, intent):
    if intent == "job":
        return f"""Great {name}! 😊

I understand you're looking for job opportunities.

👉 I recommend our *Testing course*

📘 Duration: 2 months  
💰 Fee: 4000 INR  

Shall I help you enroll?"""

    elif intent == "beginner":
        return f"""Hi {name}! 👋

No worries if you're just starting 👍

👉 Python is the best beginner-friendly course.

📘 Duration: 2 months  
💰 Fee: 5000 INR  

Shall I help you enroll?"""

    elif intent == "ai":
        return f"""Awesome {name}! 🤖

AI is a trending field.

📘 Duration: 3 months  
💰 Fee: 8000 INR  

Shall I help you enroll?"""

    elif intent == "testing":
        return f"""Good choice {name}! 👍

Testing is great for quick IT entry.

📘 Duration: 2 months  
💰 Fee: 4000 INR  

Shall I help you enroll?"""

    elif intent == "python":
        return f"""Nice {name}! 😊

Python is widely used and easy to learn.

📘 Duration: 2 months  
💰 Fee: 5000 INR  

Shall I help you enroll?"""

    else:
        return f"""Hi {name}! 😊

I can help you choose the right course.

👉 Python (Beginner friendly)  
👉 Testing (Job-oriented)  
👉 AI (Advanced)

Tell me your goal (job / beginner / AI)"""


# 🔹 Main Bot
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip()
    user = request.values.get("From")

    resp = MessagingResponse()
    msg = resp.message()

    msg_text = incoming_msg.lower()

    # 🔹 Greeting
    if msg_text in ["hi", "hello", "hey"]:
        user_state[user] = {"step": "ask_name"}
        msg.body("Hello! 😊 Welcome to our institute.\n\nWhat is your name?")
        return str(resp)

    # 🔹 Bot identity
    if "your name" in msg_text:
        msg.body("I'm your AI Enquiry Assistant 🤖. I help you choose the right course.")
        return str(resp)

    # 🔹 Handle enrollment YES/NO
    if user in user_state and user_state[user].get("step") == "confirm_enroll":

        if msg_text in ["yes", "yeah", "y", "ok", "sure"]:
            user_state[user]["step"] = "ask_phone"
            msg.body("Great! 😊 Please share your phone number.")
            return str(resp)

        elif msg_text in ["no", "not now", "later"]:
            msg.body("No problem 👍 You can message me anytime!")
            user_state.pop(user)
            return str(resp)

        else:
            msg.body("Please reply with YES or NO 🙂")
            return str(resp)

    # 🔹 Capture phone number
    if user in user_state and user_state[user].get("step") == "ask_phone":
        user_state[user]["phone"] = incoming_msg

        msg.body(f"Thank you {user_state[user].get('name','')}! 📞\n\nOur team will contact you soon.")

        print("New Lead:", user_state[user])  # for demo

        user_state.pop(user)
        return str(resp)

    # 🔹 Ask name
    if user not in user_state:
        user_state[user] = {"step": "ask_name"}
        msg.body("Hi! 😊 What is your name?")
        return str(resp)

    # 🔹 Save name
    if user_state[user]["step"] == "ask_name":
        user_state[user]["name"] = incoming_msg
        user_state[user]["step"] = "ask_need"
        msg.body(f"Nice to meet you {incoming_msg}! 😊\n\nWhat are you looking for?\n(job / beginner / AI / testing)")
        return str(resp)

    # 🔹 Suggest course
    if user_state[user]["step"] == "ask_need":
        name = user_state[user]["name"]
        intent = detect_intent(incoming_msg)

        if intent == "unknown":
            msg.body("I didn’t understand 🤔\n\nAre you looking for a job or starting as a beginner?")
            return str(resp)

        reply = get_course_reply(name, intent)

        user_state[user]["step"] = "confirm_enroll"
        msg.body(reply)
        return str(resp)

    return str(resp)


if __name__ == "__main__":
    app.run(port=5000)