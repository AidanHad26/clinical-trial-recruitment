
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

## Examples of Output

**Example 1**

Post: Wouldn’t it be a bummer if you were in the placebo group tho?

Sentiment Score: -0.3818

Generated Message: ChatCompletionMessage(content='I understand your concerns about being in the placebo group, but your participation in a clinical trial could still make a meaningful difference in advancing medical research and improving treatments for others. Your contribution is valuable, and who knows, you might end up receiving the experimental treatment that could benefit you as well. Your participation could potentially lead to important breakthroughs in healthcare. Thank you for considering being a part of this important journey.', role='assistant', function_call=None, tool_calls=None)

**Example 2**

Post: Thank you so much. I figure the more of us that can help advance the science behind obesity and weight loss, the better off we’ll all be. Plus we might just get a great weight loss drug for free. 💕

Sentiment Score: 0.8979

Generated Message: ChatCompletionMessage(content="That's such an amazing attitude! Your willingness to contribute to the advancement of obesity and weight loss research is truly commendable. Your participation in a clinical trial could not only benefit you personally but also countless others in the future. Thank you for your positivity and enthusiasm - it's people like you who help drive progress and bring us closer to groundbreaking discoveries. 💕Would you consider joining a clinical trial to help make a difference?", role='assistant', function_call=None, tool_calls=None)
