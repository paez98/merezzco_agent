from langchain.tools import tool


@tool
def cotizar_torta(personas: int, fecha: str, tematica: str) -> str:
    """
    Genera una cotización base según número de personas.
    Usar cuando el cliente proporcione:
    - Número de personas
    """

    options = [
        {"max": 8, "recomendacion": "Mini Cake", "precio": "Desde 16$"},
        {"max": 15, "recomendacion": "Torta pequeña", "precio": "Desde 32$"},
        {"max": 20, "recomendacion": "Torta mediana", "precio": "Desde 44$"},
        {"max": 30, "recomendacion": "Torta grande", "precio": "Desde 58$"},
    ]

    recomendacion = "Torta de 2 pisos"
    precio = "Desde 95$"

    for option in options:
        if personas <= option["max"]:
            recomendacion = option["recomendacion"]
            precio = option["precio"]
            break

    return f"""
    🤎 Para {personas} personas te recomendamos una {recomendacion}.

    💰 Precio base: {precio}

    Incluye diseño personalizado, relleno, caja y vela✨
    """
