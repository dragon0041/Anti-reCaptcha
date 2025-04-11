from .exceptions import RecaptchaTokenNotFound, RecaptchaResponseNotFound
from .session import Session
from .structs import CustomSite
from .constants import POST_DATA
from .utils import extractor

import re
from typing import Union

class reCaptchaBypasser:
    """
    reCaptchaBypasser
    -----------------
    Bypass reCaptcha V3 only by sending requests.
    
    Attributes
    ----------
    site: str or CustomSite
        site from `pypasser.sites` or CustomSite object from `pypasser.structs`.

    """
    def __new__(cls, site: Union[str, CustomSite], timeout: int = 20) -> str:

        cls.session = Session(timeout)
        
        if type(site) == str:
            data = extractor(site)
        else:
            data = site.dict()
        
        # Gets recaptcha token.
        token = cls.get_recaptcha_token(data['endpoint'],
                                        data['params']
                                        )
        
        # Converts string params to Dict.
        params = dict(pair.split('=') for pair in data['params'].split('&'))
        
        
        # Gets recaptcha response.
        post_data = POST_DATA.format(params["v"], token,
                                     params["k"], params["co"])
        
        recaptcha_response = cls.get_recaptcha_response(data['endpoint'],
                                                        f'k={params["k"]}',
                                                        post_data
                                                        )
        
        return recaptcha_response
        
                
    def get_recaptcha_token(endpoint: str, params: str) -> str:
        """
        Sends GET request to `anchor URL` to get recaptcha token.
        
        """
        response = reCaptchaBypasser.session.send_request(
                                f"{endpoint}/anchor", params=params)
        
        results = re.findall(r'"recaptcha-token" value="(.*?)"', response.text)
        if not results:
            raise RecaptchaTokenNotFound()
        
        return results[0]
            

    def get_recaptcha_response(endpoint: str, params: str, data: str) -> str:
        """
        Sends POST request to `reload URL` to get recaptcha response.
        
        """
        response = reCaptchaBypasser.session.send_request(
                                f"{endpoint}/reload", data=data, params=params)
        
        results = re.findall(r'"rresp","(.*?)"', response.text)
        if not results:
            RecaptchaResponseNotFound()
        
        return results[0]