import requests
from io import BytesIO
from bs4 import BeautifulSoup as bs
from PIL import Image                                                                                

print("=== Github Webscrapping Project ===")
github_username = input("Enter Github Username: ")
github_url = "https://github.com/" + github_username
r = requests.get(github_url)
soup = bs(r.content, "html.parser")

try:
    # HTML Tag of Profile Picture
    # <img style="height:auto;" alt="" width="260" height="260" 
    # class="avatar avatar-user width-full border color-bg-primary" 
    # src="https://avatars.githubusercontent.com/u/51283594?v=4">
    profile_image = soup.find("img", {"alt" : "Avatar"})["src"]

    # HTML Tag of Follower Count
    # <a class="Link--secondary no-underline no-wrap" href="https://github.com/cyberjj999?tab=followers">
    # <svg class="octicon octicon-people text-icon-tertiary" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M5.5 3.5a2 2 0 100 4 2 2 0 000-4zM2 5.5a3.5 3.5 0 115.898 2.549 5.507 5.507 0 013.034 4.084.75.75 0 11-1.482.235 4.001 4.001 0 00-7.9 0 .75.75 0 01-1.482-.236A5.507 5.507 0 013.102 8.05 3.49 3.49 0 012 5.5zM11 4a.75.75 0 100 1.5 1.5 1.5 0 01.666 2.844.75.75 0 00-.416.672v.352a.75.75 0 00.574.73c1.2.289 2.162 1.2 2.522 2.372a.75.75 0 101.434-.44 5.01 5.01 0 00-2.56-3.012A3 3 0 0011 4z"></path></svg>
    # <span class="text-bold color-text-primary">1</span> follower </a>
    followers_count = soup.find("a", {"href" : github_url + "?tab=followers"}).span.text

    # followers_count = soup.find("span", {"class" : "text-bold"}).text
    # HTML Tag of Following Count
    # <a class="Link--secondary no-underline no-wrap" href="https://github.com/cyberjj999?tab=following">
    # <span class="text-bold color-text-primary">0</span> following </a>
    following_count = soup.find("a", {"href" : github_url + "?tab=following"}).span.text

    # Printing Output
    print("Github User - " + github_username)
    print(" ------------------------- ")
    print("Followers: " + followers_count)
    print("Following: " + following_count)
    print("Profile Picture URL: " + profile_image)
except:
    print("Error! Github User does not Exist!")
