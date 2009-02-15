import wx

class TB1 (wx.ToolBar):
    def __init__(self,parent):
        wx.ToolBar.__init__(self,parent, -1, wx.DefaultPosition, wx.DefaultSize,
                         wx.TB_FLAT | wx.TB_NODIVIDER)
        
        self.parent=parent
        
        self.SetToolBitmapSize(wx.Size(48,48))
        self.AddLabelTool(101, "Test", wx.ArtProvider_GetBitmap(wx.ART_ERROR))
        self.AddSeparator()
        self.AddLabelTool(102, "Test", wx.ArtProvider_GetBitmap(wx.ART_QUESTION))
        self.AddLabelTool(103, "Test", wx.ArtProvider_GetBitmap(wx.ART_INFORMATION))
        self.AddLabelTool(103, "Test", wx.ArtProvider_GetBitmap(wx.ART_WARNING))
        self.AddLabelTool(103, "Test", wx.ArtProvider_GetBitmap(wx.ART_MISSING_IMAGE))
        self.Realize()

    def PaneInfo(self):
        return wx.aui.AuiPaneInfo().Name("tb1").Caption("Big Toolbar"). \
               ToolbarPane().Top().LeftDockable(False).RightDockable(False)
