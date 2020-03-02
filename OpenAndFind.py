from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


def main():
    with urllib.request.urlopen("https://github.com/kuman514") as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        
        # crawl all img tags in the requested html
        all_imgs = soup.find_all("img")
        print(all_imgs)


if __name__ == '__main__':
    main()
