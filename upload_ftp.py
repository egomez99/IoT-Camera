#!/usr/bin/python
# -*- coding: utf-8 -*-
#https://pythonspot.com/ftp-client-in-python/
from ftplib import FTP, error_perm
import ftplib
import os
import base64
import sys
import subprocess

#Definitions
from datetime import date
def now():
    return str(date.today())

def processRunning(name):
    for i in range(10):
        print "*",
    print "Process: " + name


def upload_handle(block):
    global sizeWritten
    fh.read(block)
    os.system('CLS')
    percentComplete = sizeWritten / totalSize
    percentComplete = round((percentComplete*100),1)

    print (percentComplete, "% complete")

def uploadFile(ftp, file):
    try:
        fh = open(file, 'rb')
        print "FTP File Opened"
        ftp.storbinary('STOR %s' % file, fh)#upload_handle
        print "FTP Upload Complete"
        fh.close()
    except Exception as e:
        print ("FTP Upload Error: ", repr(e))
#From Arduino sketch this prevents ftp upload our image.png
#ftplib.error_perm: 550 /root/test.png: No such file or directory

def uploadThis(path):
    files = os.listdir(path)
    os.chdir(path)
    for f in files:
        if os.path.isfile(path + r'\{}'.format(f)):
            fh = open(f, 'rb')
            ftp.storbinary('STOR %s' % f, fh)
            fh.close()
        elif os.path.isdir(path + r'\{}'.format(f)):
            ftp.mkd(f)
            ftp.cwd(f)
            uploadThis(path + r'\{}'.format(f))
    ftp.cwd('..')
    os.chdir('..')

def abspath(*paths):
    filename = os.path.join(*(paths or ('',)))
    if not os.path.isabs(filename):
        filename = os.path.join('/', filename)
    return filename

def subirArchivo(ftp, source, filename):
    fullname = abspath(filename)
    for row in filename:
        subprocess.call(row, shell=True)
    f = open(source, 'rb')
    if True:
        sys.stdout.write('<storing>')
    try:
        ftp.storbinary('STOR '+fullname, f, 8*1024)
    except error_perm, msg:
        if verbose:
            sys.stdout.write('FAILED: %s\n' % (msg))
            sys.stdout.flush()
        else:
            sys.stderr.write('FAILED to upload %r: %s\n' % (filename, msg))
            sys.stderr.flush()
    f.close()


# Encode image
with open(str(sys.argv[1]), "rb") as image_file:
    #encoded_file = base64.b64encode(inf.read())
    #contents_file = image_file.read()
    fileName = sys.argv[1]
    print os.path.basename(sys.argv[1])

#FTP routines
ftp = ftplib.FTP('ftp.SERVER.com')
ftp.set_debuglevel(1)#we want more details
ftp.login('UserName','PassWord')

#data = []
#ftp.cwd('/PathToFolder/')
#ftp.dir(data.append)

#uploadThis(r'/arduino/') # file to
#subirArchivo(ftp, source, encoded_file )
uploadFile(ftp, fileName) # file to send
ftp.quit()

#processRunning("Showing up FTP folder:")
#for line in data:
#    print "-", line
