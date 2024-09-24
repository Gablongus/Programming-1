import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._Button1 = System.Windows.Forms.Button()
        self._Button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MintCream
        self._label1.Font = System.Drawing.Font("Microsoft JhengHei", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(333, 93)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(249, 145)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # Button1
        # 
        self._Button1.BackColor = System.Drawing.Color.SpringGreen
        self._Button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._Button1.Location = System.Drawing.Point(124, 325)
        self._Button1.Name = "Button1"
        self._Button1.Size = System.Drawing.Size(138, 61)
        self._Button1.TabIndex = 1
        self._Button1.Text = "Show"
        self._Button1.UseVisualStyleBackColor = False
        self._Button1.Click += self.Button1Click
        # 
        # Button2
        # 
        self._Button2.BackColor = System.Drawing.Color.SpringGreen
        self._Button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._Button2.Location = System.Drawing.Point(393, 325)
        self._Button2.Name = "Button2"
        self._Button2.Size = System.Drawing.Size(138, 61)
        self._Button2.TabIndex = 2
        self._Button2.Text = "Hide"
        self._Button2.UseVisualStyleBackColor = False
        self._Button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.SpringGreen
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(642, 325)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(138, 61)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkSeaGreen
        self.ClientSize = System.Drawing.Size(923, 440)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._Button2)
        self.Controls.Add(self._Button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "My Name"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Gavin Schraedley"
        
    

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        
    
    def Button3Click(self, sender, e):
        Application.Exit()