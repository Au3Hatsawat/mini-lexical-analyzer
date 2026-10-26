# Mini Lexical Analyzer

โปรแกรมวิเคราะห์คำ (Lexical Analyzer) สำหรับภาษาจำลอง พัฒนาด้วยภาษา Python และไลบรารี [SLY](https://sly.readthedocs.io/) เพื่อสแกนและแยก Source Code จากไฟล์ข้อความ (`.txt`) ออกเป็น Token ประเภทต่าง ๆ ตามข้อกำหนดของโครงงาน

## ฟีเจอร์หลัก (Features)
* **Tokenization:** รองรับการแยก Keywords (พิมพ์เล็กเท่านั้น), Identifiers, Integers, Strings, Operators และสัญลักษณ์ (วงเล็บ, Semicolon)
* **Symbol Table:** บันทึก Identifier ใหม่และตรวจจับ Identifier ที่ซ้ำซ้อน
* **Comment Handling:** ละเว้นการอ่านโค้ดใน Single-line (`//`) และ Block comments (`/* ... */`)
* **Error Detection:** ตรวจจับ Lexical Error (เช่น ตัวอักษรที่ไม่อนุญาต หรือ Identifier ผิดรูปแบบ) แจ้งตำแหน่งที่ผิดพลาด และหยุดการทำงานทันที

## สิ่งที่ต้องมี (Prerequisites)
* Python 3.10 หรือใหม่กว่า
* Git

## การตั้งค่าโปรเจกต์ (Project Setup)

1. **Clone repository และเข้าไปยังโฟลเดอร์โปรเจกต์:**
   ```bash
   git clone <ใส่-URL-ของ-Repository-ที่นี่>
   cd mini-lexer
   ```

2. **สร้างและเปิดใช้งาน Virtual Environment:**
   
   *สำหรับ Windows (PowerShell):*
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
   
   *สำหรับ macOS / Linux:*
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **ติดตั้ง Dependencies:**
   ตรวจสอบว่ามีไฟล์ `requirements.txt` หรือ `pyproject.toml` แล้วรันคำสั่ง:
   ```bash
   pip install -e .
   ```

## วิธีการใช้งาน (Usage)

โปรแกรมถูกออกแบบมาให้รับ Input เป็นไฟล์ข้อความ (`.txt`) รันคำสั่ง `python` ตามด้วยชื่อไฟล์หลักและไฟล์ที่ต้องการทดสอบ:

```bash
mini-lexer ./src/inputs/input_error.txt
# หรือ
python ./src/mini_lexer/main.py ./src/inputs/input-1.txt
```



### ตัวอย่างการทำงาน

**ไฟล์ `input1.txt`:**
```text
read A;
if A >= 10 then
    print "A is greater";
endif
```

**ผลลัพธ์ (Output):**
```text
keyword: read
new identifier: A
semicolon: ;
keyword: if
identifier "A" already in symbol table
operator: >=
integer: 10
keyword: then
keyword: print
string: "A is greater"
semicolon: ;
keyword: endif
```

## โครงสร้างโปรเจกต์ (Project Structure)
```text
mini-lexer/
│
├── mini_lexer/
│   ├── __init__.py
│   ├── main.py 
│   ├── lexer.py          # คลาส MyLexer และกฎ Regular Expression
│   └── helper.py         # ฟังก์ชันช่วยจัดรูปแบบ Output (format_token_output)
├── inputs/               # โฟลเดอร์สำหรับเก็บไฟล์ทดสอบ
│   ├── input_1.txt       # โค้ดที่ถูกต้อง
│   ├── input_2.txt       # โค้ดที่มีเงื่อนไขซับซ้อนขึ้น
│   └── input_error.txt   # โค้ดที่จงใจให้เกิด Lexical Error
├── .gitignore
├── pyproject.toml        # (หรือ requirements.txt) จัดการ dependencies
└── README.md
```