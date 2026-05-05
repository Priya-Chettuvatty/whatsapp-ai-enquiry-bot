# whatsapp-ai-enquiry-bot
AI-based WhatsApp Enquiry Assistant using Python &amp; Twilio

This project is a **WhatsApp-based AI Enquiry Assistant** built using Python, Flask, and Twilio.  
It automatically responds to user queries, collects lead details, and guides users through course enrollment.

---Workflow

User sends WhatsApp message
        ↓
Twilio Sandbox receives message
        ↓
Flask server processes request
        ↓
Python chatbot logic checks user message
        ↓
Bot generates response
        ↓
Twilio sends reply back to WhatsApp user
   
---Install Requirements
pip install flask twilio

--Run Application
python app.py

ngrok http 5000

Connect Twilio
Use Twilio Sandbox for WhatsApp

Set webhook URL (using ngrok)
