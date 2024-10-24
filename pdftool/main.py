import wx
import PdfToolPanels

app = wx.App()
frame = wx.Frame(None, title='PDF小工具', size=(600, 400))
notebook = wx.Notebook(frame)

notebook.AddPage(PdfToolPanels.Pdf2ImgPanel(notebook), "PDF转图片")
notebook.AddPage(PdfToolPanels.Img2PdfPanel(notebook), "图片合成PDF")
notebook.AddPage(PdfToolPanels.PdfSplit(notebook), "PDF拆分")
notebook.AddPage(PdfToolPanels.PdfMerge(notebook), "PDF合并")


frame.Show()
app.MainLoop()
