#!/usr/bin/env python2.4

try:
    import treemixin 
except ImportError:
    from wx.lib.mixins import treemixin

import wx, wx.lib.customtreectrl, wx.gizmos, wx.aui, os, images

"""
treemodel = kwargs.pop('treemodel')
        super(TreeNotebook, self).__init__(*args, **kwargs)
        self.trees = []
        for class_, title in [(VirtualTreeCtrl, 'TreeCtrl'),
                              (VirtualTreeListCtrl, 'TreeListCtrl'),
                              (VirtualCustomTreeCtrl, 'CustomTreeCtrl')]:
            tree = class_(self, treemodel=treemodel)
            treemodel = TreeModel()
        super(TreeNotebook, self).__init__(*args, **kwargs)
        self.trees = []
        for class_, title in [(VirtualTreeCtrl, 'TreeCtrl'),
                              (VirtualTreeListCtrl, 'TreeListCtrl'),
                              (VirtualCustomTreeCtrl, 'CustomTreeCtrl')]:
            tree = class_(self, treemodel=treemodel)
"""


class DemoTreeMixin(treemixin.VirtualTree, treemixin.DragAndDrop, 
                    treemixin.ExpansionState):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('treemodel')
        self.log = kwargs.pop('log')
        super(DemoTreeMixin, self).__init__(*args, **kwargs)
        self.CreateImageList()

    def CreateImageList(self):
        size = (16, 16)
        self.imageList = wx.ImageList(*size)
        for art in wx.ART_FOLDER, wx.ART_FILE_OPEN, wx.ART_NORMAL_FILE:
            self.imageList.Add(wx.ArtProvider.GetBitmap(art, wx.ART_OTHER, 
                                                        size))
        self.AssignImageList(self.imageList)

    def OnGetItemText(self, indices):
        return self.model.GetText(indices)

    def OnGetChildrenCount(self, indices):
        return self.model.GetChildrenCount(indices)

    def OnGetItemFont(self, indices):
        # Show how to change the item font. Here we use a small font for
        # items that have children and the default font otherwise.
        if self.model.GetChildrenCount(indices) > 0:
            return wx.SMALL_FONT
        else:
            return super(DemoTreeMixin, self).OnGetItemFont(indices)

    def OnGetItemTextColour(self, indices):
        # Show how to change the item text colour. In this case second level
        # items are coloured red and third level items are blue. All other
        # items have the default text colour.
        if len(indices) % 2 == 0:
            return wx.RED
        elif len(indices) % 3 == 0:
            return wx.BLUE
        else:
            return super(DemoTreeMixin, self).OnGetItemTextColour(indices)

    def OnGetItemBackgroundColour(self, indices):
        # Show how to change the item background colour. In this case the
        # background colour of each third item is green.
        if indices[-1] == 2:
            return wx.GREEN
        else: 
            return super(DemoTreeMixin, 
                         self).OnGetItemBackgroundColour(indices)

    def OnGetItemImage(self, indices, which):
        # Return the right icon depending on whether the item has children.
        if which in [wx.TreeItemIcon_Normal, wx.TreeItemIcon_Selected]:
            if self.model.GetChildrenCount(indices):
                return 0
            else:
                return 2
        else:
            return 1

    def OnDrop(self, dropTarget, dragItem):
        dropIndex = self.GetIndexOfItem(dropTarget)
        dropText = self.model.GetText(dropIndex)
        dragIndex = self.GetIndexOfItem(dragItem)
        dragText = self.model.GetText(dragIndex)
        self.log.write('drop %s %s on %s %s'%(dragText, dragIndex,
            dropText, dropIndex))
        self.model.MoveItem(dragIndex, dropIndex)
        self.GetParent().RefreshItems()




class VirtualTreeListCtrl(DemoTreeMixin, wx.gizmos.TreeListCtrl):
    def __init__(self, *args, **kwargs):
        kwargs['style'] = wx.TR_DEFAULT_STYLE | wx.TR_FULL_ROW_HIGHLIGHT
        super(VirtualTreeListCtrl, self).__init__(*args, **kwargs)
        self.AddColumn('Column 0')
        self.AddColumn('Column 1')
        for art in wx.ART_TIP, wx.ART_WARNING:
            self.imageList.Add(wx.ArtProvider.GetBitmap(art, wx.ART_OTHER, 
                                                        (16, 16)))


