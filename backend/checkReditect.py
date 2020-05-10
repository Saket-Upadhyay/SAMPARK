import requests

def scan(urlts):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


    urlts="http://"+urlts

    r = requests.get(urlts, headers=headers, timeout=5, allow_redirects=True)  # first we try http

    data=r.text

    if "http-equiv=\"refresh\"" in data:
        return True
    else:
        return False


if __name__ == '__main__':
    print(scan("http://x64mayhem.github.io"))