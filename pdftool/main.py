import wx
# from pdf2imgpanel import Pdf2ImgPanel
from PdfToolPanels import Pdf2ImgPanel, Img2PdfPanel

app = wx.App()
frame = wx.Frame(None, title='PDF小工具', size=(600, 400))
notebook = wx.Notebook(frame)

notebook.AddPage(Pdf2ImgPanel(notebook), "PDF转图片")
notebook.AddPage(Img2PdfPanel(notebook), "图片合成PDF")

frame.Show()
app.MainLoop()
