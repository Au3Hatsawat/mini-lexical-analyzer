## Gemini Prompt

```
ขอ setup project python + lib sly แบบ best practice หน่อยครับ ใช้แค่ lexer พอครับจะทำ Mini Lexical Analyzer
```

```
ตอนนี้ใช้ window อยู่ source .venv/bin/activate  ไม่ได้
source .venv/bin/activate
source : The term 'source' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try 
again.
At line:1 char:1
+ source .venv/bin/activate
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (source:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
```

```
มีเคสหนึ่งคือ ตัว identifier ห้ามขึ้นต้นด้วย ตัวเลข ห้ามใช้ underscore มี regex แนะนำไหม
เพื่อที่จะได้เขียน func ดักก่อนที่จะเข้าเคส identifier
```

```
มันสามารถรวมเคสกันได้ไหม แบบ r'\d+[a-zA-Z][a-zA-Z0-9]* | [a-zA-Z0-9]*_[a-zA-Z0-9_]*'
```

```
class MyLexer(Lexer):

ตัว (Lexer) ที่เป็น เหมือน class รับ args Lexer นี่มันคือการ extend ของ python หรอครับ
```

```
 tokens = {
        # Keywords
        IF, ELSE, WHILE, RETURN, INT_KW, FLOAT_KW,
        # Identifiers & Literals
        ID, FLOAT_LIT, INT_LIT, STRING_LIT,
        # Operators (Multi-char ต้องมาก่อน Single-char)
        EQ, NEQ, LTE, GTE, ASSIGN,
        PLUS, MINUS, TIMES, DIVIDE, LT, GT,
    }

คือถ้าตัว tokens ถูก declare ตรงนี้แล้ว assign ค่าที่เป็ฯ IF , ELSE มันจะ not defined นะ งั้นก็ต้องใส่เป็ฯ 'IF' ไม่ใช่หรอครับ
```

```
attach full code & term-report-1-2569.pdf

ผมไม่ต้องทำ parser ครับอาจารย์ให้ทำตัว mini-lexical-analyzer เฉยๆครับช่วยตรวจให้หน่อยครับว่า requirement ครบรึป่าว
```

```
ขอ gitignore หน่อยครับ
```