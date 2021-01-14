import os
# from os import system as sys
from socket import socket

import idna
from flask import Flask, request, redirect, render_template
# from werkzeug.utils import secure_filename

from backend import vtscan, certcheck, httpscheck,checkReditect,checkTrustedCert
import config

app = Flask(__name__)
app.secret_key = "secret key";
app.config['MAX_CONTENT_LENGTH'] = 350 * 1024 * 1024;

vtscan_bool=False

if config.VTAPIKEY == "YOU_NEED_TO_ENTER_YOUR_API_KEY_HERE_FOR_VIRUSTOTAL_SCAN_TO_WORK":
    vtscan_bool=False
else:
    vtscan_bool=True

@app.route('/')
def hello_world():
    # sys("rm ./templates/result.html")

    return render_template('main.html')


@app.route('/', methods=['POST'])
def upload_file():
    global urlts
    urlts=""
    if request.method == 'POST':
        # check if the post request has the file part
        if 'urlts' not in request.values:
            # flash('No file part')
            return redirect(request.url)

        url = request.values['urlts']
        agent=""
        if "@shell" in str(url):
            agent="shell"
            url=str(url)[:-6]

        print(request.values['urlts'])
        return processurl(url,agent)


def processurl(urltsm,agent):

    urltsm=httpscheck.rmrf_protocol(urltsm)
    #ASSUME NOT SAFE AS DEFAULT
    ISWEBSITESAFE = True
    CERTSCORE = "DANGER"     # THIS WILL MAKE IT NOT SAFE BY DEFAULT
    ISHTTPS="NO"
    REDIRECTIONSCORE="NA"

    REASON = {
        'https': "The website uses HTTPS. It's needed to transmit data securely.",
        'certtrust': "The certificate for encryption is not provided by trusted Certification Authority. An attacker can forge a certificate and decrypt the data from HTTPS over SSL, making HTTPS insecure.",
        'malware': "This website is not reported for malicious scripts.",
        'redir': "Redirection is how a website navigates the user to HTTPS even if they try to visit from HTTP on its own.",
        'covred': "The website does not contain redirection code.",
        'overall': "",
        'webstat': "Website Available"
    }

    if vtscan_bool:
        RESULT=vtscan.getResult(config.VTAPIKEY,urltsm)

        MALWARESCORE = RESULT['positives']

        TRIGGERS=[]
        MALHITS=[]

        if MALWARESCORE > 0:
            REASON['overall']=REASON['overall']+" * MALWARE HIT"
            REASON['malware']= "This website is reported to contain malicious scripts or tools, or it is created with malicious intent. BE CAUTIOUS. An adversary can take advantage and steal your data."
            ISWEBSITESAFE= False

        if MALWARESCORE > 0:
            for i in RESULT['scans']:
                if RESULT['scans'][i]['detected'] == True:
                    TRIGGERS.append(i)
                    MALHITS.append(RESULT['scans'][i]['result'])
    else:
        TRIGGERS=[]
        MALHITS=[]
        TRIGGERS.append("--")
        MALHITS.append("--")
        REASON['malware']="VirusTotal API key not used, skipping malware scan."

