> टिप्पणी #१ : यह संपर्क प्रोटोटाइप (v४.०) है जो की [साकेत उपाध्याय](https://github.com/Saket-Upadhyay) एवं  [ऊर्जा रुंगटा](https://github.com/OorjaRungta) द्वारा  HackCoVIT'20 में प्रस्तुत करने के लिए बनाया गया था, जहां इसे प्रथम पुरुस्कार से सम्मानित किया गया। 

> वर्तमान में "Google Developer Student Club (DSC) VIT Bhopal" (दिनांक- ११ जनवरी २०२१) के  "Web Development and Security" विभाग के मासिक परियोजना कार्य के अंतर्गत इसमें सुधार एवं परिवर्तन किए जा रहें हैं । 

> **[DSCVITBHOPAL/Sampark-Web-Extension](https://github.com/DSCVITBHOPAL/Sampark-Web-Extension) पर इसके आगे के विकास पर नज़र रखी जा सकती है।**

> अगर DSC के सामुदायिक दिशानिर्देशों से अनुमति मिलती है तो हम इसे यहां भी अपडेट करेंगे।  

---

# संपर्क 
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg?style=for-the-badge&logo=heroku)](https://samparkscan.herokuapp.com/)  [![Version](https://img.shields.io/badge/Version-4.0-green?style=for-the-badge)](#) [![License-MIT-blue](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](https://github.com/Saket-Upadhyay/SAMPARK/blob/master/LICENSE) [![made-with-python](https://img.shields.io/badge/Python-3-green?style=for-the-badge&logo=python)](https://www.python.org/)
### प्रोटटाइप ४.०
##### आवश्यक लाइब्रेरी इंस्टॉल करें
```bash
python3 -m pip install -r requirements.txt
```
##### अप्पलीकेशन को रन करें 
```bash
python3 app.py
```

* टिप्पणी #२ : अगर आपका VirusTotal मापांक क्रैश होता है तो कृपया अपनी VirusTotal API KEY की जांच करें, जो की config.py में उपस्थितः है। 
* विकास योजना [TODO](https://github.com/Saket-Upadhyay/SAMPARK/blob/master/TODO.md) में है। 
* VirusTotal API को सार्वजनिक संस्करण से हटा दिया गया है। हेरोकू ऐप को निजी संस्करण द्वारा होस्ट किया जाता है।

# प्रस्तावित आर्किटेक्चर डिजाइन

![](https://raw.githubusercontent.com/Saket-Upadhyay/SAMPARK/master/DOCS/FLOW/SAMPARK%20FRAMEWORK.png "Overall Idea")
![](https://raw.githubusercontent.com/Saket-Upadhyay/SAMPARK/master/DOCS/FLOW/SAMPARK%20ARCHITECTURE.png "Initial Prototype")

# स्क्रीनशॉटस 
![](https://raw.githubusercontent.com/Saket-Upadhyay/SAMPARK/master/DOCS/Screenshots/Screenshot1.png)
![](https://raw.githubusercontent.com/Saket-Upadhyay/SAMPARK/master/DOCS/Screenshots/Screenshot2.png)
![](https://raw.githubusercontent.com/Saket-Upadhyay/SAMPARK/master/DOCS/Screenshots/Screenshot3.png)

##### HackCoVIT 2020 का समस्या प्रश्न -
हाल ही में, अंत-ग्राहकों को लक्षित करने वाले ऑनलाइन संचालन वेब-आधारित सेवाओं पर अधिक भरोसा कर रहे हैं। कई फर्जी ई-कॉमर्स वेबसाइट उन उत्पादों को बेचने का दावा कर सकती हैं जो वर्तमान में कहीं और उपलब्ध नहीं हैं। अनजान ग्राहकों की बढ़ती मात्रा को देखते हुए, हम साइबर अपराधी के नजरिए से अधिक सुरक्षा संकट और आसान अवसर देख सकते हैं। उदाहरण के लिए: अगर लोग दैनिक आवश्यकताओं को खरीदने के लिए बाहर नहीं जा सकते हैं वे ऐसे  ई-कॉमर्स वेबसाइटों पर भरोसा करते हैं जो उन्हें अज्ञात / कम भरोसेमंद स्रोतों का उपयोग करने के लिए मजबूर कर सकते हैं जो उनकी निजी जानकारी की मांग करते हैं  एवं उनको अपनी संवेदनशील जानकारी देने के लिए मजबूर कर सकते हैं। इससे अपराधियों को आपके क्रेडिट कार्ड की आवश्यकता के बिना, अनधिकृत लेनदेन करने के लिए आपके क्रेडिट कार्ड नंबर, पिन और सुरक्षा कोड को चुराने में मदद मिलेगी।

ऐसा सॉफ़्टवेयर बनाएं जो इन क्रेडिट कार्ड धोखाधड़ी को रोकने में मदद करता है और उपयोगकर्ता को ऑनलाइन लेनदेन करने से पहले चेतावनी देता है।
