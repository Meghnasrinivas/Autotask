from typing import Dict, Any

# TODO: Replace with an actual database integration

DATABASE = {
    "chats": [],
    "files": [],
    "agent_responses": [],
    "final_responses": [],
}


def save_chat(user_id: str, query: str) -> str:
    chat_id = f"chat_{len(DATABASE['chats']) + 1}"
    DATABASE['chats'].append({"chat_id": chat_id, "user_id": user_id, "query": query})
    return chat_id


def save_response(chat_id: str, agent_name: str, response_text: str, round_number: int):
    DATABASE['agent_responses'].append({
        "response_id": f"resp_{len(DATABASE['agent_responses']) + 1}",
        "chat_id": chat_id,
        "agent_name": agent_name,
        "response_text": response_text,
        "round_number": round_number,
    })


def save_final(chat_id: str, final_answer: str):
    DATABASE['final_responses'].append({
        "final_id": f"final_{len(DATABASE['final_responses']) + 1}",
        "chat_id": chat_id,
        "final_answer": final_answer,
    })


def get_history(user_id: str):
    return [c for c in DATABASE['chats'] if c['user_id'] == user_id]
