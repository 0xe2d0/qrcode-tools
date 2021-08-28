__author__ = "eyyub1337"

import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
from sys import argv

def main():
    helpMsg = "QRCode Reader & Generator\nUsage : \n\nGenerate\n\n\t"\
            "python3 main.py g <message> <output-filename>"\
            "\n\nRead\n\n\tpython3 main.py r <qrcode-file-path>"
    
    if len(argv)>=2:
        
        if argv[1].lower() == "g":
            # Generate Mode
            msg = argv[2].strip()
            output = argv[3].strip()
            generateQR(msg,output)
        
        elif argv[1].lower() == "r":
            # Read Mode
            path = argv[2].strip()
            readFile(path)
            
        
        else:
            print(helpMsg)
            exit()

    else:
        print(helpMsg)
        exit()


def readFile(path):
    data = decode(Image.open(path))[0].data.decode("ascii")
    print(f"QRCode Content :\n{data}")
    exit()

def generateQR(msg,filename):
    qr = qrcode.make(str(msg))
    qr.save(filename)
    print("Saved "+filename)
    exit()

main()
