from agent.app.services.agent_services import request_agent

from fastapi import APIRouter

router = APIRouter(tags=["Agent"], prefix="/agent")


# http://localhost:8000/agent/message
@router.get("/message")
def message(
    user_message: str, chat_id: str, img_url: str = None, audio_url: str = None
):

    ai_message = request_agent(chat_id=chat_id, message=user_message)

    return ai_message
