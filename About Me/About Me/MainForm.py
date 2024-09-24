import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Thistle
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._label1.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(193, 61)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(514, 228)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DeepPink
        self._button1.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(42, 39)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(70, 62)
        self._button1.TabIndex = 1
        self._button1.Text = "Exit"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Orchid
        self._button2.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(242, 348)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(184, 62)
        self._button2.TabIndex = 2
        self._button2.Text = "Show"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Orchid
        self._button3.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(472, 348)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(184, 62)
        self._button3.TabIndex = 3
        self._button3.Text = "Hide"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Plum
        self.ClientSize = System.Drawing.Size(902, 449)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Cursor = System.Windows.Forms.Cursors.Default
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D
        self.Name = "MainForm"
        self.Text = "About Me"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self._label1.Text = "My Name is Gavin Schraedley. I was born in South Carolina and I moved to eastern Idaho when I was very young, when I was six I moved to Wisconsin. I enjoy coding and building things, anthing that takes effort and has an end result. I have 2 Axolots, which are a type of salamander, and I live with my brother and my parents."

    def Button3Click(self, sender, e):
        self._label1.Text = ""
        
    

    def Button1Click(self, sender, e):
       Application.Exit()