class DemoPanel(wx.Panel):
    """This Panel hold two simple buttons, but doesn't really do anything."""
    def __init__(self, parent, *args, **kwargs):
        """Create the DemoPanel."""
        wx.Panel.__init__(self, parent, *args, **kwargs)

        
        Sizer = wx.BoxSizer(wx.VERTICAL)

        #divisor
        splitter = wx.SplitterWindow(self,style=wx.SPLIT_VERTICAL)
        
        
        splitter.SetSplitMode(wx.SPLIT_VERTICAL)

        #splitter.SplitHorizontally() 	    
        
        sty = wx.BORDER_SUNKEN
        
        p1 = wx.Window(splitter, style=sty | wx.HSCROLL)
        p1.SetBackgroundColour("pink")
        wx.StaticText(p1, -1, "Panel One", (5,5))

        p2 = wx.Window(splitter, style=sty)
        p2.SetBackgroundColour("sky blue")
        wx.StaticText(p2, -1, "Panel Two", (5,5))

        splitter.SetMinimumPaneSize(20)
        
        #splitter.SplitVertically(p1, p2, -100)
        splitter.SplitHorizontally(p1, p2)

        Sizer.Add(splitter, proportion=1, flag=wx.EXPAND|wx.ALL)
        self.SetSizer(Sizer)

