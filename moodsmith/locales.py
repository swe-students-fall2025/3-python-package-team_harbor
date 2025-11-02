"""Holds message templates for positive_quote()."""

POSITIVE_TEMPLATES = {
    "es": [
        (
            "Steve Jobs dijo que una computadora enseña a todos a pensar, "
            "y de hecho estás pensando{punct}"
        ),
        "Estás haciendo un trabajo excelente{punct}",
        "Los pequeños pasos se suman, y sin duda tú estás sumando{punct}",
        "Me encanta el progreso{punct} - Sigue adelante",
    ],
    "en": [
        (
            "Steve Jobs said a computer teaches everyone to think, "
            "and you are indeed thinking{punct}"
        ),
        "You are doing a great job{punct}",
        "Tiny steps add up, and you are certainly adding{punct}",
        "Love the progress{punct} - Keep going",
    ],
    "fr": [
        (
            "Steve Jobs disait qu'un ordinateur apprend à chacun à penser, "
            "et vous êtes effectivement en train de penser{punct}"
        ),
        "Vous faites un excellent travail{punct}",
        "Les petits pas s'accumulent, et vous y contribuez certainement{punct}",
        "J'adore les progrès{punct} - continuer toujours",
    ],
}

MOTIVATIONAL_TEMPLATES = {
    "en": {
        "soft": [
            "Progress, not perfection—ship the next small improvement.",
            "You're learning every time the code runs, even when it fails.",
            "Tiny commits today become big momentum tomorrow.",
            "Be kind to yourself—debugging takes patience.",
            "Every clean refactor is a gift to your future self.",
        ],
        "medium": [
            "Mastery is built on reps—write, test, repeat.",
            "Feedback is fuel; tests are the engine.",
            "If you can explain it, you can build it.",
            "Read the errors like clues, not verdicts.",
            "When in doubt, make it smaller and make it pass.",
            "Experience is the name everyone gives to their mistakes. - Oscar Wilde",
            "If, at first, you do not succeed, call it version 1.0. ― Khayri R.R. Woulfe",
            "Confusion is part of programming. ― Felienne Hermans"
        ],
        "hard": [
            "Courage is a green test after a brutal red.",
            "You don't need perfect—ship, learn, iterate.",
            "Make the diff. Review. Improve. Repeat.",
            "If it hurts, automate it. If it breaks, test it.",
            "Discipline beats inspiration: show up and push a commit.",
            "It's not a bug; it's an undocumented feature. - Grace Hopper",
            "Talk is cheap. Show me the code. ― Linus Torvalds"
        ],
    }
}
