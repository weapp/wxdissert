import wx

class TBVERT (wx.ToolBar):
    def __init__(self,parent):
        wx.ToolBar.__init__(self,parent, -1, wx.DefaultPosition, wx.DefaultSize,
                         wx.TB_FLAT | wx.TB_NODIVIDER | wx.TB_VERTICAL)
        
        
        self.SetToolBitmapSize(wx.Size(48, 48))
        #b=self.AddLabelTool(101, "Test", wx.ArtProvider_GetBitmap(wx.ART_ERROR)) 
        #self.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle, b)
        #self.AddSeparator()
        self.AddCheckTool(103, wx.Bitmap("famfamfam/error.png", wx.BITMAP_TYPE_PNG))
        self.AddCheckTool(103, wx.Bitmap("famfamfam/star.png", wx.BITMAP_TYPE_PNG))
        self.AddCheckTool(103, wx.Bitmap("famfamfam/lightbulb_off.png", wx.BITMAP_TYPE_PNG))
        self.AddCheckTool(103, wx.Bitmap("famfamfam/wrench_orange.png", wx.BITMAP_TYPE_PNG))
        self.AddCheckTool(103, wx.Bitmap("famfamfam/zoom.png", wx.BITMAP_TYPE_PNG))
        self.AddCheckTool(103, wx.Bitmap("famfamfam/help.png", wx.BITMAP_TYPE_PNG))
        self.AddCheckTool(103, wx.Bitmap("famfamfam/bin.png", wx.BITMAP_TYPE_PNG))
        self.AddCheckTool(103, wx.Bitmap("famfamfam/group.png", wx.BITMAP_TYPE_PNG))
        self.AddCheckTool(103, wx.Bitmap("famfamfam/exclamation.png", wx.BITMAP_TYPE_PNG))
        self.Realize()
        
                                
        #['AddCheckLabelTool', 'AddCheckTool', 'AddChild', 'AddControl', 'AddLabelTool', 'AddPendingEvent', 'AddRadioLabelTool', 'AddRadioTool', 'AddSeparator', 'AddSimpleTool', 'AddTool', 'AddToolItem']
        #print filter(lambda x:x[:3]=='Add',dir(self))

        

    def PaneInfo(self):
        return wx.aui.AuiPaneInfo().Name("tbvert").Caption("Sample Vertical Toolbar"). \
            ToolbarPane().Right().GripperTop().TopDockable(False).BottomDockable(False)
