# 📄 PDF to Markdown Converter

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991.svg)](https://openai.com)

A tool that converts PDF documents to Markdown format using OpenAI's vision model for accurate text extraction and formatting.

## ✨ Features

- 📝 Convert PDF files to Markdown format
- ➗ Maintain mathematical equations formatting
- 🈺 Support for Chinese text
- 🖼️ Automatic image processing and handling
- 📊 Progress bar for conversion status

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/AbyssSkb/pdf2md.git
cd pdf2md
```

2. Install dependencies:
```bash
pip install -r pyproject.toml
```

3. Create a `.env` file with your OpenAI configuration:
```env
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=your_base_url
OPENAI_LLM_MODEL=your_model_name
```

## 📖 Usage

1. Place your PDF file in the project directory as `input.pdf`
2. Run the converter:
```bash
python main.py
```
3. Find the converted markdown in `output.md`

## 🛠️ Requirements

- Python 3.10 or higher
- OpenAI API access
- pdf2image
- python-dotenv

> **Note**: pdf2image requires additional system dependencies:
> - On Windows: Install [poppler](https://github.com/oschwartz10612/poppler-windows/releases/)
> - On Linux: `apt-get install poppler-utils`
> - On macOS: `brew install poppler`
>
> For detailed installation instructions, please check [pdf2image documentation](https://github.com/Belval/pdf2image).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
