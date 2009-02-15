import tarfile
import xml.dom.minidom
from pygame import Color
import pygame

def formatear(string):
    s=''
    n=0
    for st in string:
        s+=st
        if st==' ':
            n=0
            continue
        n+=1
        n%=20
        if n==0:
            s+=' '
    return s

flags=('warning','bien','idea','requiere trabajo','aclarar','pregunta','basura','reunion','problema')

colores=(
    ( Color('#FFFCD5'), Color('#646D00') ) ,
    ( Color('#ABFBC7'), Color('#035900') ) ,
    ( Color('#FDE1E1'), Color('#930002') ) ,
    ( Color('#FFE8CE'), Color('#563900') ) ,
    ( Color('#D2F1FF'), Color('#03BFEE') ) ,
    ( Color('#EDDFFF'), Color('#000000') ) ,
    ( Color('#FFFFFF'), Color('#000000') ) ,
    ( Color('#000000'), Color('#ECFF19') )
    )

omitir=('picurl', 'outlinecolor', 'textcolor', 'piccaption', 'defaultfont', 'comment', 'fillcolor')

def isElementNode(node):
    return node.nodeType == xml.dom.minidom.Node.ELEMENT_NODE

links=[]
pos_x={}
pos_y={}
#rects={}
item_by_id={}

class Item():

    def __init__(self,node):
        self.node=node
        #elements = filter(isElementNode,node.childNodes)
        self.child=[]
        self.flag=[]
            
        for  elem in node.childNodes:
            if  elem.nodeType != xml.dom.minidom.Node.ELEMENT_NODE or elem.tagName in omitir:
                continue 
                
            data=elem.firstChild.data if elem.firstChild else ""
                
            if elem.tagName in ('child','flag'):
                getattr( self , elem.tagName ).append( int(data) )
                if elem.tagName == 'child':
                    links.append( (int(self.id),int(data)) )
            else:
                setattr(self,elem.tagName, data)

        self.id=int(self.id)
        self.parent=int(self.parent)
        self.colorscheme=int(self.colorscheme)
        self.xpos=int(float(self.xpos))
        self.ypos=int(float(self.ypos))
 
        pos_x[self.id]=self.xpos
        pos_y[self.id]=self.ypos
        item_by_id[self.id]=self
        
    def __str__(self):
        return '###############'+str(self.__dict__)
    def __repr__(self):
        return '###############'+str(self.__dict__)


class Kdi:
    def __init__(self,filename):
        xmlfile='maindoc.xml'
        tmp='/tmp/py-mind/'
        tmpxml=tmp+'/'+xmlfile
    
        ftar = tarfile.open(filename)
        ftar.extract(xmlfile,tmp)

        f = file(tmpxml,'r')
        txt=f.read().replace('utf8','utf-8',1)
        f.close()
        f = file(tmpxml,'w')
        f.write( txt )
        f.close()
        main=xml.dom.minidom.parse(tmpxml)
        
        kdissertdoc=main.firstChild

        #elements = filter(isElementNode,kdissertdoc.childNodes)
        #items = filter(lambda elem: elem.tagName=='item',elements)
        #items  = [elem for elem in elements if elem.tagName=='item']
        
        #items = [child for child in kdissertdoc.childNodes if  \
# child.nodeType == xml.dom.minidom.Node.ELEMENT_NODE and child.tagName=='item']

       #self.items=map(Item,items)

        self.items = [Item(child) for child in kdissertdoc.childNodes if  \
 child.nodeType == xml.dom.minidom.Node.ELEMENT_NODE and child.tagName=='item']
        
        self.links=links
        self.pos_x=pos_x
        self.pos_y=pos_y
        #self.rects=rects
        self.item_by_id=item_by_id


        self.flags=flags
        self.colores=colores
