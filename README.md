# PDF Privacy Eraser

**Description:**

The PDF Privacy Eraser is a tool designed to remove sensitive information from PDF documents. It provides a secure and efficient way to redact or delete private data, ensuring that confidential information is not visible to unauthorized individuals.

**Features:**

- **Redaction:** 			Easily redact sensitive text or images within PDF files.
- **Configurable Rules:** 		Customize redaction rules based on keywords, patterns, or specific criteria.
- **Secure Processing:** 		The tool ensures the privacy and security of the redacted information.(mostly)

**Usage:**

1. Clone the repository:
   ```bash
	https://github.com/Musosuke/PrivateDataRedacation.git
	
2. Install dependency
	pip install pathlib
	pip install "paddleocr>=2.0.1"
	pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
	pip install 	json
	pip install 	rapidfuzz
	pip install 	pymupdf
	pip install 	openai
	pip install 	reportlab
	pip install Pillow

3. run
enter working directory, open terminal, type:
	python _main.py

4. input
	type the path of the pdf you want to erase private data
