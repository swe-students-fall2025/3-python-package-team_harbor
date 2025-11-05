import argparse
from . import __version__
from .core import motivational, positive


def create_parser():
    lang_keys = set(POSITIVE_TEMPLATES.keys())
    lang_keys.update(FUNNY_TEMPLATE.keys())
    lang_keys.update(MOTIVATIONAL_TEMPLATES.keys())
    lang_keys.update(NEGATIVE_MOTIVATIONAL.keys())
    languages = sorted(list(lang_keys))
    categories = ["positive", "funny", "motivational", "negative"]
    intensities = ["soft", "medium", "hard"]

    parser = argparse.ArgumentParser(
        description="""Motivational sentences for programmers.""",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-c",
        "--category",
        choices=categories,
        default="motivational",
        help="""Category of the message.
  positive: A positive quote.
  funny: A funny sentence.
  motivational: An earnest motivational message.
  negative: A negatively-toned motivational message.
  (default: motivational)""",
    )

    parser.add_argument(
        "-l",
        "--language",
        choices=languages,
        default="en",
        help=f"""Message language.
  Available: {', '.join(languages)}
  Falls back to 'en' if a language is unsupported
  for a given category.
  (default: en)""",
    )

    parser.add_argument(
        "-i",
        "--intensity",
        choices=intensities,
        default="medium",
        help=f"""Tone intensity.
  Available: {', '.join(intensities)}
  Applies to 'motivational' and 'negative' categories.
  (default: medium)""",
    )

    parser.add_argument(
        "-e",
        "--enthusiasm",
        type=int,
        choices=range(0, 6),
        default=1,
        metavar="{0-5}",
        help="""Controls punctuation (enthusiasm).
  0: ends with a period (.)
  1-5: ends with that many exclamation points (!)
  Applies to 'positive', 'funny', and 'negative' categories.
  (default: 1)""",
    )
    pos_parser.add_argument(
        "-n", "--name",
        help="Person to address.",
    )
    pos_parser.set_defaults(func=positive)
    mot_parser = subparsers.add_parser(
        "motivational",
        help="Get a short motivational message.",
        description="Get a short motivational message.",
    )
    mot_parser.add_argument(
        "-i", "--intensity",
        choices=["soft", "medium", "hard"],
        default="medium",
        help="Intensity/tone of the message (default: medium).",
    )
    mot_parser.add_argument(
        "-n", "--name",
        help="Person to address.",
    )

    parser.add_argument(
        "--seed", type=int, help="Seed for deterministic (test) output."
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"moodsmith {__version__}"
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    message = ""
    try:
        if args.category == "positive":
            message = positive_quote(
                language=args.language,
                name=args.name,
                enthusiasm=args.enthusiasm,
                seed=args.seed,
            )
        elif args.category == "funny":
            message = funny(
                language=args.language,
                name=args.name,
                enthusiasm=args.enthusiasm,
                seed=args.seed,
            )
        elif args.category == "motivational":
            message = motivational(
                language=args.language,
                intensity=args.intensity,
                name=args.name,
                seed=args.seed,
            )
        elif args.category == "negative":
            message = negative(
                language=args.language,
                name=args.name,
                enthusiasm=args.enthusiasm,
                intensity=args.intensity,
                seed=args.seed,
            )

        print(message)

    except Exception as e:
        print(f"An error occurred: {e}")
        parser.print_help()


if __name__ == "__main__":
    main()
