from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests
import os


def ImageDownload(id):
    if type(id) is not str:
        print('It should be ID')
        return

    url = 'https://twitter.com/' + id + '/media'
    download_id = 'twitter_' + id

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

            # save all avalible imgs in the twitter ID folder
            if not os.path.isdir(download_id):
                os.mkdir(download_id)

            try:
                print('Downloading ' + os.path.basename(lnk))
                with open(os.path.join(download_id, os.path.basename(lnk)), "wb") as f:
                    f.write(requests.get(lnk).content)
            except:
                print("Error Occured")
                print("Pass This Link: " + lnk)


def main():
    entered_id = input('Please Enter Twitter ID: ')
    while entered_id != 'QUIT':
        try:
            ImageDownload(entered_id)
        except:
            print("Error Occured")
        entered_id = input('Please Enter Twitter ID: ')


if __name__ == '__main__':
    main()
