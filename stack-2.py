# Using BeautifulSoup to extract items from a dictionary
text = """
<script type="text/javascript">
    window.untisUIVersion = 2;
    window.untisMomentLocale= "de";
    window.untis__webpack_public_path__ = "https://content.webuntis.com/WebUntis/static/2022.14.2/js/untis/";
    untis = {
        config: {
            "mode":"STANDARD",
            "locale":"de-at","contextPath":"/WebUntis",
            "licence":{
                "name":"HTBLA Weiz",
                "name2":"A-8160, 
                Dr.Karl-Widdmannstr. 40"
                },
                "mandantName":"htbla-weiz",
                "mandant":16270,
                "customerNumber":70284,
                "imageServiceConfig":{
                    "customLogo":true
                    },
                "loginServiceConfig":{
                    "ssoType":"none",
                    "samlProviderLabel":"",
                    "idpName":"",
                    "loginError":
                    "Invalid user name and/or password",
                    "lastUserName":"",
                    "lastMandantName":"htbla-weiz"
                    },
                },
            };
</script>
"""

import json
import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, "html.parser")
results = soup.find('script')
# print(results.prettify())
stringtext = results.get_text()

# print(stringtext)

array = stringtext.split(';')
untis = array[3].strip()
untis = re.sub("\s\s+"," ", untis)
# print(untis[18:-6])
# print(untis[40:-34])
structjson = json.loads(untis[18:-6]+"}")

print(structjson["loginServiceConfig"]["loginError"])
