import sys
from mini_lexer.lexer import MyLexer
from mini_lexer.helper import format_token_output

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file.txt>")
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        data = f.read()

    lexer = MyLexer()
    
    for token in lexer.tokenize(data):
        print(format_token_output(token))

if __name__ == '__main__':
   main()