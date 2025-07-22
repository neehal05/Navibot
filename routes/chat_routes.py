# routes/chat_routes.py
from flask import Blueprint, render_template, request, jsonify
from bot.logic import get_bot_response

chat_bp = Blueprint('chat', __name__)

@chat_bp.route("/")
def index():
    # Render the chatbot interface
    return render_template("chat.html")    

@chat_bp.route("/get_respones/", methods=["POST"])
def get_response():
    try:
        data = request.get_json()
        user_input = data.get("message", "I Am Neehal")
        response = get_bot_response(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
