from wxPython.wx import *

class MioFrame(wxFrame):
    def __init__(self):
        # Chiama il costruttore di wxFrame.
        wxFrame.__init__(self, None, -1, "Prova con i menu")

        ID_INFO = wxNewId()
        ID_ESCI = wxNewId()
        menu_file = wxMenu()
        menu_file.Append(ID_INFO, "&Informazioni...",
                         "Qualche informazione sul programma")
        menu_file.AppendSeparator()
        menu_file.Append(ID_ESCI, "&Esci",
                         "Esci dal programma")
        EVT_MENU(self, ID_INFO, self.OnInfo)
        EVT_MENU(self, ID_ESCI, self.OnEsci)

        menu_bar = wxMenuBar()
        menu_bar.Append(menu_file, "&File");
        self.SetMenuBar(menu_bar)

        # Crea una barra di stato con due pannelli.
        self.CreateStatusBar()
        # Imposta il testo della barra di stato.
        self.SetStatusText("Semplice barra di stato")

    def OnInfo(self, event):
        # Mostra un semplice messaggio.
        wxMessageBox("Questo programma mostra "
                     "come usare i menu")

    def OnEsci(self, event):
        # Distrugge il frame.
        self.Close(1)


class MiaApp(wxApp):
    def OnInit(self):
        frame = MioFrame()
        frame.Show(1)
        self.SetTopWindow(frame)
        return 1

app = MiaApp()
app.MainLoop()