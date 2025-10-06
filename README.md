# AI Deobf

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/Eatgrapes/AI_Deobf)

## Project Overview

AI Deobf is an experimental AI-powered deobfuscator designed to simplify obfuscated code in **JavaScript** and **Java**. It leverages large language models to analyze and reconstruct readable code. 

> **Note**: As with any AI tool, occasional hallucinations (unexpected or incorrect outputs) may occur. Always review the results manually for accuracy.

This project is in early development—contributions and feedback are highly encouraged!

## Features
- Supports deobfuscation for JavaScript and Java code.
- Integrates with popular AI APIs (DeepSeek, Gemini, OpenAI).
- Simple CLI interface for quick usage.
- Extensible design for adding more languages or models.

## Requirements
- Python 3.8 or higher ([Download here](https://www.python.org/downloads/)).
- Access to an AI API key (see [Get AI API](#get-ai-api) below).

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Eatgrapes/AI_Deobf.git
cd AI_Deobf
```

Alternatively, download the ZIP from the [GitHub Releases](https://github.com/Eatgrapes/AI_Deobf/archive/refs/heads/main.zip) page.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Your AI API
Run the initialization script to set up your API key:
```bash
python init.py
```
Follow the prompts to enter your API details (e.g., endpoint, key, model).

### 4. Run the Deobfuscator
```bash
python Main.py
```
- Provide the path to your obfuscated file when prompted.
- Select the language (JavaScript or Java).
- Review the deobfuscated output in the console or generated file.

## Get AI API Keys

To use the tool, you'll need an API key from one of these providers:

- **[DeepSeek](https://platform.deepseek.com/)**
- **[Google Gemini](https://aistudio.google.com/api-keys)**:
- **[OpenAI ChatGPT](https://platform.openai.com/api-keys)**

Sign up, generate a key, and configure it via `init.py`.

## Troubleshooting
- **API Errors**: Ensure your key is valid and has sufficient quota. Check the console for error messages.
- **Dependency Issues**: Use a virtual environment (`python -m venv env && source env/bin/activate` on Unix/Mac or `env\Scripts\activate` on Windows).
- **Python Version**: Verify with `python --version`.

## Found a Bug? 🐛
Help us improve! Report issues on the [GitHub Issues page](https://github.com/Eatgrapes/AI_Deobf/issues). Include details like your OS, Python version, API provider, and a minimal reproducible example.

## Contributing
We'd love your help to expand language support, fix bugs, or enhance the UI. Here's how:

1. Fork the repo and create a feature branch (`git checkout -b feature/amazing-feature`).
2. Commit your changes (`git commit -m 'Add amazing feature'`).
3. Push to the branch (`git push origin feature/amazing-feature`).
4. Open a [Pull Request](https://github.com/Eatgrapes/AI_Deobf/compare) and describe your changes.

Thanks for contributing! 🚀

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
