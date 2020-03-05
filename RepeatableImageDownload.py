from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests
import os


def ImageDownload(url):
    if type(url) is not str:
        print('It should be URL')
        return
    
    with urllib.request.urlopen(url) as response:
        try:
            html = response.read()
        except:
            print("Error: Invalid URL")
            return
        
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


def main():
    entered_url = input('Please Enter URL: ')
    while entered_url != 'QUIT':
        try:
            ImageDownload(entered_url)
        except:
            print("Error Occured")
        entered_url = input('Please Enter URL: ')


if __name__ == '__main__':
    main()
