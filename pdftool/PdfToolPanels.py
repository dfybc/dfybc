# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import gettext
import os

import wx
import wx.xrc
from pdf2image import convert_from_path
import img2pdf

_ = gettext.gettext

NOT_CHOOSE_FILE_STR = '还未选择文件'
CONVERT_SUCCESS_STR = '转换成功'

###########################################################################
## Class Pdf2ImgPanel
###########################################################################

class Pdf2ImgPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.input_dir = ''
        self.input_file_path = ''
        self.output_dir = ''
        self.lbltxt_show_input_file_path = NOT_CHOOSE_FILE_STR
        self.result = ''

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
        dlg = wx.FileDialog(self, "选择文件", self.input_dir, "", "*.pdf;*.PDF", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.input_file_path = dlg.GetPath()    # 获取文件完整路径
            self.input_dir = dlg.GetDirectory()    # 获取文件目录
            if self.output_dir == '':
                self.output_dir = self.input_dir
                print(self.output_dir)
            self.lbltxt_show_input_file_path = '已选择文件：' + self.input_file_path
            self.result = ''
            self.update()
        dlg.Destroy()

    def chg_output_dir( self, event ):
        dlg = wx.DirDialog(self, "选择图片输出目录", self.output_dir, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.output_dir = dlg.GetPath()
            print(self.output_dir)
            self.update()
        dlg.Destroy()

    def convert( self, event ):
        if self.input_file_path:
            try:
                images = convert_from_path(self.input_file_path, dpi=200,
                                        first_page=None, last_page=None)
                for i, image in enumerate(images):
                    # 将图片保存到指定目录
                    image.save('{}/page_{}.png'.format(self.output_dir, i), 'PNG')
                self.str_lbl_input_file_path = NOT_CHOOSE_FILE_STR
                self.result = CONVERT_SUCCESS_STR
            except Exception as e:
                self.result = '转换失败:' + str(e)
        else:
            self.result = '请先选择要转换的文件'
        self.update()

    def update(self):
        self.lbl_show_choose_file.SetLabel(self.lbltxt_show_input_file_path)
        self.textctl_outputdir.SetValue(self.output_dir)
        if self.result == CONVERT_SUCCESS_STR:
            self.textcrl_result.SetValue(self.result)
            self.textcrl_result.SetForegroundColour('blue')
        else:
            self.textcrl_result.SetValue(self.result)
            self.textcrl_result.SetForegroundColour('red')
###########################################################################
## Class Img2PdfPanel
###########################################################################

class Img2PdfPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.input_dir = os.getcwd()
        self.result = ''
        self.img_suffixs = ['.jpg', '.png', '.bmp', '.jpeg']
        self.sort_key = '文件名'
        self.sort_type = '升序'

        vbox = wx.BoxSizer( wx.VERTICAL )

        hbox1 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl1 = wx.StaticText( self, wx.ID_ANY, _(u"图片输入目录"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl1.Wrap( -1 )

        hbox1.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.textctl_input_dir = wx.TextCtrl( self, wx.ID_ANY, self.input_dir, wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox1.Add( self.textctl_input_dir, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btn_chdir = wx.Button( self, wx.ID_ANY, _(u"点击切换\n图片输入目录"), wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox1.Add( self.btn_chdir, 0, wx.ALL, 5 )


        vbox.Add( hbox1, 0, wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"图片按照"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer8.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        combo_sort_keyChoices = [ _(u"文件名"), _(u"文件修改时间") ]
        self.combo_sort_key = wx.ComboBox( self, wx.ID_ANY, _(u"文件名"), wx.DefaultPosition, wx.DefaultSize, combo_sort_keyChoices, wx.CB_READONLY )
        self.combo_sort_key.SetSelection( 0 )
        bSizer8.Add( self.combo_sort_key, 0, wx.ALL, 5 )

        combo_sort_typeChoices = [ _(u"升序"), _(u"降序") ]
        self.combo_sort_type = wx.ComboBox( self, wx.ID_ANY, _(u"升序"), wx.DefaultPosition, wx.DefaultSize, combo_sort_typeChoices, wx.CB_READONLY )
        self.combo_sort_type.SetSelection( 0 )
        bSizer8.Add( self.combo_sort_type, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"排序"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer8.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        vbox.Add( bSizer8, 0, wx.EXPAND, 5 )

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
        self.combo_sort_key.Bind( wx.EVT_COMBOBOX, self.set_sort_key )
        self.combo_sort_type.Bind( wx.EVT_COMBOBOX, self.set_sort_type )
        self.btn_merge.Bind( wx.EVT_BUTTON, self.merge_pdf )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def chg_input_dir( self, event ):
        dlg = wx.DirDialog(self, "选择图片输出目录", self.input_dir, style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.input_dir = dlg.GetPath()
            print(self.input_dir)
            self.update()
        dlg.Destroy()
		
    def set_sort_key( self, event ):
        print('set_sort_key:', event.GetString())
        self.sort_key = event.GetString()

    def set_sort_type( self, event ):
        print('set_sort_type:', event.GetString())
        self.sort_type = event.GetString()

    def merge_pdf( self, event ):
        try:
            image_files = []
            for file in os.listdir(self.input_dir):
                if os.path.isfile(os.path.join(self.input_dir, file)) and os.path.splitext(file)[1].lower() in self.img_suffixs:
                    image_files.append(os.path.join(self.input_dir, file))
            
            image_files.sort(key=lambda x: os.path.getmtime(x) if self.sort_key == _(u"文件修改时间") else x,
                             reverse=True if self.sort_type == _(u"降序") else False)
            if len(image_files) == 0:
                raise Exception('目录下没有图片文件！')

            output_pdf_path = os.path.join(os.path.dirname(self.input_dir), "output.pdf")

            with open(output_pdf_path, "wb") as f:
                f.write(img2pdf.convert(image_files))
            self.result = 'PDF合成成功,pdf 路径：' + output_pdf_path
        except Exception as e:
            self.result = 'PDF合成失败：' + str(e)
        self.update()

    def update(self):
        self.textctl_input_dir.SetValue(self.input_dir)
        if self.result.find('成功') > -1:
            self.textctl_result.SetValue(self.result)
            self.textctl_result.SetForegroundColour('blue')
        else:
            self.textctl_result.SetValue(self.result)
            self.textctl_result.SetForegroundColour('red')
