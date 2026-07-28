def get_oath_dialogue(hero):

    return {
        "awakening": (
            f"The ancient chamber trembles...\n\n"
            f"The sleeping soul of **{hero['name']}** begins to awaken.\n\n"
            "\"After countless years of silence...\"\n\n"
            "\"A soul has finally called my name.\""
        ),

        "question": (
            f"**{hero['name']}** opens their eyes.\n\n"
            "\"Wanderer...\"\n\n"
            "\"Why have you awakened me from my eternal sleep?\""
        ),

        "accept": (
            f"The soul of **{hero['name']}** remains silent.\n\n"
            "\"Perhaps fate brought you here.\"\n\n"
            "\"Perhaps our paths were always meant to cross.\"\n\n"
            "The ancient bond begins to form.\n\n"
            "⚔ Our souls shall walk together."
        ),

        "complete": (
            f"✨ The oath has been accepted.\n\n"
            f"**{hero['name']}** has answered your call.\n\n"
            "But the ruins still remain...\n\n"
            "The final trial awaits."
        )
    }