from ui import menu
import wx



class runner():
   def __init__(self):
      self.app = wx.App()
      self.frame = menu.menu(None, "File2Wav")   
         
      self.frame.Show()
      self.app.MainLoop()

if __name__ == "__main__":
   runner()