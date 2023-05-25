import sys
import argparse
import json
import requests
import time
import hashlib

from pathlib import Path
from types import SimpleNamespace

class TinyLink:
    def __init__(self, api: str, token: str, verbose: bool=False):
        self.api = api
        self.token = token
        self.verbose = verbose
    
    @property
    def verbose(self) -> bool:
        return self.__verbose
    
    @verbose.setter
    def verbose(self, value) -> bool:
        self.__verbose = value

    def short(self, url: str, check: bool=False, keyword: str=str(), format: str="json") -> str:
        timestamp=int(time.time())
        data = {
            "timestamp": f"{timestamp}",
            "signature": f"{self.create_key(timestamp)}",
            "action": "shorturl",
            "url": f"{url}",
            "format": f"{format}"
            }
        
        if(self.verbose):
            print(data)

        if(keyword):
            data.update({ "keyword": f"{keyword}" })
        
        if(check):
            self.check_url(url)
            
        echo = json.loads(requests.post(url = f"{self.api}", data = data, headers={'Accept': 'application/json'}).text, object_hook=lambda d: SimpleNamespace(**d))
    
        if(hasattr(echo, 'shorturl')):
            return echo.shorturl
        else:
            return str()

    def expand(self, url: str, check: bool=False, format: str="json") -> str:
        timestamp=int(time.time())
        data = {
            "timestamp": f"{timestamp}",
            "signature": f"{self.create_key(timestamp)}",
            "action": "expand",
            "shorturl": f"{url}",
            "format": f"{format}"
            }

        if(self.verbose):
            print(data)

        if(check):
            self.check_url(url)

        echo = json.loads(requests.post(url = f"{self.api}", data = data, headers={'Accept': 'application/json'}).text, object_hook=lambda d: SimpleNamespace(**d))
    
        if(hasattr(echo, 'longurl')):
            return echo.longurl
        else:
            return str()

    def check_url(self, url: str, status: int=[ 200, 301, 302, 303 ]) -> bool:
        try:
            if(not (requests.get(url = url).status_code in status)):
                raise ConnectionRefusedError(url)
        except:
            raise ConnectionError(url)

    def create_key(self, timestamp: int) -> str:
        return hashlib.md5((f"{self.token}{timestamp}").encode('utf-8')).hexdigest()


def tinylink_main(argv):
    filename = Path(__file__).name

    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("-a", "--api", required=True, help="Link to YOURLS API")
    argumentParser.add_argument("-k", "--key", required=True, help="Secret YOURLS signature token")
    argumentParser.add_argument("-u", "--url", required=True, help="URL to be shorten/expanded")
    argumentParser.add_argument("-n", "--name", help="Prefix for URL that should be shorten")
    argumentParser.add_argument("-c", "--check", action="store_true", help="Check if URL is accessible (Status 200)")
    argumentParser.add_argument("-e", "--expand", action="store_true", help="Expand a shorten URL")
    argumentParser.add_argument("-s", "--short", action="store_true", help="Short a given URL")
    argumentParser.add_argument("-v", "--verbose", action="store_true", help="Show whats going on")

    args = argumentParser.parse_args()

    if(args.verbose):
        print(filename, "args=%s" % args)

    tinylink = TinyLink(args.api, args.key)
    name = str()

    check: bool = args.check
    name: bool = args.name

    try:
        if(args.expand):
            print(tinylink.expand(args.url, check=check))
        elif(args.short):
            print(tinylink.short(args.url, check=check, keyword=name))
    except ConnectionRefusedError as ex:
        print(f"{ConnectionRefusedError.__name__}->{ex.strerror}")
    except ConnectionError as ex:
        print(f"{ConnectionRefusedError.__name__}->{ex.strerror}")
    except Exception as ex:
        print(f"{Exception.__name__}->{ex.args}")


if __name__ == "__main__":
   tinylink_main(sys.argv[1:])