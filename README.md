# Anti-reCaptcha

**Anti-reCaptcha** is a Python module designed to automatically solve Google's reCAPTCHA V2 and V3 challenges. Powered by Selenium, it enables full browser automation and human-like interactions, making it ideal for bot developers, automation workflows, and penetration testing tools.

## Key Features

- 🔓 Automatic bypass for reCAPTCHA V2 checkbox and audio challenges
- 🧠 Intelligent handling of reCAPTCHA V3 score-based verification
- 🌐 Compatible with headless browsers and proxies
- 🧪 Built for Selenium, tested with Undetected ChromeDriver

Whether you're building automated scripts, scraping data, or testing CAPTCHA behavior, **Anti-reCaptcha** is your plug-and-play solution for dealing with Google’s CAPTCHA systems.

🔴 reCaptchaV3 bypass does not work on all sites. Test on your target to find out.

🐍 Support Python >= 3.7

# Installation

### Install from PyPI

```
pip install anti-recaptcha
```

### To Upgrade

```
pip install anti-recaptcha --upgrade
```

### Install from Github (latest repo code)

```
pip install git+https://github.com/dragon0041/Anti-reCaptcha@master
```

# Bypassing **reCaptchaV3**

To bypass reCAPTCHA V3, first extract the anchor URL:

- Open inspect-element on your browser.
- Go to the web page that has reCaptcha V3 (not V2 invisible).
- In Network tab you should see many requests.
- Type `anchor` in text-field filter to hide unnecessary requests.
- Now you should see a url like this:

  > ``https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfCVLAUAAAAFwwRnnCFW_J39&co=aHR....``
  >

  pass this url to `reCaptchaV3` class:

Note that the anchor urls also can have `/enterprise/anchor` instead of `/api2/anchor` in other sites.

```python
from anti_recaptcha import reCaptchaV3

reCaptcha_response = reCaptchaV3('ANCHOR URL')
## use this response in your request ...
```

### **Proxy**

```python
from anti_recaptcha import reCaptchaV3
from anti_recaptcha.structs import Proxy

## Using Proxy structure
proxy = Proxy(Proxy.type.HTTPs,'HOST','PORT')

## with authentication credentials
# proxy = Proxy(Proxy.type.HTTPs,'HOST','PORT','USERNAME', 'PASSWORD')

reCaptcha_response = reCaptchaV3('ANCHOR URL', proxy)
```

_also you can configure it as Dict._

```python

proxy = {"http": "http://HOST:PORT",
         "https": "https://HOST:PORT"}

reCaptcha_response = reCaptchaV3('ANCHOR URL', proxy)
```

### **Timeout**

Default timeout is `20 seconds` but you can change the amount like this:

```python
from anti_recaptcha import reCaptchaV3

reCaptcha_response = reCaptchaV3('ANCHOR URL', timeout = 10)
```

# Bypassing **reCaptchaV2**

Before start using reCaptchaV2 solver, you must install the following requirements.

### **Requirements** :
- **PocketSphinx** (used as speech-to-text engine)
- **ffmpeg** (used for audio format conversion)

After installing requirements, you should pass your webdriver to reCaptchaV2 class then anti-recaptcha tries to solve the reCaptcha V2 which is in current tab of browser.

```python
from anti_recaptcha import reCaptchaV2

# Create an instance of webdriver and open the page has recaptcha v2
# ...

# pass the driver to reCaptchaV2
is_checked = reCaptchaV2(driver_instance) # it returns bool

```

### **Arguments**
**driver**: An instance of webdriver.\
**Play**: Click on 'PLAY' button. [Default is True means it plays the audio].\
**Attempts**: Maximum solving attempts for a recaptcha. [Default is 3 times].

```python
is_checked = reCaptchaV2(
                    driver = driver_instance,
                    play = False,
                    attempts = 5
                  )

```

> Note that Google gonna blocks you if you try to solve many recaptcha via audio challenge. In this case anti-recaptcha raises `IpBlock` exception.

# Exception

| Exception | Bypass | Description |
| ---------- | -------------- | --------------- |
| ConnectionError | reCaptchaV3 | Raised due to network connectivity-related issues. |
| RecaptchaTokenNotFound | reCaptchaV3 | Raised when couldn't find token due to wrong `anchor_url`. |
| RecaptchaResponseNotFound | reCaptchaV3 | Raised when couldn't find reCaptcha response due to using **anti-recaptcha** for site that hasn't reCaptchaV3. |
| IpBlock | reCaptchaV2 | Raised due to solving many recaptcha via audio challenge. |

# Legal Disclaimer

This was made for educational purposes only, nobody which directly involved in this project is responsible for any damages caused.
**You are responsible for your actions.**

&nbsp;

# License

[MIT](https://choosealicense.com/licenses/mit/)
