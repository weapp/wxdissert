#!/bin/env python
#----------------------------------------------------------------------------
# Name:         Main.py
# Purpose:      Testing lots of stuff, controls, window types, etc.
#
# Author:       Robin Dunn
#
# Created:      A long time ago, in a galaxy far, far away...
# RCS-ID:       $Id: Main.py 55621 2008-09-14 19:55:48Z RD $
# Copyright:    (c) 1999 by Total Control Software
# Licence:      wxWindows license
#----------------------------------------------------------------------------

# FIXME List:
# * Problems with flickering related to ERASE_BACKGROUND
#     and the splitters. Might be a problem with this 2.5 beta...?
#     UPDATE: can't see on 2.5.2 GTK - maybe just a faster machine :)
# * Demo Code menu?
# * Annoying switching between tabs and resulting flicker
#     how to replace a page in the notebook without deleting/adding?
#     Where is SetPage!? tried freeze...tried reparent of dummy panel....
#     AG: It looks like this issue is fixed by Freeze()ing and Thaw()ing the
#         main frame and not the notebook

# TODO List:
# * UI design more professional (is the new version more professional?)
# * save file positions (new field in demoModules) (@ LoadDemoSource)
# * Update main overview

# * Why don't we move _treeList into a separate module

import sys, os, time, traceback, types

import wx              
import wx.aui
import wx.html

import version

# We won't import the images module yet, but we'll assign it to this
# global when we do.
######################images = None
import images 

# For debugging
##wx.Trap();
##print "wx.VERSION_STRING = %s (%s)" % (wx.VERSION_STRING, wx.USE_UNICODE and 'unicode' or 'ansi')
##print "pid:", os.getpid()
##raw_input("Press Enter...")


#---------------------------------------------------------------------------

USE_CUSTOMTREECTRL = False
ALLOW_AUI_FLOATING = False
DEFAULT_PERSPECTIVE = "Default Perspective"

#---------------------------------------------------------------------------



mainOverview = """<html><body>
<h2>wxPython</h2>

<p> wxPython is a <b>GUI toolkit</b> for the Python programming
language.  It allows Python programmers to create programs with a
robust, highly functional graphical user interface, simply and easily.
It is implemented as a Python extension module (native code) that
wraps the popular wxWindows cross platform GUI library, which is
written in C++.

<p> Like Python and wxWindows, wxPython is <b>Open Source</b> which
means that it is free for anyone to use and the source code is
available for anyone to look at and modify.  Or anyone can contribute
fixes or enhancements to the project.

<p> wxPython is a <b>cross-platform</b> toolkit.  This means that the
same program will run on multiple platforms without modification.
Currently supported platforms are 32-bit Microsoft Windows, most Unix
or unix-like systems, and Macintosh OS X. Since the language is
Python, wxPython programs are <b>simple, easy</b> to write and easy to
understand.

<p> <b>This demo</b> is not only a collection of test cases for
wxPython, but is also designed to help you learn about and how to use
wxPython.  Each sample is listed in the tree control on the left.
When a sample is selected in the tree then a module is loaded and run
(usually in a tab of this notebook,) and the source code of the module
is loaded in another tab for you to browse and learn from.

"""



"""
class Share (object):
    def __init__(self):
        pass
"""

share=type('Share', (), {})()

share.demoPngs = ["overview", "recent", "frame", "dialog", "moredialog", "core",
             "book", "customcontrol", "morecontrols", "layout", "process", "clipboard",
             "images", "miscellaneous"]

