import wx
from PdfToolPanels import Pdf2ImgPanel, Img2PdfPanel, PdfSplit

app = wx.App()
frame = wx.Frame(None, title='PDF小工具', size=(600, 400))
notebook = wx.Notebook(frame)

notebook.AddPage(Pdf2ImgPanel(notebook), "PDF转图片")
notebook.AddPage(Img2PdfPanel(notebook), "图片合成PDF")
notebook.AddPage(PdfSplit(notebook), "PDF拆分")

frame.Show()
app.MainLoop()
