import wx

class TB2 (wx.ToolBar):
    def __init__(self,parent):
        wx.ToolBar.__init__(self,parent, -1, wx.DefaultPosition, wx.DefaultSize,
                         wx.TB_FLAT | wx.TB_NODIVIDER)
        self.SetToolBitmapSize(wx.Size(24,24))
        self_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_QUESTION, wx.ART_OTHER,wx.Size(24, 24))
        
        buttons=[(101, "Test", self_bmp1),]*9
        buttons.insert(3,'separator')
        for tuple_ in buttons:
            if tuple_ == 'separator':
                self.AddSeparator()
            else:
                self.AddLabelTool(*tuple_)    
        self.Realize()
    
    def PaneInfo(self):
        return wx.aui.AuiPaneInfo().Name("tb2").Caption("Toolbar 2"). \
            ToolbarPane().Top().Row(2).LeftDockable(False).RightDockable(False)
