import math
wordCapacity = 36

f = open("favorites.txt")
plenis = open("resule.pdf","w")
flst = f.readlines()
for idx,i in enumerate(flst):
    flst[idx] = i.replace("\n","")
fCout = 0
fEnd = len(flst)
npage = math.ceil(1.0*len(flst)/wordCapacity)
npage = int(npage)

def pdx2odx(i):
    return i*2+5
    
def initialize_pages():
    header = (
    "%PDF-1.4\n"+
    "1 0 obj <</Type /Catalog /Pages 2 0 R>>\n"+
    "endobj\n"+
    "2 0 obj <</Type /Pages /Kids [3 0 R 7 0 R]/Count 2>>\n"+
    "endobj\n"+
    "3 0 obj<</Font <</F1 4 0 R>>>>\n"+
    "endobj\n"+
    "4 0 obj<</Type /Font /Subtype /Type1 /BaseFont /Helvetica>>\n"+
    "endobj\n"
    )
    plenis.write(header[:86]+ 
                ' 0 R '.join(str(pdx2odx(i)) for i in range(npage))+' 0 R'+
                header[97:97+8]+str(npage)+
                header[97+9:]
                )

def write_page(i):
    page = (
    str(pdx2odx(i))+" 0 obj<</Type /Page /Parent 2 0 R /Resources 3 0 R /MediaBox [0 0 500 800] /Contents "+str(pdx2odx(i)+1)+" 0 R>>\n"+
    "endobj\n"+
    str(pdx2odx(i)+1)+" 0 obj\n"+
    "<</Length 44>>\n"+
    "stream\n"+
    "".join("BT /F1 24 Tf 175 %d Td (%s)Tj ET\n"%(780-22*dudinx,duco) for (dudinx,duco) in enumerate(flst[fCout:min(fCout+wordCapacity,fEnd)]))+
    "endstream\n"+
    "endobj\n"
    )
    plenis.write(page)

def endcaping():
    cap = (
    "trailer <</Root 1 0 R>>\n"+
    "%%EOF"
    )
    plenis.write(cap)

    
initialize_pages()
for i in range(npage):
    write_page(i)
    fCout+=wordCapacity
endcaping()