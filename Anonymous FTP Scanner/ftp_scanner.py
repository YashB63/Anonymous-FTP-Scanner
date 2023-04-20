import ftplib

def anonymousLogin(hostName):
    try:
        ftp = ftplib.FTP(hostName)
        ftp.login('anonymous')
        print('\n [+] ' + str(hostName) + ' FTP Anonymous Login Succeded. ')
        ftp.quit()
        return True
    except Exception:
        print('\n [-] ' + str(hostName) + ' FTP Anonymous Login Fails. ')
        return False
    

if __name__ == "__main__":
    anonymousLogin('172.25.90.10')