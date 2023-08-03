import requests

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_input="google.com"
with open("subdomainlist.txt","r") as subdomain_list:
    for word in subdomain_list:
        word=word.strip()
        url="https://" + word + "." + target_input
        response=make_request(url)
        if response:
            print("found subdomain---> " + url)

#"subdomainlist.txt" dosyasından alt alan adları listesini alır ve o isimde google nin alt bir sayfası var mı onu kontrol eder
#yani subdomain kontrolu