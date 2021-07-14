import os, sys
from PIL import Image

class converter:
    def __init__(self):
        super().__init__()
        pass
    
    def clearDir(self, dir=""):
        if os.path.isdir(dir):
            try:
                os.remove(dir)
                print(f"{dir} Cleared!")
            except OSError:
                print(f"Failed to clear dir{dir}")

    def convertUI(self,src="",dest=""):
        res = False
        for file in os.listdir(src):
            if file.endswith('.ui'): 
                infile  = os.path.join(src,file)
                outfile = os.path.join(dest,"Ui"+file.split('.')[0]+".py")
                if infile != outfile:
                    try:
                        cmd = "pyside2-uic " + infile +" -o " + outfile 
                        self.clearDir(outfile)#if it exists already
                        res = os.system(cmd)==0 
                    except OSError:
                        print("cannot convert", infile)
                        sys.exit()
        return res

#sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)] 
    def convertImage(self,src="",dest="",format="ico",size=[(128,128)]): 
        res = False
        for file in os.listdir(src):
            f, e = os.path.splitext(file)
            infile  = os.path.join(src,file)
            outfile = os.path.join(dest,f +"."+format) 

            if infile != outfile:
                try:
                    with Image.open(infile) as im:
                        self.clearDir(outfile)
                        res = im.save(outfile,format = format.upper(), sizes=size) 
                except OSError:
                    print("cannot convert", infile)
                    sys.exit()
        return res

    def makeThumbnails(self,src="",dest="",format="jpeg",size=(256, 256)): 
        res = False
        for file in os.listdir(src):
            infile  = os.path.join(src,file)
            outfile = dest+"\\"+os.path.splitext(file)[0] +".thumb"
        
            if infile != outfile:
                try:
                    with Image.open(infile) as im:
                        im.thumbnail(size)
                        self.clearDir(outfile+format)
                        res = im.save(outfile,format = format.upper(), sizes=size)
                except OSError:
                    print("cannot create thumbnail for", infile)
                    sys.exit()
        return res

 
# run and make conversions
logoIn   = "C:\\Users\\Admin\\Pictures\\logos"
imageIn  = "C:\\Users\\Admin\\Pictures\\Pictures"
inpfile  = "C:\\Users\\Admin\\Pictures\\UI_designs\\Sefa_HIMS_v4"

logoOut  = "C:\\Users\\Admin\\Work-Space\\pyInstaller-Projects\\SEFA\\Sefa_v4\\Include\\icons"
imageOut = "C:\\Users\\Admin\\Work-Space\\pyInstaller-Projects\\SEFA\\Sefa_v4\\Include\\images"
outpfile = "C:\\Users\\Admin\\Work-Space\\pyInstaller-Projects\\SEFA\\Sefa_v4\\Include\\interface"
 
lib = converter()
if lib.convertUI(inpfile,outpfile): # convert's .ui to .py
    lib.convertImage(logoIn,logoOut) # creates icons
    lib.makeThumbnails(imageIn,imageOut) # creates thumbnails

