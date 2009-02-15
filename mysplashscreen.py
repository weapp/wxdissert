from share import *
class MySplashScreen(wx.SplashScreen):
    def __init__(self):
        bmp = wx.Image(opj("bitmaps/splash.png")).ConvertToBitmap()
        wx.SplashScreen.__init__(self, bmp,
                                 wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,
                                 5000, None, -1)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.fc = wx.FutureCall(2000, self.ShowMain)


    def OnClose(self, evt):
        # Make sure the default handler runs too so this window gets
        # destroyed
        evt.Skip()
        self.Hide()
        
        # if the timer is still running then go ahead and show the
        # main frame now
        if self.fc.IsRunning():
            self.fc.Stop()
            self.ShowMain()


    def ShowMain(self):
        frame = wxPythonDemo(None, "wxPython: (A Demonstration)")
        frame.Show()
        if self.fc.IsRunning():
            self.Raise()
        wx.CallAfter(frame.ShowTip)