share.treeList = [
    # new stuff
    ('Recent Additions/Updates', [
        'RichTextCtrl',
        'Treebook',
        'Toolbook',
        'BitmapFromBuffer',
        'RawBitmapAccess',
        'DragScroller',
        'DelayedResult',
        'ExpandoTextCtrl',
        'ButtonPanel',
        'FlatNotebook',
        'CustomTreeCtrl',
        'AboutBox',
        'AlphaDrawing',
        'GraphicsContext',
        'CollapsiblePane',
        'ComboCtrl',
        'OwnerDrawnComboBox',
        'BitmapComboBox',
        'I18N',
        'Img2PyArtProvider',
        'SearchCtrl',
        'SizedControls',
        'AUI_MDI',
        'TreeMixin',
        'AdjustChannels',
        'RendererNative',
        'PlateButton',
        'ResizeWidget',
        'Cairo',
        'Cairo_Snippets',
        ]),

    # managed windows == things with a (optional) caption you can close
    ('Frames and Dialogs', [
        'AUI_DockingWindowMgr',
        'AUI_MDI',
        'Dialog',
        'Frame',
        'MDIWindows',
        'MiniFrame',
        'Wizard',
        ]),

    # the common dialogs
    ('Common Dialogs', [
        'AboutBox',
        'ColourDialog',
        'DirDialog',
        'FileDialog',
        'FindReplaceDialog',
        'FontDialog',
        'MessageDialog',
        'MultiChoiceDialog',
        'PageSetupDialog',
        'PrintDialog',
        'ProgressDialog',
        'SingleChoiceDialog',
        'TextEntryDialog',
        ]),

    # dialogs from libraries
    ('More Dialogs', [
        'ImageBrowser',
        'ScrolledMessageDialog',
        ]),

    # core controls
    ('Core Windows/Controls', [
        'BitmapButton',
        'Button',
        'CheckBox',
        'CheckListBox',
        'Choice',
        'ComboBox',
        'Gauge',
        'Grid',
        'Grid_MegaExample',
        'ListBox',
        'ListCtrl',
        'ListCtrl_virtual',
        'ListCtrl_edit',
        'Menu',
        'PopupMenu',
        'PopupWindow',
        'RadioBox',
        'RadioButton',
        'SashWindow',
        'ScrolledWindow',
        'SearchCtrl',        
        'Slider',
        'SpinButton',
        'SpinCtrl',
        'SplitterWindow',
        'StaticBitmap',
        'StaticBox',
        'StaticText',
        'StatusBar',
        'StockButtons',
        'TextCtrl',
        'ToggleButton',
        'ToolBar',
        'TreeCtrl',
        'Validator',
        ]),
    
    ('"Book" Controls', [
        'AUI_Notebook',
        'Choicebook',
        'FlatNotebook',
        'Listbook',
        'Notebook',
        'Toolbook',
        'Treebook',
        ]),

    ('Custom Controls', [
        'AnalogClock',
        'ButtonPanel',
        'ColourSelect',
        'ComboTreeBox',
        'CustomTreeCtrl',
        'Editor',
        'FlatNotebook',
        'GenericButtons',
        'GenericDirCtrl',
        'LEDNumberCtrl',
        'MultiSash',
        'PlateButton',
        'PopupControl',
        'PyColourChooser',
        'TreeListCtrl',
    ]),
    
    # controls coming from other libraries
    ('More Windows/Controls', [
        'ActiveX_FlashWindow',
        'ActiveX_IEHtmlWindow',
        'ActiveX_PDFWindow',
        'BitmapComboBox',
        'Calendar',
        'CalendarCtrl',
        'CheckListCtrlMixin',
        'CollapsiblePane',
        'ComboCtrl',
        'ContextHelp',
        'DatePickerCtrl',
        'DynamicSashWindow',
        'EditableListBox',
        'ExpandoTextCtrl',
        'FancyText',
        'FileBrowseButton',
        'FloatBar',  
        'FloatCanvas',
        'FoldPanelBar',
        'HtmlWindow',
        'HyperLinkCtrl',
        'IntCtrl',
        'MVCTree',   
        'MaskedEditControls',
        'MaskedNumCtrl',
        'MediaCtrl',
        'MultiSplitterWindow',
        'OwnerDrawnComboBox',
        'Pickers',
        'PyCrust',
        'PyPlot',
        'PyShell',
        'ResizeWidget',
        'RichTextCtrl',
        'ScrolledPanel',
        'SplitTree',
        'StyledTextCtrl_1',
        'StyledTextCtrl_2',
        'TablePrint',
        'Throbber',
        'Ticker',
        'TimeCtrl',
        'TreeMixin',
        'VListBox',
        ]),

    # How to lay out the controls in a frame/dialog
    ('Window Layout', [
        'GridBagSizer',
        'LayoutAnchors',
        'LayoutConstraints',
        'Layoutf',
        'RowColSizer',
        'ScrolledPanel',
        'SizedControls',
        'Sizers',
        'XmlResource',
        'XmlResourceHandler',
        'XmlResourceSubclass',
        ]),

    # ditto
    ('Process and Events', [
        'DelayedResult',
        'EventManager',
        'KeyEvents',
        'Process',
        'PythonEvents',
        'Threads',
        'Timer',
        ##'infoframe',    # needs better explanation and some fixing
        ]),

    # Clipboard and DnD
    ('Clipboard and DnD', [
        'CustomDragAndDrop',
        'DragAndDrop',
        'URLDragAndDrop',
        ]),

    # Images
    ('Using Images', [
        'AdjustChannels',
        'AlphaDrawing',
        'AnimateCtrl',
        'ArtProvider',
        'BitmapFromBuffer',
        'Cursor',
        'DragImage',
        'Image',
        'ImageAlpha',
        'ImageFromStream',
        'Img2PyArtProvider',
        'Mask',
        'RawBitmapAccess',
        'Throbber',
        ]),

    # Other stuff
    ('Miscellaneous', [
        'AlphaDrawing',
        'Cairo',
        'Cairo_Snippets',
        'ColourDB',
        ##'DialogUnits',   # needs more explanations
        'DragScroller',
        'DrawXXXList',
        'FileHistory',
        'FontEnumerator',
        'GraphicsContext',
        'GLCanvas',
        'I18N',        
        'Joystick',
        'MimeTypesManager',
        'MouseGestures',
        'OGL',
        'PrintFramework',
        'PseudoDC',
        'RendererNative',
        'ShapedWindow',
        'Sound',
        'StandardPaths',
        'Unicode',
        ]),


    ('Check out the samples dir too', [
        ]),

]