###### =======================================

    hostname_idna = idna.encode(urltsm)
    sock = socket()

    ERROR404=False
    try:

        sock.connect((hostname_idna, 80))

        MARK =1
    except Exception:
        MARK=-1


    if MARK > 0:

        REDIRECTIONSCORE=checkReditect.scan(urltsm)



        HTTPSBOOL = httpscheck.scan(urltsm)
        HTTPSBOOL = HTTPSBOOL.split(';')
        ISHTTPS = HTTPSBOOL[0]
        if HTTPSBOOL[1] == 'SR':
            REDIRECTSCHEME = "SOFT REDIRECTION TO HTTPS"
        elif HTTPSBOOL[1] == 'HR':
            REDIRECTSCHEME = "HARD REDIRECTION TO HTTPS"
        else:
            REDIRECTSCHEME = "NO REDIRECT"

        ### CHECKING RESULTS
        # print("NO" in ISHTTPS)

        if "NO" in ISHTTPS:
            print("http hit")
            REASON['https']="The website do not use HTTPS. It's needed to transmit data securely."
            REASON['overall'] = REASON['overall'] + " * HTTP HIT"
            ISWEBSITESAFE = False



        if REDIRECTIONSCORE:
            print("red hit")
            REASON['overall'] = REASON['overall'] + " * COVERT REDIRECTION HIT"
            REASON['covred'] = "The website contains redirection code. It can redirect to some other page without " \
                               "user consent. "
            ISWEBSITESAFE= False

        if "YES" in ISHTTPS:
            print("cert check")
            CERT = certcheck.getMainScan(urltsm)
            CERT = CERT.split(';')
            # CHECK TRUSTED CERTS
            if checkTrustedCert.scan(CERT[4]) == True:
                REASON['certtrust'] = "The certificate for encryption is provided by trusted Certification Authority."
                CERTSCORE = "SAFE"

            #

        if "SAFE" not in CERTSCORE:
            print("cert hit")
            REASON['overall'] = REASON['overall'] + " * UNTRUSTED ENCRYPTION CERT"
            REASON['certtrust'] = "The certificate for encryption is not provided by trusted Certification Authority. An attacker can forge a certificate and decrypt the data from HTTPS over SSL, making HTTPS insecure."
            ISWEBSITESAFE = False

    else:
        ERROR404=True
        REASON['webstat']="Website appears to be unreachable."


    ### COMPILING THE DATA IN A STRUCTURE
    REDIRECTSCHEME="NA"
    if ISWEBSITESAFE == True:
        TRANRESULT="YES"
    else:
        TRANRESULT="NO"


    WEBUS=urltsm

    if vtscan_bool:
        if MALWARESCORE > 0:
            MALSR="UNSAFE"
            TRIGGERS=str(TRIGGERS)
            MALHITS=str(MALHITS)
        else:
            MALSR = "SAFE"
    else:
        MALSR="N/A"

    if "NO" not in ISHTTPS:
        HTTPSSCORE="YES"
        REDIR=REDIRECTSCHEME

        if CERT is not None:
            CERT0=CERT[0]
            CERT1 = CERT[1]
            CERT2 = CERT[2]
            CERT3 = str(CERT[3])
            CERT4 = CERT[4]
            CERT5 = CERT[5]
            CERT6 = CERT[6]
        else:
            CERT0 = "NA"
            CERT1 = "NA"
            CERT2 = "NA"
            CERT3 = "NA"
            CERT4 = "NA"
            CERT5 = "NA"
            CERT6 = "NA"

        if checkTrustedCert.scan(CERT[4]) == True:
            CERTTRUST="YES"
        else:
            CERTTRUST = "NO"

    else:
        HTTPSSCORE = "NO"
        REDIR = REDIRECTSCHEME
        CERT0 = "NA"
        CERT1 = "NA"
        CERT2 = "NA"
        CERT3 = "NA"
        CERT4 = "NA"
        CERT5 = "NA"
        CERT6 = "NA"
        CERTTRUST="NA"

    if REDIRECTIONSCORE == True:
        COVRED="YES"
    else:
        COVRED = "NO"
    
    if agent == "shell":
        return str(str(TRANRESULT)+";"+(WEBUS)+";"+(MALSR)+";"+str(TRIGGERS)+";"+str(MALHITS)+";"+HTTPSSCORE+";"+COVRED+";"+REDIR+";"+CERT0+";"+CERT1+";"+CERT2+";"+CERT3+";"+CERT4+";"+CERT5+";"+CERT6+";"+CERTTRUST+";"+str(ERROR404)+";"+str(REASON))

    return render_template('res.html',TRANRESULT=TRANRESULT,WEBUS=WEBUS,MALSR=MALSR,TRIGGERS=TRIGGERS,MALHITS=MALHITS,
                           HTTPSSCORE=HTTPSSCORE,COVRED=COVRED,REDIR=REDIR,CERT0=CERT0,CERT1 = CERT1,CERT2 = CERT2,CERT3 = CERT3,CERT4 = CERT4,CERT5 = CERT5,CERT6 = CERT6,CERTTRUST=CERTTRUST
                           ,ERROR404=ERROR404,REASON=REASON)


if __name__ == '__main__':
    # sys("rm ./templates/result.html")
    app.run()
