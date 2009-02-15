#!/usr/bin/env python
#-*- coding:utf-8 -*-

from library.sidebar import *

class SideInfo(Sidebar):
    def __init__(self,surface,kdi):
        Sidebar.__init__(self,surface)
        self.kdi=kdi
        
    def draw(self):
        if self.kdi.actual_selected:
            Sidebar.draw(self)
            
            it=self.kdi.data.item_by_id[self.kdi.actual_selected]
            txts = [ 'Item:','id: %d'%it.id , it.summary , '\n'+' -'*20+' ' , it.text]
            self.render_text_sidebar(txts,100,(0,20),(0,30))
            
            init=(25,225)
            paso=(25,0)
            
            self.buttons=[Button(i,self.kdi.icons[i],'enable' if i in it.flag else'disable') for i in range(len(self.kdi.icons)) ]
            
            self.render_button_sidebar(self.buttons[:5],init,paso)
            
            init=(25+25/2,250)
            self.render_button_sidebar(self.buttons[5:],init,paso)
        
    def new_event(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN and self.kdi.actual_selected:
            if self.rect.collidepoint(event.pos):
                for button in self.buttons:
                    if button.rect.collidepoint(event.pos):
                        it=self.kdi.data.item_by_id[self.kdi.actual_selected]
                        if button.id in it.flag:
                            it.flag.remove(button.id)
                        else:
                            it.flag.append(button.id)
                        self.kdi.render()
                return True
            
            
