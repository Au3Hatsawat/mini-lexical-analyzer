def format_token_output(token):
    operators = {
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN', 
        'GT', 'GE', 'LT', 'LE', 'EQ', 'INCREMENT', 'DECREMENT'
    }
    
    keywords = {
        'IF', 'THEN', 'ELSE', 'ENDIF', 'WHILE', 'DO', 
        'ENDWHILE', 'PRINT', 'NEWLINE', 'READ'
    }

    display_map = {
        'IDENTIFIER': 'new identifier',
        'LPAREN': 'left parenthesis',
        'RPAREN': 'right parenthesis',
        'SEMICOLON': 'semicolon',
        'INTEGER': 'integer',
        'STRING': 'string'
    }

    if token.type in operators:
        label = 'operator'
    elif token.type in keywords:
        label = 'keyword'
    else:
        label = display_map.get(token.type, token.type.lower())

    return f"{label}: {token.value}"