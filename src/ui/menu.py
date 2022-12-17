import wx


class menu(wx.Frame):
    def __init__(self, parent, title): 
      super(menu, self).__init__(parent, title = title,size = (700,600))

      panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      
      hbox2 = wx.BoxSizer(wx.HORIZONTAL)
      l2 = wx.StaticText(panel, -1, "Sample Rate") 
		
      hbox2.Add(l2, 1, wx.ALIGN_LEFT|wx.ALL,5) 
      self.t2 = wx.TextCtrl(panel) 
      self.t2.SetMaxLength(16) 
		
      hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      vbox.Add(hbox2)

