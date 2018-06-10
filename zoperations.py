import zipfile

def extract(zfile,password):    #zfile: eg. "test2.py", password: eg. "123abc"
    try:
        zfile = zipfile.ZipFile(zfile)
        zfile.extractall(pwd=password.encode('cp850', 'replace'))
        return True
    except Exception as e:
        print(e)

def extractable(zfile, password):    #zfile: eg. "test2.py", password: eg. "123abc"
    try:
        zf = zipfile.ZipFile(zfile)
        files = zf.infolist()
        zf.read(files[0],pwd=password.encode('cp850', 'replace'))
        zf.close()
        return True
    except:
        return False
