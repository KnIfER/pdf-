#coding=utf-8
#based on ReportLab-master\tests\test_multibyte_chs.py
"""
The code in this module will disappear any day now and be replaced
by classes in reportlab.pdfbase.cidfonts
"""
import math
from reportlab.lib.testutils import setOutDir,makeSuiteForClasses, outputfile, printLocation

import string, os
import codecs
import unittest
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors
from reportlab.lib.codecharts import KutenRowCodeChart, hBoxText

global VERBOSE
VERBOSE = 0


from reportlab.lib import colors
#colors.lavenderblush lawngreen lemonchiffon lightblue lightcoral

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
            return True
    else:
            return False

class CHSFontTests(unittest.TestCase):
    def test0(self):
        "A basic document drawing some strings"
        wordCapacity = 36
        fontSize = 24
        
        import codecs
        f = codecs.open(r"/storage/emulated/0/org.qpython.qpy/scripts/favorites.txt","r","utf-8")
        flst = f.readlines()
        for idx,i in enumerate(flst):
            flst[idx] = i.replace("\n","")
        fCout = 0
        fEnd = len(flst)
        npage = math.ceil(1.0*len(flst)/wordCapacity)
        npage = int(npage)
        
        from reportlab.pdfbase.cidfonts import UnicodeCIDFont, findCMapFile
        pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
        
        #Canvas(self,filename,
        #        pagesize=(595.27,841.89),
        #        bottomup = 1,
        #        pageCompression=0,
        #        encoding=rl_config.defaultEncoding,
        #        verbosity=0
        #        encrypt=None):
        c = Canvas(r"/storage/emulated/0/org.qpython.qpy/scripts/rp2.pdf")
        #draw pages
        #stuffs:    "gb2312" "utf8" 'STSong-Light' 'Helvetica'
        for i in range(npage): 
            for (dudinx,duco) in enumerate(flst[fCout:min(fCout+wordCapacity,fEnd)]):
                has_jiaguwen = 0
                #determine which font to use
                for uchar in flst[fCout+dudinx].replace("\r",""):
                    #print uchar
                    if is_chinese(uchar):
                        has_jiaguwen = 1
                if has_jiaguwen:
                    c.setFont('STSong-Light', fontSize)
                    c.drawString(
                            175,
                            780-22*dudinx,
                            flst[fCout+dudinx].replace("\r","").encode("utf8")
                            )
                else:
                    c.setFont('Helvetica', fontSize)
                    c.drawString(
                            175,
                            780-22*dudinx,
                            flst[fCout+dudinx].replace("\r","").encode("utf8")
                            )                
            fCout+=wordCapacity
            #c.setFont('Helvetica',10)
           
            c.setFillGray(0.1)
            c.setFillColor(colors.Color( 100, 0, 0, alpha=1))
            #c.drawCentredString drawRightString     other pos:(550,36)
            c.drawRightString(115, 760, 'Page %d' % c.getPageNumber())
            #drop a page,start a new one
            c.showPage()
        c.save()


def makeSuite():
    return makeSuiteForClasses(CHSFontTests)


#noruntests
if __name__ == "__main__":
    VERBOSE = 1
    unittest.TextTestRunner().run(makeSuite())

