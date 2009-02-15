# create menu
mb = wx.MenuBar()

file_menu = wx.Menu()
file_menu.Append(wx.ID_EXIT, "Exit")

view_menu = wx.Menu()
view_menu.Append(ID_CreateText, "Create Text Control")
view_menu.Append(ID_CreateHTML, "Create HTML Control")
view_menu.Append(ID_CreateTree, "Create Tree")
view_menu.Append(ID_CreateGrid, "Create Grid")
view_menu.Append(ID_CreateSizeReport, "Create Size Reporter")
view_menu.AppendSeparator()
view_menu.Append(ID_GridContent, "Use a Grid for the Content Pane")
view_menu.Append(ID_TextContent, "Use a Text Control for the Content Pane")
view_menu.Append(ID_HTMLContent, "Use an HTML Control for the Content Pane")
view_menu.Append(ID_TreeContent, "Use a Tree Control for the Content Pane")
view_menu.Append(ID_SizeReportContent, "Use a Size Reporter for the Content Pane")    
   
options_menu = wx.Menu()
options_menu.AppendRadioItem(ID_TransparentHint, "Transparent Hint")
options_menu.AppendRadioItem(ID_VenetianBlindsHint, "Venetian Blinds Hint")
options_menu.AppendRadioItem(ID_RectangleHint, "Rectangle Hint")
options_menu.AppendRadioItem(ID_NoHint, "No Hint")
options_menu.AppendSeparator();
options_menu.AppendCheckItem(ID_HintFade, "Hint Fade-in")
options_menu.AppendCheckItem(ID_AllowFloating, "Allow Floating")
options_menu.AppendCheckItem(ID_NoVenetianFade, "Disable Venetian Blinds Hint Fade-in")
options_menu.AppendCheckItem(ID_TransparentDrag, "Transparent Drag")
options_menu.AppendCheckItem(ID_AllowActivePane, "Allow Active Pane")
options_menu.AppendSeparator();
options_menu.AppendRadioItem(ID_NoGradient, "No Caption Gradient")
options_menu.AppendRadioItem(ID_VerticalGradient, "Vertical Caption Gradient")
options_menu.AppendRadioItem(ID_HorizontalGradient, "Horizontal Caption Gradient")
options_menu.AppendSeparator();
options_menu.Append(ID_Settings, "Settings Pane")

self._perspectives_menu = wx.Menu()
self._perspectives_menu.Append(ID_CreatePerspective, "Create Perspective")
self._perspectives_menu.Append(ID_CopyPerspective, "Copy Perspective Data To Clipboard")
self._perspectives_menu.AppendSeparator()
self._perspectives_menu.Append(ID_FirstPerspective+0, "Default Startup")
self._perspectives_menu.Append(ID_FirstPerspective+1, "All Panes")
self._perspectives_menu.Append(ID_FirstPerspective+2, "Vertical Toolbar")

help_menu = wx.Menu()
help_menu.Append(ID_About, "About...")

mb.Append(file_menu, "File")
mb.Append(view_menu, "View")
mb.Append(self._perspectives_menu, "Perspectives")
mb.Append(options_menu, "Options")
mb.Append(help_menu, "Help")

#self.SetMenuBar(mb)
