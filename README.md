
# Clinical Trial Recruitment

Reddit Scraping, Sentiment Analysis, and Personalized Messaging for Clinical Trial
Recruitment


## Prerequisites

Before you begin, ensure that you have the following installed
- Python 3.8 or higher
- Selenium
- NLTK
- WebDriver Manager for Chrome
- OpenAI API key

## Installation

1. Clone the repository
```bash
  git clone https://github.com/AidanHad26/clinical-trial-recruitment.git
  cd clinical-trial-recruitment
```
2. Set Up Python Environment
```bash
python -m venv venv
source venv/bin/activate
```
3. Install Required Packages
```bash
pip install -r packages.txt
```
4. Set Up an OpenAI API Key
- Obtain an API key from OpenAI
- Create a `.env` file in the root directory of this project and add the API key:
```
OPENAI_API_KEY = your_api_key_here
```
5. Run the script
```bash
python scraper_mgenerator.py
```
## Output
Due to OpenAI token restraints, the script outputs the first five user posts, their associated sentiment scores, and their personalized messages to the console. 

## Methodology
- Scraping: Used Selenium to scrape Reddit posts from specified URLS to capture post content. This content is placed into a JSON file. 
- Sentiment Analysis: Applied NTLK's VADER to analyze the sentiment of each post.
- Message Generation: Used OpenAI API to generate personalized mesages based on the sentiment of the posts

## Future Improvements
With more time and information, I would have liked to better personalize messages. For example, based on what the Reddit post says (identify key words), I would like to include specifc information in the generated message tailored to the individual. This could be things like when or where the next clinical trial is being held.