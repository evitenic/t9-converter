from helpers.t9_mapper import convert_text_to_t9, read_file_and_convert

def convert_file():
    input_file = input("📥 Enter file path: ")
    read_file_and_convert(input_file)

def convert_text():
    input_text = input("📝 Enter text: ")
    converted = convert_text_to_t9(input_text)  
    print(f"T9 Result: {converted}")

def menu():
    print("\n========================================")
    print("🔢 T9 Converter Menu 🔢")
    print("========================================")
    print("1. Convert text to t9")
    print("2. Convert file to t9")
    print("0. Exit")
    print("========================================")
    
def main():
    while True:
        menu()

        choice = int(input("\nSelect an option: "))

        if choice == 1:
            convert_text()
        elif choice == 2:
            convert_file()
        elif choice == 0:
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
