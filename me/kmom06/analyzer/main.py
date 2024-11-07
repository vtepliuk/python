"""
A simple program to analyze text
"""
import analyzer

def main():
    """Main function of the analyzer program."""
    current_file = "phil.txt"
    content = ""

    while True:
        # Load content from the current file at the start of the loop
        try:
            with open(current_file, 'r') as file:
                content = file.read()
            print(f"Loaded content from {current_file}")
        except FileNotFoundError:
            print(f"File {current_file} not found.")
            continue

        print("lines) Count lines")
        print("words) Count words")
        print("letters) Count letters")
        print("word_frequency) Find 7 most used words")
        print("letter_frequency) Find 7 most used letters")
        print("all) Do everything")
        print("change) Change file")
        print("q) quit")

        choice = input("Enter command: ").strip().lower()

        if choice == "q":
            break

        if choice == "change":
            new_file = input("Enter the new file name (phil.txt or lorum.txt): ").strip()
            try:
                with open(new_file, 'r') as file:
                    content = file.read()  # Read the new file's content immediately
                    current_file = new_file
                    print(f"File changed to {current_file}")
                    print(f"New content length: {len(content)}")
            except FileNotFoundError:
                print(f"File {new_file} not found. Please try again.")
            continue

        # Debugging: Print the current file and content length
        print(f"Current file: {current_file}")
        print(f"Content length: {len(content)}")

        # Execute the chosen command
        if choice == "lines":
            print(analyzer.count_lines(content))
        elif choice == "words":
            print(analyzer.count_words(content))
        elif choice == "letters":
            print(analyzer.count_letters(content))
        elif choice == "word_frequency":
            for word, count, percent in analyzer.word_frequency(content):
                print(f"{word}: {count} | {percent}%")
        elif choice == "letter_frequency":
            for letter, count, percent in analyzer.letter_frequency(content):
                print(f"{letter}: {count} | {percent}%")
        elif choice == "all":
            print(analyzer.count_lines(content))
            print(analyzer.count_words(content))
            print(analyzer.count_letters(content))
            for word, count, percent in analyzer.word_frequency(content):
                print(f"{word}: {count} | {percent}%")
            for letter, count, percent in analyzer.letter_frequency(content):
                print(f"{letter}: {count} | {percent}%")
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
