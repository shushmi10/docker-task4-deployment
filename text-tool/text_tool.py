def to_upper(s): return s.upper()
def reverse(s):  return s[::-1]
def word_count(s): return len(s.split())

def main():
    print("Text Toolkit")
    print("Options: 1) Uppercase  2) Reverse  3) Word-count  4) Quit")
    while True:
        choice = input("Choose [1-4]: ").strip()
        if choice == "4":
            print("Bye!")
            break
        text = input("Enter text: ")
        if choice == "1":
            print(to_upper(text))
        elif choice == "2":
            print(reverse(text))
        elif choice == "3":
            print(f"Words: {word_count(text)}")
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
