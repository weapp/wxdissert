import tarfile
import xml.dom.minidom
from pygame import Color
import pygame
from library import textrect

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
"""
                del self.picurl
                del self.outlinecolor
                del self.textcolor
                del self.piccaption
                del self.defaultfont
                del self.comment
                del self.fillcolor
"""

veloc=10

class KdiParser:
    def __init__(self,filename):
        xmlfile='maindoc.xml'
        tmp='/tmp/py-mind/'
        tmpxml=tmp+'/'+xmlfile
        def isElementNode(node):
            return node.nodeType == xml.dom.minidom.Node.ELEMENT_NODE

        links=[]
        pos_x={}
        pos_y={}
        rects={}
        item_by_id={}

        class Item(dict):

            def __init__(self,node):
                self.node=node
                elements = filter(isElementNode,node.childNodes)
                self.child=[]
                self.flag=[]
                    
                for elem in elements:
                    data=elem.firstChild.data if elem.firstChild else ""
                    if elem.tagName in omitir:
                        continue 
                        
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
            
                #def __str__(self):
                #    return str([self.id,self.xpos])
                
            def __str__(self):
                return '###############'+str(self.__dict__)
            def __repr__(self):
                return '###############'+str(self.__dict__)


        ftar = tarfile.open(filename)
        ftar.extract(xmlfile,tmp)

        f = file(tmpxml,'r')
        txt=f.read().replace('utf8','utf-8')
        f.close()
        f = file(tmpxml,'w')
        f.write( txt )
        f.close()
    
        main=xml.dom.minidom.parse(tmpxml)

        kdissertdoc=main.firstChild

        elements = filter(isElementNode,kdissertdoc.childNodes)

        items = filter(lambda elem: elem.tagName=='item',elements)

        self.items=map(Item,items)


        self.links=links
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.rects=rects
        self.item_by_id=item_by_id


        print items[0:10]
        
