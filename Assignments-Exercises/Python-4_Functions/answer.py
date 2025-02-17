def create_greeting(name: str) -> str:
    return f"Hello, {name}!, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"


def main() -> None:
    try:
        name: str = input("What is your name? ")
        greeting: str = create_greeting(name)
        print(greeting)
    except ValueError:
        print("Invalid input: Please enter a valid name.")


if __name__ == "__main__":
    main()
