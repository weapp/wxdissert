from wxPython.wx import *

class MiaApp(wxApp):
    def OnInit(self):
        frame = wxFrame(None, -1, "Ciao mondo")
        # viene mostrata la finestra
        frame.Show(1)
        # imposta la finestra principale
        self.SetTopWindow(frame)
        return 1

# crea un'istanza della classe MiaApp
app = MiaApp(0)
app.MainLoop()
