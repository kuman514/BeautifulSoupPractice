from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests
import os


def main():
    url = "https://twitter.com/kumankoishi"
    
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
            
            lnk = source[source_index:]
            print(lnk)
            
            try:
                with open(os.path.basename(lnk), "wb") as f:
                    f.write(requests.get(lnk).content)
            except:
                print("Error Occured")
                print("Pass This Link: " + lnk)


if __name__ == '__main__':
    main()
