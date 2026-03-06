from agent.app.models.schemas import AgentRequest
from agent.app.services.agent_services import request_agent

from fastapi import APIRouter

router = APIRouter(tags=["Agent"], prefix="/agent")


# http://localhost:8000/agent/message
@router.post("/{chat_id}/conversation")
def message(chat_id, form_data: AgentRequest):
    data = {"chat_id": chat_id, "data": form_data.model_dump()}
    ai_message = request_agent(data)
    return ai_message
