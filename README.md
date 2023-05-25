[![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1%20Beta-orange.svg)](https://github.com/0x007e) [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
# Small YOURLS Python API

This python script can be used with command line or as import from another script.

## Parameter

For additional information call:

``` bash
python ./tinylink.py -h
```

| Short | Expand    | Description        |
|-------|-----------|--------------------|
| -h    | --help    | Help menu          |
| -v    | --verbose | Enable verbosity   |
| -c    | --check   | Check given URL    |
| -a    | --api     | YOURLS API URL     |
| -k    | --key     | YOURLS API key     |
| -u    | --url     | Short/expand URL   |
|-------|-----------|--------------------|
| -s    | --short   | Short given URL    |
| -n    | --name    | Name for short URL |
|-------|-----------|--------------------|
| -e    | --expand  | Expand given URL   |

## CLI-Usage

### Short a link:
``` bash
# Short link without url check
python ./tinylink.py -a https://YOUR-API-URL/yourls-api.php -k API-KEY -u https://github.com/0x007e -s

# Short link with url check -c
python ./tinylink.py -a https://YOUR-API-URL/yourls-api.php -k API-KEY -u https://github.com/0x007e -s -c

# Short link with specific name -n
python ./tinylink.py -a https://YOUR-API-URL/yourls-api.php -k API-KEY -u https://github.com/0x007e -s -n linkname

# Return value is shorten URL or error message
```

### Expand a link:
``` bash
# Expand a link without url check
python ./tinylink.py -a https://YOUR-API-URL/yourls-api.php -k API-KEY -u https://YOUR-API-UR/3jd7ed -e

# Expand link with url check -c
python ./tinylink.py -a https://YOUR-API-URL/yourls-api.php -k API-KEY -u https://YOUR-API-UR/3jd7ed -e -c

# Return value is expanded URL or error message
```

## Python usage

``` python
API: str = "https://YOUR-API-UR/"
KEY: str = "YOURKEY"

# ------------------------------------------------------------------------------

# Short link without url check
print(tinylink.short("https://github.com/0x007e"))

# Short link with url check
print(tinylink.short("https://github.com/0x007e", check=True))

# Short link with url check and specific name
print(tinylink.short("https://github.com/0x007e", check=True, keyword="MYLINK"))

# ------------------------------------------------------------------------------

# Expand link without url check
print(tinylink.expand("https://YOUR-API-UR/3jd7ed"))

# Expand link with url check
print(tinylink.expand("https://YOUR-API-UR/3jd7ed", check=True))

# ------------------------------------------------------------------------------
```
