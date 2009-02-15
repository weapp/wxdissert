#!/usr/bin/env python
#-*- coding:utf-8 -*-


import wx

class MioFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Toolbar")
        self.CreateStatusBar()

        # wx.ID utilizzati dal pulsante e dal combo
        # inseriti nella toolbar.
        wx.ID_INFO = wx.ID_ANY
        wx.ID_COMBO = wx.ID_ANY
        tb = self.CreateToolBar(wx.TB_HORIZONTAL|
                                wx.NO_BORDER|wx.TB_FLAT)

        # bmp contiene un'immagine caricata dal
        # file "nuovo.bmp".
        bmp = wx.Bitmap("famfamfam/page_white.png", wx.BITMAP_TYPE_PNG)
        tb.AddSimpleTool(wx.ID_INFO, bmp, "Nuovo",
                         "Crea un nuovo documento")
        # Alla pressione del pulsante viene chiamata self.OnNuovo.
        wx.EVT_TOOL(self, wx.ID_INFO, self.OnNuovo)

        # Aggiunge un separatore fra i due controlli.
        tb.AddSeparator()

        # Viene creato un combo box, maggiori informazioni
        # saranno date nei capitoli successivi.
        combo = wx.ComboBox(tb, wx.ID_COMBO, choices =
                           ["Ciao", "sono", "un", "combobox"])
        # Il combo box appena creato viene inserito
        # nella tool bar.
        tb.AddControl(combo)
        # Quando viene cambiata la selezione nel combobox
        # viene chiamata self.on_combo.
        wx.EVT_COMBOBOX(self, wx.ID_COMBO, self.OnCombo)

        # Realize deve essere chiamata affinché i cambiamenti
        # fatti alla toolbar siano visibili.
        tb.Realize()


    def OnNuovo(self, event):
        wx.MessageBox("Questo funzione dovrebbe creare "
                     "un nuovo documento ma non e "
                     "stata implementata.")

    def OnCombo(self, event):
        # Nella versione di wx.Python utilizzata per la
        # scrittura del tutorial questa funzione
        # viene richiamata 3 volte a causa di un bug.
        wx.MessageBox("La selezione del combobox e "
                     "stata cambiata.")


class MiaApp(wx.App):
    def OnInit(self):
        frame = MioFrame()
        frame.Show(1)
        self.SetTopWindow(frame)
        return 1

app = MiaApp()
app.MainLoop()
