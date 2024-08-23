# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class Pdf2ImgPanel
###########################################################################

class Pdf2ImgPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        vbox = wx.BoxSizer( wx.VERTICAL )

        hbox1 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn_choosefile = wx.Button( self, wx.ID_ANY, _(u"点击选择文件"), wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox1.Add( self.btn_choosefile, 0, wx.ALL, 5 )

        self.lbl_show_choose_file = wx.StaticText( self, wx.ID_ANY, _(u"还未选择文件"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_show_choose_file.Wrap( -1 )

        hbox1.Add( self.lbl_show_choose_file, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        vbox.Add( hbox1, 0, wx.EXPAND, 5 )

        hbox2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"图片输出目录："), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        hbox2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.textctl_outputdir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox2.Add( self.textctl_outputdir, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.btn_chdir = wx.Button( self, wx.ID_ANY, _(u"点击切换\n图片输出目录"), wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox2.Add( self.btn_chdir, 0, wx.ALL, 5 )


        vbox.Add( hbox2, 0, wx.EXPAND, 5 )

        hbox3 = wx.BoxSizer( wx.VERTICAL )

        self.btn_convert = wx.Button( self, wx.ID_ANY, _(u"开始转换"), wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox3.Add( self.btn_convert, 0, wx.ALL, 5 )

        self.textcrl_result = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.BORDER_NONE )
        hbox3.Add( self.textcrl_result, 1, wx.ALL|wx.EXPAND, 5 )


        vbox.Add( hbox3, 0, wx.EXPAND, 5 )


        self.SetSizer( vbox )
        self.Layout()

        # Connect Events
        self.btn_choosefile.Bind( wx.EVT_BUTTON, self.choose_file )
        self.btn_chdir.Bind( wx.EVT_BUTTON, self.chg_output_dir )
        self.btn_convert.Bind( wx.EVT_BUTTON, self.convert )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def choose_file( self, event ):
        event.Skip()

    def chg_output_dir( self, event ):
        event.Skip()

    def convert( self, event ):
        event.Skip()


###########################################################################
## Class Img2PdfPanel
###########################################################################

class Img2PdfPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        vbox = wx.BoxSizer( wx.VERTICAL )

        hbox1 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl1 = wx.StaticText( self, wx.ID_ANY, _(u"图片输入目录"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl1.Wrap( -1 )

        hbox1.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.textctl_input_dir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox1.Add( self.textctl_input_dir, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btn_chdir = wx.Button( self, wx.ID_ANY, _(u"点击切换\n图片输入目录"), wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox1.Add( self.btn_chdir, 0, wx.ALL, 5 )


        vbox.Add( hbox1, 0, wx.EXPAND, 5 )

        hbox2 = wx.BoxSizer( wx.VERTICAL )

        self.btn_merge = wx.Button( self, wx.ID_ANY, _(u"开始合成PDF"), wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox2.Add( self.btn_merge, 0, wx.ALL, 5 )

        self.textctl_result = wx.TextCtrl( self, wx.ID_ANY, _(u"合成结果"), wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.BORDER_NONE )
        hbox2.Add( self.textctl_result, 1, wx.ALL|wx.EXPAND, 5 )


        vbox.Add( hbox2, 0, wx.EXPAND, 5 )


        self.SetSizer( vbox )
        self.Layout()

        # Connect Events
        self.btn_chdir.Bind( wx.EVT_BUTTON, self.chg_input_dir )
        self.btn_merge.Bind( wx.EVT_BUTTON, self.merge_pdf )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def chg_input_dir( self, event ):
        event.Skip()

    def merge_pdf( self, event ):
        event.Skip()