class DemoFrame(wx.Frame):
    """Main Frame holding the Panel."""
    def __init__(self, *args, **kwargs):
        """Create the DemoFrame."""
        wx.Frame.__init__(self, *args, **kwargs)

        # Build the menu bar
        MenuBar = wx.MenuBar()

        FileMenu = wx.Menu()
        EditMenu = wx.Menu()
        ViewMenu = wx.Menu()
        ToolsMenu = wx.Menu()
        SettingsMenu = wx.Menu()
        HelpMenu = wx.Menu()
        AllMenu = wx.Menu()

        ids=filter(lambda x: x[:3] == 'ID_' ,dir(wx))
        
        for id in ids:
            AllMenu.Append(getattr(wx,id), text=id)
       
        item = FileMenu.Append(wx.ID_NEW, text="&New")
        item = FileMenu.Append(wx.ID_SEPARATOR)
        item = FileMenu.Append(wx.ID_OPEN, text="&Open...")
        
        OpenRecentsSubMenu = wx.Menu()
        self.filehistory = wx.FileHistory()
        self.filehistory.UseMenu(OpenRecentsSubMenu)
        FileMenu.AppendMenu(103, "Open &Recents", OpenRecentsSubMenu)
        #self.Bind(wx.EVT_MENU_RANGE, self.OnFileHistory, id=wx.ID_FILE1, id2=wx.ID_FILE9)
        #item = FileMenu.Append(wx.ID_OPEN, text="&OpenRecents")
        FileMenu.Enable(103, False)
        
        item = FileMenu.Append(wx.ID_SAVE, text="&Save")
        item = FileMenu.Append(wx.ID_SAVEAS, text="Save &As...")
        item = FileMenu.Append(wx.ID_PRINT, text="&Print...")
        item = FileMenu.AppendSeparator()
        item = FileMenu.Append(wx.ID_CLOSE, text="&Close")
        item = FileMenu.AppendSeparator()
        item = FileMenu.Append(wx.ID_EXIT, text="&Quit")
        self.Bind(wx.EVT_MENU, self.OnQuit, item)
        
        item = HelpMenu.Append(wx.ID_HELP, text="&Help\tF1")
        item = HelpMenu.Append(wx.ID_ABOUT, text="&About...")
        
        item = EditMenu.Append(wx.ID_UNDO, text="&Undo")
        item = EditMenu.Append(wx.ID_REDO, text="Re&do")
        item = EditMenu.AppendSeparator()
        item = EditMenu.Append(203, text="&Importar Datos...")
        item = EditMenu.AppendSeparator()
        item = EditMenu.Append(204, text="&Reorganizar el Mapa\tCtrl+G")
        EditMenu.Enable(204, False)
        
        MoverSeleccionSubMenu = wx.Menu()
        EditMenu.AppendMenu(205, "&Mover Seleccion", MoverSeleccionSubMenu)
        
        AlignAndDistributeSubMenu = wx.Menu()
        EditMenu.AppendMenu(206, "A&lign and Distribute", AlignAndDistributeSubMenu)
        
        AdicionarObjetosSubMenu = wx.Menu()
        EditMenu.AppendMenu(207, "&Adicionar Objetos", AdicionarObjetosSubMenu)
        
        item = EditMenu.AppendSeparator()
        item = EditMenu.Append(wx.ID_PROPERTIES, text="&Propiedades del Documento")
        
        ZoomSubMenu = wx.Menu()
        ViewMenu.AppendMenu(301, "&Zoom", ZoomSubMenu)
        
        item = ViewMenu.Append(wx.ID_ZOOM_IN, text="Zoom &In")
        item = ViewMenu.Append(wx.ID_ZOOM_OUT, text="Zoom &Out")
        item = ViewMenu.Append(wx.ID_ZOOM_FIT, text="Zoom &Fit")
        item = ViewMenu.Append(wx.ID_ZOOM_100, text="Zoom &100")
        
        item = ViewMenu.Append(306, text="Efocar >")
        item = ViewMenu.Append(307, text="ToolViews > paneles")
        item = ViewMenu.Append(308, text="ToolDock >")
        
        item = ToolsMenu.AppendRadioItem(wx.ID_DEFAULT, "Seleccionar Hojas")
        item = ToolsMenu.AppendRadioItem(402, "&Enlazar Hojas")
        item = ToolsMenu.AppendRadioItem(403, "&Organizar Subarboles")
        item = ToolsMenu.AppendRadioItem(404, "&Desplazamiento")
        ToolsMenu.AppendSeparator()
        item = ToolsMenu.Append(405, text="&Generar Documentos...")
        item = ToolsMenu.Append(406, text="&Regenerar Documento")
        item = ToolsMenu.Append(407, text="&Crear Imagen...")
        ToolsMenu.AppendSeparator()
        item = ToolsMenu.Append(408, text="&Spelling...")
        
        
        item = SettingsMenu.AppendCheckItem(401, "Show Toolbar")
        item = SettingsMenu.AppendCheckItem(402, "Hide Statusbar")
        item = SettingsMenu.AppendSeparator()
        item = SettingsMenu.Append(403, text="Configure Shortcuts...")
        item = SettingsMenu.Append(404, text="Configure Toolbars...")
        item = SettingsMenu.Append(wx.ID_PREFERENCES, text="Configure Wxdissert...")
        
        MenuBar.Append(FileMenu, "&File")
        MenuBar.Append(EditMenu, "&Edit")
        MenuBar.Append(ViewMenu, "&View")
        MenuBar.Append(ToolsMenu, "&Tools")
        MenuBar.Append(SettingsMenu, "&Settings")
        MenuBar.Append(HelpMenu, "&Help")
        MenuBar.Append(AllMenu, "&All")
        
        
        
        self.SetMenuBar(MenuBar)

        # Add the Widget Panel
        #self.Panel = DemoPanel(self)
        
        pnl = wx.Panel(self)
        self.pnl = pnl
        
        self.mgr = wx.aui.AuiManager()
        self.mgr.SetManagedWindow(pnl)

        self.loaded = False
        self.cwd = os.getcwd()
        self.curOverview = ""
        self.demoPage = None
        self.codePage = None
        self.shell = None
        self.firstTime = True
        self.finddlg = None

        icon = images.WXPdemo.GetIcon()
        self.SetIcon(icon)
        
        self.otherWin = None
        
        self.Centre(wx.BOTH)
        self.CreateStatusBar(1, wx.ST_SIZEGRIP)

        self.dying = False
        self.skipLoad = False
        
        def EmptyHandler(evt): pass

        self.ReadConfigurationFile()
    
    
    
    def ReadConfigurationFile(self):

        self.auiConfigurations = {}
        self.expansionState = [0, 1]
        """
        config = GetConfig()
        val = config.Read('ExpansionState')
        if val:
            self.expansionState = eval(val)

        val = config.Read('AUIPerspectives')
        if val:
            self.auiConfigurations = eval(val)
        """

       
    def OnQuit(self, event=None):
        """Exit application."""
        self.Close()


    def OnFileOpenDialog(self, evt):
        #TODO no se lo que hace
        """COPIADOOOOOOOOOOOOOOOO"""
        dlg = wx.FileDialog(self,
                           defaultDir = os.getcwd(),
                           wildcard = "All Files|*",
                           style = wx.OPEN | wx.CHANGE_DIR)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.log.write("You selected %s\n" % path)

            # add it to the history
            self.filehistory.AddFileToHistory(path)

        dlg.Destroy()



if __name__ == '__main__':
    app = wx.App()
    width = 500
    height = 320
    frame = DemoFrame(None, title="Micro App",size=(width, height)) #ventana principal
    frame.Show()
    app.MainLoop()
