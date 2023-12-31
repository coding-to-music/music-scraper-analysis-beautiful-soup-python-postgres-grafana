from bs4 import BeautifulSoup
import requests
import pprint

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}


def create_custom_hacker_news(links, sub_text):
    hacker_news = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        points = sub_text[idx].select(".score")
        if len(points):
            points = int(points[0].getText().replace(" points", ""))
        else:
            points = 0
        hacker_news.append({"title": title, "link": href, "points": points})
    return hacker_news


def scrape_the_page(page_number):
    base_url = "https://news.ycombinator.com/news?p=" + str(page_number)
    # base_url = 'https://news.ycombinator.com/news'
    print(base_url)
    response = requests.get(base_url, headers=headers)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")

    posts = soup.find_all("tr", class_="athing")

    print(len(posts))

    print(posts[1].prettify())

    hacker_news_data = []

    for post in posts:
        # Extract the "rank" from the post
        rank = post.find("span", class_="rank").get_text().strip()

        # Check if the "storylink" element exists before accessing the title
        title_element = post.find("a", class_="storylink")
        title_text = (
            title_element.get_text().strip() if title_element else "No Title Found"
        )

        # Extract the "url" from the post
        url = title_element["href"] if title_element else "#"

        hacker_news_data.append({"rank": rank, "title": title_text, "url": url})

    # Print the extracted information
    pprint.pprint(hacker_news_data)

    links = soup.select(".storylink")
    print(links)
    sub_text = soup.select(".subtext")

    return create_custom_hacker_news(links, sub_text)


if __name__ == "__main__":
    custom_hn_lists = scrape_the_page(1)
