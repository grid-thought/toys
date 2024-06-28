import time

def rainbow_text(text):
    rainbow_colors = [
        "\033[91m",  # Red
        "\033[93m",  # Yellow
        "\033[92m",  # Green
        "\033[96m",  # Cyan
        "\033[94m",  # Blue
        "\033[95m"   # Purple
    ]
    reset_color = "\033[0m"

    while True:
        for color in rainbow_colors:
            print(f"{color}{text}{reset_color}", end='\r', flush=True)
            time.sleep(0.1)

if __name__ == "__main__":
    user_input = input("Enter text: ")
    rainbow_text(user_input)