from pydantic import BaseModel, Field
from typing import Optional


# 1. Lo que RECIBIMOS de n8n
class AgentRequest(BaseModel):
    message: str = Field(..., examples=["Hola, para cotizar una torta"])
    img_b64: Optional[str] = None


# 2. Lo que ENVIAMOS de vuelta a n8n
class AgentResponse(BaseModel):
    # La respuesta final que generó el Agente
    reply: str

    # Opcional: El estado del bot o qué herramientas usó (útil para debugear)
    status: str = "success"
