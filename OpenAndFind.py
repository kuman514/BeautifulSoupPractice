from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


def main():
    url = "https://github.com/kuman514"
    
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        
        # crawl all img tags in the requested html
        all_imgs = soup.find_all("img")
        print(all_imgs)
        
        for img in soup.find_all("img"):
            source = img.get('src')
            if source is None:
                continue
            
            source_index = source.find('http')
            if source_index == -1:
                continue
            
            print(source[source_index:])


if __name__ == '__main__':
    main()
