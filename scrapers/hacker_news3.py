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

    athing_elements = soup.find_all('tr', class_='athing')

    print(len(athing_elements))

    # Print the results
    # for element in athing_elements:
    #     print(element.prettify())  # Use prettify() to display the element nicely formatted
    #     print("------------")
    
    link_element = element.find('a', class_='storylink')
    if link_element:
        print("Link:", link_element['href'])

    # links = soup.select('.storylink')
    # print(links)
    # sub_text = soup.select('.subtext')

    return create_custom_hacker_news(links, sub_text)

if __name__ == "__main__":
    custom_hn_lists = scrape_the_page(1)
    pprint.pprint(custom_hn_lists)

