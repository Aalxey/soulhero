def get_challenge_dialogue(
    challenger_name: str,
    challenger_hero: str
):

    return {
        "challenge": (

            "A black raven lands before you and drops "
            "a sealed scroll at your feet.\n\n"

            "The crimson seal breaks on its own...\n\n"

            f"**{challenger_name}, Bearer of {challenger_hero},** "
            "has challenged you to a duel.\n\n"

            "\"Will your soul answer the call?\""

        ),

        "accepted": (

            "The raven lets out one final cry.\n\n"

            "The ancient seal burns away.\n\n"

            "The battlefield has acknowledged your answer."

        ),

        "declined": (

            "The scroll burns into black ash.\n\n"

            "The raven disappears into the darkness.\n\n"

            "This duel shall never take place."

        )
    }