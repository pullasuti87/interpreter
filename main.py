import getpass
from src.repl import repl


def main():
    try:
        user = getpass.getuser()
    except Exception as e:
        print(f"user error: {e}")
        return

    print(f"hello {user}! this is the fairytale language!")
    print("press something!")

    repl.start()


if __name__ == "__main__":
    main()
