#encoding: utf-8

import wx
import os
import webbrowser


class PathManager(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent)
		self.rchbtn=wx.Button(self)
		self.rchbtn.SetLabel(u'科研')
		self.rchbtn.Bind(wx.EVT_BUTTON,self.Research)
		self.QQfile=wx.Button(self,label=u'QQ文件')
		self.QQfile.Bind(wx.EVT_BUTTON,self.QQfilesopen)
		
		self.hbox=wx.BoxSizer(wx.HORIZONTAL)
		self.hbox.Add(self.rchbtn,proportion=0,flag=wx.Left,border=5)
		self.hbox.Add(self.QQfile,proportion=0,flag=wx.Left,border=5)
		self.SetSizer(self.hbox)
	
	def Research(self,event):
		path=u'E:\\文档论文'
		os.system('start '+path.encode('gbk'))

	def QQfilesopen(self,event):
		path=u'F:\\QQ文件\\763405111\\FileRecv'
		os.system('start '+path.encode('gbk'))

class webmanager(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent)
		self.webbtn=wx.Button(self,label='redmine')
		self.webbtn.Bind(wx.EVT_BUTTON,self.redmine_click)
		
	def redmine_click(self,event):
		rurl=r'http://114.214.170.122:8006/redmine/'
		webbrowser.open_new_tab(rurl)

def load(event):
	filepath=r'./txt/'+filename.GetValue()
	file=open(filepath)
	contents.SetValue(file.read())
	file.close()

def save(event):
	filepath=r'./txt/'+filename.GetValue()
	file=open(filepath,'w')
	file.write(contents.GetValue().encode('gbk'))
	file.close()
    
app=wx.App()

win=wx.Frame(None,size=(410,355))
win.SetTitle("tomatoes")
mynotebook=wx.Notebook(win,id=-1)

bkg=wx.Panel(mynotebook)
MyPathManager=PathManager(mynotebook)
wm=webmanager(mynotebook)
mynotebook.AddPage(bkg,'Plans')
mynotebook.AddPage(MyPathManager,'PathManager')
mynotebook.AddPage(wm,'WebManager')

btn1=wx.Button(bkg)
btn2=wx.Button(bkg)
btn1.SetLabel("open")
btn2.SetLabel("save")
btn1.Bind(wx.EVT_BUTTON,load)
btn2.Bind(wx.EVT_BUTTON,save)

filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE |wx.HSCROLL)

hbox=wx.BoxSizer(wx.HORIZONTAL)
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(btn1,proportion=0,flag=wx.Left,border=5)
hbox.Add(btn2,proportion=0,flag=wx.Left,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,
        border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()