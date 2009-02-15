import wx

class TB4 (wx.ToolBar):

    def __init__(self,parent):
        self.parent=parent
        wx.ToolBar.__init__(self,parent, -1, wx.DefaultPosition, wx.DefaultSize,
                         wx.TB_FLAT | wx.TB_NODIVIDER) #| wx.TB_HORZ_TEXT)
                         
        self.SetToolBitmapSize(wx.Size(24,24))
        self_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER,wx.Size(24, 24))
        self.SetToolBitmapSize(wx.Size(24,24))
        self_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER,wx.Size(24, 24))
        
        
        """
        self.AddLabelTool(101, "Item 1", self_bmp1)
        self.AddLabelTool(101, "Item 2", self_bmp1)
        self.AddLabelTool(101, "Item 3", self_bmp1)
        self.AddLabelTool(101, "Item 4", self_bmp1)
        self.AddSeparator()
        self.AddLabelTool(101, "Item 5", self_bmp1)
        self.AddLabelTool(101, "Item 6", self_bmp1)
        self.AddLabelTool(101, "Item 7", self_bmp1)
        self.AddLabelTool(101, "Item 8", self_bmp1)
        """

        #self_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR,wx.Size(24, 24))
        png = wx.Bitmap("famfamfam/page_white_add.png", wx.BITMAP_TYPE_PNG)
        self.AddLabelTool(wx.ID_NEW, "New", png, longHelp="New")
        
        #self_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR,wx.Size(24, 24))
        png = wx.Bitmap("famfamfam/folder_page_white.png", wx.BITMAP_TYPE_PNG)
        self.AddLabelTool(wx.ID_OPEN, "Open", png)
        
        #self_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_CROSS_MARK, wx.ART_TOOLBAR,wx.Size(24, 24))
        png = wx.Bitmap("famfamfam/page_white_add.png", wx.BITMAP_TYPE_PNG)
        self.AddLabelTool(wx.ID_CLOSE, "Close", png)
        
        #self_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR,wx.Size(24, 24))
        png = wx.Bitmap("famfamfam/disk.png", wx.BITMAP_TYPE_PNG)
        self.AddLabelTool(wx.ID_CLOSE, "File Save", png)
        
        #self_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR,wx.Size(24, 24))
        png = wx.Bitmap("famfamfam/disk_multiple.png", wx.BITMAP_TYPE_PNG)
        self.AddLabelTool(wx.ID_CLOSE, "File Save As...", png)
        
        #self_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_UNDO, wx.ART_TOOLBAR,wx.Size(24, 24))
        png = wx.Bitmap("famfamfam/arrow_undo.png", wx.BITMAP_TYPE_PNG)
        self.AddLabelTool(wx.ID_UNDO, "Undo", png)
        
        #self_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_REDO, wx.ART_TOOLBAR,wx.Size(24, 24))
        png = wx.Bitmap("famfamfam/arrow_redo.png", wx.BITMAP_TYPE_PNG)
        self.AddLabelTool(wx.ID_REDO, "Redo", png)
        
        
        #for art in filter(lambda x:x[0:4] == 'ART_',dir(wx)):
        #    print '"wx.%s",'% art
        #    self_bmpX = wx.ArtProvider_GetBitmap(getattr(wx,art), wx.ART_OTHER,wx.Size(24, 24))
        #    self.AddLabelTool(101, art[4:], self_bmpX)
        
        self.Realize()


    def AddPane(self):
        self.parent._mgr.AddPane(self, self.PaneInfo())
                  
    def PaneInfo(self):
        return wx.aui.AuiPaneInfo().Name("tb4").Caption("General"). \
            ToolbarPane().Top().Row(1).LeftDockable(False).RightDockable(False)
