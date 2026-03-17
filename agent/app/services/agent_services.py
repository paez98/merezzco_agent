from agent.app.llm.model import agente


def extract_message(ai_msg: dict):
    if isinstance(ai_msg, dict):
        messages = ai_msg.get("messages")
        return messages[-1]


def request_agent(form_data: dict):
    message = form_data.get("data").get("message")
    chat_id = form_data.get("chat_id")

    if form_data.get("data").get("img_b64"):
        img = form_data.get("data").get("img_b64")
        ai_msg = agente.generate(chat_id, message, img)

    else:
        ai_msg = agente.generate(chat_id, message)

    response = extract_message(ai_msg=ai_msg)
    text = response.content

    # Si es una lista, extraemos el texto del primer bloque
    if isinstance(text, list):
        text = text[0].get("text", "")

    cln_response = text.replace("¿", "")
    cln_response = cln_response.replace("¡", "")

    return cln_response
