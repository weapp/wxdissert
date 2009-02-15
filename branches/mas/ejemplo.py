# use a wx.BoxSizer(orient) for widget layout
# wx.VERTICAL = stacked vertically
# wx.HORIZONTAL = stacked horizontally (default)
# add widget with Add() --> has options ...
# proportion=0 no vertical stretch with frame stretch in sizer_v
# proportion=1 stretch with frame stretch
# proportion=2 fill remaining space proportional (eg. 1:2)
# proportion=3 fill remaining space proportional (eg. 1:3)
# border=10 pixel border around each
# flag=wx.ALL puts the specified border on all sides
# (also has wx.LEFT wx.RIGHT wx.TOP and wx.BOTTOM)
# flag=wx.EXPAND --> expand to fit frame
# flag=wx.SHAPED --> change size preserving original aspect ratio

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, mytitle, mysize, *args,**keys):
        wx.Frame.__init__(self, parent, title=mytitle, size=mysize, *args, **keys )#wx.ID_ANY, mytitle, size=mysize)

        # Build the menu bar
        MenuBar = wx.MenuBar()

        FileMenu = wx.Menu()

        item = FileMenu.Append(wx.ID_EXIT, text="&Quit")
        self.Bind(wx.EVT_MENU, self.OnQuit, item)

        MenuBar.Append(FileMenu, "&File")
        self.SetMenuBar(MenuBar)

       
        #marco resizable
        splitter = MySplitter(self, -1)
        sty = wx.BORDER_SUNKEN
        
        p1 = wx.Window(splitter, style=sty)
        p1.SetBackgroundColour("pink")
        wx.StaticText(p1, -1, "Panel One", (5,5))

        p2 = wx.Window(splitter, style=sty)
        p2.SetBackgroundColour("sky blue")
        wx.StaticText(p2, -1, "Panel Two", (5,5))

        splitter.SetMinimumPaneSize(20)
        splitter.SplitVertically(p1, p2, -100)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter, proportion=1, flag=wx.EXPAND|wx.ALL)
        





        # only set the main sizer
        #self.SetSizer(sizer)
        # in some cases you may want to use this to fit the frame
        # around the sizer area
        self.SetSizerAndFit(sizer_v)


    
    def OnQuit(self, event=None):
        """Exit application."""
        self.Close()


class MySplitter(wx.SplitterWindow):
    def __init__(self, parent, ID):
        wx.SplitterWindow.__init__(self, parent, ID,
                                   style = wx.SP_LIVE_UPDATE
                                   )
        #self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnSashChanged)
        #self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGING, self.OnSashChanging)

    def OnSashChanged(self, evt):
        self.log.WriteText("sash changed to %s\n" % str(evt.GetSashPosition()))

    def OnSashChanging(self, evt):
        self.log.WriteText("sash changing to %s\n" % str(evt.GetSashPosition()))
        # uncomment this to not allow the change
        #evt.SetSashPosition(-1)



app = wx.App(0)
mytitle = "wx.BoxSizer() Test"
width = 300
height = 320
# create a MyFrame instance and show the frame
MyFrame(None, mytitle, (width, height)).Show()
app.MainLoop()

