import os

T9_KEY_MAPPING = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': [' ']
}

def convert_text_to_t9(text: str) -> str:
    """Convert text to t9

    Args:
        text (str): plain text

    Returns:
        str: t9 text
    """

    result = []

    for character in text.lower():
        for key, letters in T9_KEY_MAPPING.items():
            if character in letters:
                position = letters.index(character) + 1
                if key == '0':
                    result.append(f"{key}")
                else:
                    result.append(f"{key}{position}")

    return ','.join(result)

def read_file_and_convert(input_file: str) :
    """Read input file, convert to T9, and save to auto-named output file"""

    try:
        with open(input_file, 'r', encoding="utf-8") as f:
            content = f.readlines()
        
        converted_lines = []
        for line in content:
            striped_line = line.strip()
            if striped_line:
                converted_line = convert_text_to_t9(striped_line) + "\n"
                converted_lines.append(f"{striped_line}:\n{converted_line}\n")
            else:
                converted_lines.append("\n")

        # Generate output filename
        base_name, ext = os.path.splitext(input_file)
        output_file = f"{base_name}_converted{ext}"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(converted_lines)
        
        print(f"✅ Success! Converted file saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")