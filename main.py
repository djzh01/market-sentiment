from bs4 import BeautifulSoup
import lxml
import urllib.request
import praw

CLIENT_ID = 'UJjmN-ZQ55bhBQ'
CLIENT_SECRET = 'iEYpDNPE1lhbJBGlDrqfp49wOv4'
USER_AGENT = 'RedditScraper'
USERNAME = 'bluebue6'
PASSWORD = 'Riptide23'

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     password=PASSWORD,
                     user_agent=USER_AGENT, username=USERNAME)

sub = reddit.subreddit('wallstreetbets')

for post in sub.hot(limit=None):
    print(f'{post.created_utc}: {post.title}:{post.score}')

# source = urllib.request.urlopen('https://www.reddit.com/r/news/').read()

# soup = BeautifulSoup(source, 'lxml')

# for paragraph in soup.find_all('h3'):
#   print(str(paragraph.text))
