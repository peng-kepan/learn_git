import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title="第一个Python程序！",size=(400,300),pos=(100,100))
        panel = wx.Panel(parent=self)
        #statictext = wx.StaticText(parent=panel,label='Hello World!',pos=(10,10))
        self.statictext=wx.StaticText(parent=panel,label="请单击OK按钮",pos=(110,20))
        b=wx.Button(parent=panel,label='OK',pos=(100,50))
        self.Bind(wx.EVT_BUTTON,self.on_click,b)

    def on_click(self,event):
        self.statictext.SetLabelText("Hello World!")

app = wx.App()
frm = MyFrame()
frm.Show()

app.MainLoop()
