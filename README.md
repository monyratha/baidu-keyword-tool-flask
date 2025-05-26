# Baidu Keyword Extractor 🤖

[English](./README.md) | [简体中文](./README.zh-CN.md)

A Flask web application that extracts related keywords from Baidu search results. This tool helps you discover related terms and suggestions for your keywords by scraping Baidu's mobile search interface.

## Features

- Extract related keywords from Baidu search results
- Support for multiple keywords (one per line)
- Clean and modern UI with dark mode
- Copy results to clipboard functionality
- Secure credential storage in browser's local storage
- Mobile-responsive design

## Requirements

- Python 3.x
- Flask 2.3.3
- Requests 2.31.0
- BeautifulSoup4 4.12.2

## Installation

1. Clone this repository:
```bash
git clone https://github.com/monyratha/baidu-keyword-tool-flask.git
cd baidu-keyword-tool-flask
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Configure your Baidu login credentials:
   - Click on "🔐 Configure Baidu Login"
   - Enter your BAIDUID, BDUSS, and BDORZ cookies from your Baidu account
   - These credentials will be saved in your browser's local storage

4. Enter your keywords (one per line) in the text area

5. Click "🧠 Extract" to get related keywords for each term

6. Use the "📋 Copy" button to copy all results to your clipboard

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # CSS styles (embedded in index.html)
└── templates/
    └── index.html     # Main HTML template
```

## Security Note

This application requires Baidu login credentials (cookies) to function properly. These credentials are:
- Stored securely in your browser's local storage
- Only sent to Baidu's servers
- Never stored on the application server

## License

This project is licensed under the [MIT License](./LICENSE).

> ⚠️ **Note:** This is a personal learning project.  
> I built it to practice Python, Flask, and web scraping.  
> Feel free to explore, learn from it, or improve it.

You're free to use, modify, and distribute this code under the MIT terms.  
See the `LICENSE` file for full details.