class Kdi:
    def __init__(self,filename,back_surface):
        self.data=KdiParser(filename)
        self.items=self.data.items
        self.links=self.data.links
        self.pos_x=self.data.pos_x
        self.pos_y=self.data.pos_y
        self.rects=self.data.rects
        self.item_by_id=self.data.item_by_id
        self.actual_selected=None
        self.back_surface=back_surface
                            
        self.flags=flags
        self.colores=colores

        imagen='images/icons.png'
        icons=pygame.image.load(imagen).convert_alpha()
        w=icons.get_width()
        self.icons=[icons.subsurface( (0,i*w,w,w) ) for i in range(9)]
                            
    def render(self):
        global max_x,max_y,min_x,min_y,factor
        max_x=max( map(lambda x:x.xpos,self.data.items) )+100
        min_x=min( map(lambda x:x.xpos,self.data.items) )-100
        max_y=max( map(lambda x:x.ypos,self.data.items) )+100
        min_y=min( map(lambda x:x.ypos,self.data.items) )-100

        print "max x:", max_x
        print "min x:", min_x
        print "max y:", max_y
        print "min y:", min_y

        width=max_x-min_x
        height=max_y-min_y        

        factor=1

        pygame.font.init()

        filename=pygame.font.match_font('Sans Serif')
        font=pygame.font.Font(filename, 18)
        antialias=True

        surface=pygame.Surface((width/factor,height/factor))

        surface.fill(Color('#fffde8'))

        self.surface=surface
        
        self.draw_links()
        self.draw_tags()
        
        self.rect=self.surface.get_rect()
        self.kdi_selected=pygame.Surface(self.rect.size,pygame.SRCALPHA)        
        return self.surface
        
    def draw_links(self):
        for ini,des in self.data.links:
            startpos = (self.data.pos_x[ini]-min_x , self.data.pos_y[ini]-min_y)
            endpos = (self.data.pos_x[des]-min_x , self.data.pos_y[des]-min_y)
            startpos = map (lambda x: x/factor,startpos)
            endpos = map (lambda x: x/factor,endpos)
            pygame.draw.aaline(self.surface, (0,0,0), startpos, endpos)
            pygame.draw.aaline(self.surface, (0,0,0), [startpos[0]+1,startpos[1]+1], endpos)
            pygame.draw.aaline(self.surface, (0,0,0), [startpos[0]+1,startpos[1]-1], endpos)
            pygame.draw.aaline(self.surface, (0,0,0), [startpos[0]-1,startpos[1]+1], endpos)
            pygame.draw.aaline(self.surface, (0,0,0), [startpos[0]-1,startpos[1]-1], endpos)
    
    def update(self):
        rect_back=self.back_surface.get_rect()
        keys = pygame.key.get_pressed()
        if keys [pygame.K_LEFT]:    self.rect.move_ip (+veloc, 0)
        elif keys [pygame.K_RIGHT]: self.rect.move_ip (-veloc, 0)
        elif keys [pygame.K_UP]:    self.rect.move_ip (0, +veloc)
        elif keys [pygame.K_DOWN]:  self.rect.move_ip (0, -veloc)
        
        if self.rect.x>0: self.rect.x=0
        if self.rect.bottom<rect_back.bottom: rect.bottom=rect_back.bottom
        if self.rect.y>0: self.rect.y=0
        #if self.rect.right<rect2.right-righ_margin: rect.right=rect2.right-righ_margin
        if self.rect.right<rect_back.right: self.rect.right=rect_back.right

    
    def new_event(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN:
            kdi_selected = pygame.Surface(self.rect.size,pygame.SRCALPHA)
            last_selected=self.actual_selected
            self.actual_selected=None
            
            for id,r in self.data.rects.items():
                if r.collidepoint(event.pos[0]-self.rect.x , event.pos[1]-self.rect.y ):
                    self.actual_selected=id
                    break;
            
            if self.actual_selected==last_selected:
               self.actual_selected=None 
            
            if self.actual_selected:
                r=self.data.rects[self.actual_selected]
                it=self.data.item_by_id[self.actual_selected]
                txt= "%d:%s<<%s>>,%s"%(self.actual_selected,it.summary,it.text,map(lambda x:flags[x],it.flag))
                print txt 
                
                pygame.draw.rect(kdi_selected, Color('#0000FFFF'), r, 1)
                
                rect_in_point=pygame.Rect(0,0,4,4)
                for point in ['topleft', 'bottomleft', 'topright', 'bottomright','midtop', 'midleft', 'midbottom', 'midright']:
                    rect_in_point.center=point=getattr(r,point)
                    pygame.draw.rect(kdi_selected, Color('#0000FFFF'), rect_in_point)
            self.kdi_selected=kdi_selected      

    def draw_tags(self):
        pygame.font.init()

        filename=pygame.font.match_font('Sans Serif')
        font=pygame.font.Font(filename, 18)
        antialias=True
        for item in self.data.items:
            if item.parent== -1:
                color=colores[0]
            else:    
                color=colores[item.colorscheme]
                
            #txt = font.render ( formatear(item['summary']) , antialias, (99,99,99) )
            
            txt=textrect.render_textrect(formatear(item.summary), font, pygame.Rect(0,0,150,350), (99,99,99),  None ,1)
            
            txt=txt.subsurface(txt.get_bounding_rect())
            txt_rect = txt.get_rect()
            txt_rect.center=( (item.xpos-min_x)/factor , (item.ypos-min_y)/factor )
            
            inflate_rect=txt_rect.inflate(15,15)
            self.data.rects[item.id]=inflate_rect
            pygame.draw.rect(self.surface, color[0], inflate_rect)
            
            if not item.text in ('<html></html>',''):
                imagen='images/text.png'
                img_text=pygame.image.load(imagen).convert_alpha()
                rect_img_text=img_text.get_rect()
                rect_img_text.topright =inflate_rect.topright
                self.surface.blit(img_text,rect_img_text)
                
            #w=1 if item.text in ('<html></html>','') else 4
            w=1
            pygame.draw.rect(self.surface, color[1], inflate_rect, w)

            
            item.flag.sort()
            for nf , flag in enumerate(item.flag):
                #[(e,item.flag[e]) for e in range(len(item.flag))]:
                flag=item.flag[nf]
                rect=self.icons[flag].get_rect()
                rect.bottomright=inflate_rect.topright
                rect.x-=rect.w*nf
                self.surface.blit(self.icons[flag],rect)
            
            self.surface.blit(txt,txt_rect)
            
            rect=self.surface.get_rect()
