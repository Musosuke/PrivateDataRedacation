# PDF Privacy Eraser

**Description:**

The PDF Privacy Eraser is a tool designed to remove sensitive information from PDF documents. It provides a secure and efficient way to redact or delete private data, ensuring that confidential information is not visible to unauthorized individuals.

**Features:**

- **Redaction:** 			Easily redact sensitive text or images within PDF files.
- **Configurable Rules:** 		Customize redaction rules based on keywords, patterns, or specific criteria.
- **Secure Processing:** 		The tool ensures the privacy and security of the redacted information.(mostly)

**Usage:**

### 1. Clone the repository

```bash
git clone https://github.com/Musosuke/PrivateDataRedaction.git
```

### 2\. Install dependencies


```bash
pip install pathlib
pip install "paddleocr>=2.0.1"
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install json
pip install rapidfuzz
pip install pymupdf
pip install openai
pip install reportlab
pip install Pillow
```

### 3\. Run the program

Navigate to the working directory in the terminal and type:


```bash
python _main.py
```

### 4\. Input

Type the path of the PDF file you want to redact private data from.
