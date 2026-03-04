from pydantic import BaseModel, Field
from typing import Optional


# 1. Lo que RECIBIMOS de n8n
class AgentRequest(BaseModel):
    # El mensaje de texto que envió el cliente
    message: str = Field(..., example="Hola, ¿tienen pan de jamón?")

    # El ID de la conversación (su número de WhatsApp)
    # Lo usaremos para que el bot tenga memoria por separado para cada cliente
    chat_id: str = Field(..., examples=["15551234567"])

    # Opcional: El nombre del cliente si n8n lo tiene disponible
    user_name: Optional[str] = Field(None, example="Adrián")


# 2. Lo que ENVIAMOS de vuelta a n8n
class AgentResponse(BaseModel):
    # La respuesta final que generó el Agente
    reply: str

    # Opcional: El estado del bot o qué herramientas usó (útil para debugear)
    status: str = "success"