#---------------------------------------------------------------------------
# Show how to derive a custom wxLog class
from mylog import MyLog

#PyTipProvider
from mytp import MyTP

#---------------------------------------------------------------------------
# A class to be used to simply display a message in the demo pane
# rather than running the sample itself.
from messagepanel import MessagePanel
        

#---------------------------------------------------------------------------
# A class to be used to display source code in the demo.  Try using the
# wxSTC in the StyledTextCtrl_2 sample first, fall back to wxTextCtrl
# if there is an error, such as the stc module not being present.
#

from democodeeditor import DemoCodeEditor

#---------------------------------------------------------------------------
# Constants for module versions

from constants import *

#---------------------------------------------------------------------------


from democodepanel import DemoCodePanel

#---------------------------------------------------------------------------

from fun import *

#---------------------------------------------------------------------------

from demomodules import DemoModules

#---------------------------------------------------------------------------

from demoerror import DemoError

#---------------------------------------------------------------------------

from demoerrorpanel import DemoErrorPanel

#---------------------------------------------------------------------------

from demotaskbarticon import DemoTaskBarIcon

#---------------------------------------------------------------------------

from wxpythondemo import wxPythonDemo, wxPythonDemoTree


#---------------------------

from mysplashscreen import MySplashScreen

#---------------------------------------------------------------------------

############from wxpythondemotree import

#---------------------------------------------------------------------------


###############print dir().index('wxPythonDemoTree')



#---------------------------------------------------------------------------



