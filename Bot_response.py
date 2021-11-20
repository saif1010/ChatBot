import random

R_EATING = "I don't like eating anything because I'm a bot made by my creators Satyam And Saif."
R_ADVICE = "If I were you, I would go to the GOOGLE and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "Pardon",
                "Umm?.",
                "What does that mean?"][
        random.randrange(4)]
    return response