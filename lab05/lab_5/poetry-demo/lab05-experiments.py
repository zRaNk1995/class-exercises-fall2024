import requests
from bs4 import BeautifulSoup



def main():
    url = "https://new.cs.unca.edu/"
    print("hello world")
    # user_agent makes it seem like the request is coming from a web browser (versus a bot)
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get("https://new.cs.unca.edu/", headers=user_agent)
    print(response.content)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the anchor tags (<a>) and extract the href attribute (URLs)
        links = soup.find_all('a')

        # Output all URLs found on the page
        for link in links:
            href = link.get('href')
            if href:  # Some <a> tags may not have an href attribute
                print(href)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")



if __name__ == "__main__":
    main()
