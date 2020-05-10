

def scan(certIssuer):
    trustedCA=[]
    with open("backend/calist.txt",'r') as calist:
        trustedCAD=calist.read();
        trustedCA=trustedCAD.split(';')

    certIssuer=certIssuer.split(' ')
    if certIssuer[0] in trustedCA:
        return True
    else:
        return False
