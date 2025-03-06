# AI-Powered Web Page Summarization

This project demonstrates how to summarize web pages by harnessing the power of AI using the DeepSeek API. The script fetches a web page's content, cleans it using BeautifulSoup, and then generates a summary. For reference and comparison, the code also includes commented-out sections for using the OpenAI API.

## Features

- **Web Content Extraction:** Retrieves and cleans web page content using BeautifulSoup.
- **AI Summarization:** Generates summaries using the DeepSeek API.
- **Extensible Framework:** Includes commented-out code for using the OpenAI API as an alternative.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `python-dotenv`
  - `IPython`
  - `deepseek`

## Installation

1. **Clone the Repository:**

   ```bash
   git clone git@github.com:nigavictor/ai-powered-web-page-summarization.git
   cd ai-powered-web-page-summarization
2. **Install Required Libraries:**
You can install the necessary packages using pip:

   ```
   pip install requests beautifulsoup4 python-dotenv IPython deepseek
   ```
## Setup
1. **API Key Configuration:**

Create a .env file in the root directory of the repository. This file should contain your DeepSeek API key in the following format:
   ```
   DEEPOSEEK_API_KEY=sk-proj-<your_key_here>
   ```
    
Make sure your API key starts with sk-proj- as required by the script.

2. **(Optional) Using the OpenAI API:**

If you wish to use the OpenAI API instead, uncomment the corresponding sections in the code and update your .env file with your OpenAI API key (ensuring you follow the appropriate key format).

## Usage
The script is designed to be run as a Python script or within a Jupyter Notebook environment.

- **Running as a Script:**

Simply run the Python file:
```
python "AI-Powered Web Page Summarization.py"
```

- **Within a Jupyter Notebook:**

You can open the Jupyter Notebook version of this file and run the cells to see interactive outputs.

The script demonstrates summarizing multiple web pages by calling the display_summary() function on several URLs.

## Code Overview
- **Website Class:**
Fetches the web page content and cleans it by removing unnecessary elements such as scripts, styles, images, and input fields.
- **Summarization Function:**
Uses the DeepSeek API (or optionally the OpenAI API) to generate a summary based on the processed web page content.
- **Display Function:**
Utilizes IPython's Markdown display to render the summary in a user-friendly format.

## Contributing
Feel free to fork this repository and adapt it to your needs. Contributions and improvements are welcome!

## License
This project is open source and available under the MIT License.
