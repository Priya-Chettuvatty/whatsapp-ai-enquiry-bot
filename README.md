# whatsapp-ai-enquiry-bot
AI-based WhatsApp Enquiry Assistant using Python &amp; Twilio

This project is a **WhatsApp-based AI Enquiry Assistant** built using Python, Flask, and Twilio.  
It automatically responds to user queries, collects lead details, and guides users through course enrollment.

---Workflow

1. User sends message on WhatsApp  
2. Twilio Sandbox receives message  
3. Webhook sends request to Flask app  
4. Bot processes message  
5. Bot sends reply based on user input
   
---Install Requirements
pip install flask twilio

--Run Application
python app.py

ngrok http 5000

Connect Twilio
Use Twilio Sandbox for WhatsApp

Set webhook URL (using ngrok)
