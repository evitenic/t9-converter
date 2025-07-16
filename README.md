# 🔢 T9 Text Converter 

A Python tool that converts text or files into T9 keypad sequences (like old mobile phone typing).

## ✨ Features
- Convert text to T9 format (e.g., "hello" → `42,32,53,53,63`)
- Process entire text files while preserving line breaks
- Clean menu interface with error handling
- Automatic output file naming

## 🛠️ Installation
1. Clone the repository:
```bash
git clone https://github.com/evitenic/t9-converter.git
```
2. Navigate to project directory:
```bash
cd t9-converter
```

## 🚀 Usage
Run the converter:
```bash
python t9_converter.py
```

### Menu Options
```
========================================
           🔢 T9 Converter Menu          
========================================
1. Convert Text to T9
2. Convert File to T9
0. Exit
========================================
```

### Examples
**Text Conversion:**
```
Enter text: hello world
T9 Result: 42,32,53,53,63,0,91,63,73,53,31
```

**File Conversion:**
```
Enter file path: message.txt
✅ Success! Converted file saved as 'message_converted.txt'
```

## 📝 Requirements
- Python 3.xx
- No external dependencies

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

## 📜 License
[MIT](LICENSE)

## TODO
- Support for special characters
- Support for number