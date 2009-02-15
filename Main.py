from share import *

class MyApp(wx.App):
    def OnInit(self):

        # Check runtime version
        if version.VERSION_STRING != wx.VERSION_STRING:
            wx.MessageBox(caption="Warning",
                          message="You're using version %s of wxPython, but this copy of the demo was written for version %s.\n"
                          "There may be some version incompatibilities..."
                          % (wx.VERSION_STRING, version.VERSION_STRING))

        # Now that we've warned the user about possibile problems,
        # lets import images
        import images as i
        global images
        images = i
        
        # Create and show the splash screen.  It will then create and show
        # the main frame when it is time to do so.
        wx.SystemOptions.SetOptionInt("mac.window-plain-transition", 1)
        self.SetAppName("wxPyDemo")
        
        # For debugging
        #self.SetAssertMode(wx.PYAPP_ASSERT_DIALOG)

        # Normally when using a SplashScreen you would create it, show
        # it and then continue on with the applicaiton's
        # initialization, finally creating and showing the main
        # application window(s).  In this case we have nothing else to
        # do so we'll delay showing the main frame until later (see
        # ShowMain above) so the users can see the SplashScreen effect.        
        splash = MySplashScreen()
        splash.Show()

        return True



#---------------------------------------------------------------------------

def main():
    try:
        demoPath = os.path.dirname(__file__)
        os.chdir(demoPath)
    except:
        pass
    app = MyApp(False)
    app.MainLoop()



#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

if __name__ == '__main__':
    __name__ = 'Main'
    main()

#----------------------------------------------------------------------------







