from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import json
import os
from dotenv import load_dotenv
from openai import OpenAI

#creating the scraping driver
options = Options()

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

driver.fullscreen_window()
driver.implicitly_wait(10)

#two possible subreddits related to clinical trials for reproducibility

url = 'https://www.reddit.com/r/Semaglutide/comments/12tlj2m/clinical_trials_for_glp1_obesity_meds_actively/'
#url = 'https://www.reddit.com/r/AskReddit/comments/88a853/people_who_took_part_in_failed_clinical_trials/'
driver.get(url)
   
try:
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)
    while True:
        more_comments_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'View more comments')]"))
        )
        more_comments_button.click()
        time.sleep(2)  

except Exception as e:
    print("Error or no more 'View more comments' button found:", e)

reddits = {}
posts_data=[]

posts = driver \
    .find_elements(By.CSS_SELECTOR,'[id^="-post-rtjson-content"]') 

for post in posts:
    try:
        text_content = post.text
        if text_content:  
            posts_data.append(text_content)
    except:
        continue  

reddits['posts'] = posts_data

driver.quit() #end of scraping

#creating json file
with open('subreddit.json', 'w', encoding='utf-8') as file:
    json.dump(reddits, file, indent=4, ensure_ascii=False)

#packages for sentiment analysis
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))

#function to get text ready for sentiment analysis 
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

#sentiment analysis of all posts collected
sentiments = []
for post in posts_data:
    preprocessed_text = preprocess_text(post)
    sentiment_score = sia.polarity_scores(preprocessed_text)
    sentiments.append(sentiment_score)

#loading api key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

#function to generate personalized message
def generate_message(user_post, sentiment):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "Write a personalized message to engage users about participating in a clinical trial based on their sentiment and post."},
          {"role": "user", "content": f"{user_post}. Sentiment: {sentiment}"}
      ],
      max_tokens=150
    )
    return response.choices[0].message

#loop to test the function on the first five posts 
for post, sentiment in zip(posts_data[:5], sentiments[:5]):
    sentiment_label = 'neutral'
    if sentiment['compound'] > 0.05:
        sentiment_label = 'positive'
    elif sentiment['compound'] < -0.05:
        sentiment_label = 'negative'

    # Generating message for the post based on its sentiment
    generated_message = generate_message(post, sentiment_label)
    print(f"Post: {post}")
    print(f"Sentiment Score: {sentiment['compound']}")
    print(f"Generated Message: {generated_message}")
    print("------------------------------")