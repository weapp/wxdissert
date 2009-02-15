import wx

class TB3 (wx.ToolBar):
    def __init__(self,parent):
        wx.ToolBar.__init__(self,parent, -1, wx.DefaultPosition, wx.DefaultSize,
                         wx.TB_FLAT | wx.TB_NODIVIDER)
        self.SetToolBitmapSize(wx.Size(24,24))
        self_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER,wx.Size(24, 24))
        
        
        bmp = wx.Bitmap("famfamfam/cursor.png", wx.BITMAP_TYPE_PNG)
        self.AddRadioLabelTool(wx.ID_DEFAULT, "Seleccionar Hojas", bmp)
        bmp = wx.Bitmap("famfamfam/add.png", wx.BITMAP_TYPE_PNG)
        self.AddRadioLabelTool(402, "Enlazar Hojas", bmp)
        bmp = wx.Bitmap("famfamfam/arrow_switch.png", wx.BITMAP_TYPE_PNG)
        self.AddRadioLabelTool(403, "Organizar Subarboles", bmp)
        bmp = wx.Bitmap("famfamfam/eye.png", wx.BITMAP_TYPE_PNG)
        self.AddRadioLabelTool(404, "Desplazamiento", bmp)
        
        self.Realize()

    def PaneInfo(self):
        return wx.aui.AuiPaneInfo().Name("tb3").Caption("Toolbar 3").ToolbarPane() \
             .Top().Row(1).Position(1).LeftDockable(False).RightDockable(False)
