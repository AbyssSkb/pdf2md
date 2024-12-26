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
OPENAI_BASE_URL=your_base_url (optional)
OPENAI_LLM_MODEL=your_preferred_model (default: gpt-4o)
```

## 📖 Usage

The converter supports command-line arguments for input and output files:

```bash
python main.py input.pdf --output output.md
```

Or simply:
```bash
python main.py input.pdf
```

The converted markdown will be saved to the specified output file (defaults to `output.md`).

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
