from bs4 import BeautifulSoup
import requests
import pprint

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

def sort_by_votes(hnlist):
    #sort by votes by descending order
    return sorted(hnlist, key = lambda k:k['votes'], reverse = True)

def create_custom_hacker_news(links, sub_text):
    hn = []
    for index, item in enumerate(links):
        vote = sub_text[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().strip(' points'))
            if points > 150:
                title = links[index].getText()
                href = links[index].get('href', None)
                hn.append({'title':title,'href':href,'votes':points})
    return sort_by_votes(hn)

def scrape_the_page(page_number):
    base_url = 'https://news.ycombinator.com/news?p='+str(page_number)
    # base_url = 'https://news.ycombinator.com/news'
    print(base_url)
    response = requests.get(base_url, headers = headers)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)

    posts = soup.find_all('tr', class_='athing')

    print(len(posts))

    # Check if there's at least one post in the list
    if posts:
        first_post = posts[0]  # Access the first post by its index (0)
        print(first_post.prettify())  # Printing the first post with proper formatting
    else:
        print("No posts found.")

    # Extract the "rank" from the post
    rank = first_post.find('span', class_='rank').get_text().strip()

    # Extract the "title_text" from the post
    # title_text = posts.find('span', class_='titleline').a.get_text().strip()

    # Extract the "url" from the post
    url = posts.find('span', class_='titleline').a['href']

    # Print the extracted information
    print("Rank:", rank)
    print("Title:", title_text)
    print("URL:", url)

    links = soup.select('.storylink')
    print(links)
    sub_text = soup.select('.subtext')

    return create_custom_hacker_news(links, sub_text)

if __name__ == "__main__":
    custom_hn_lists = scrape_the_page(1)
    # pprint.pprint(custom_hn_lists)

