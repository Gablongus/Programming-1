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
        self._label2 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.PaleTurquoise
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Sitka Small", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(264, 77)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(379, 230)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Pink
        self._button1.Font = System.Drawing.Font("Perpetua", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(55, 49)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(80, 76)
        self._button1.TabIndex = 1
        self._button1.Text = "Exit"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.SkyBlue
        self._button2.Font = System.Drawing.Font("Perpetua", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(264, 340)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(165, 76)
        self._button2.TabIndex = 2
        self._button2.Text = "Show"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Azure
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(379, 49)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(157, 23)
        self._label2.TabIndex = 3
        self._label2.Text = "My Favorite Activity"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.SkyBlue
        self._button3.Font = System.Drawing.Font("Perpetua", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(478, 340)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(165, 76)
        self._button3.TabIndex = 4
        self._button3.Text = "Hide"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkTurquoise
        self.ClientSize = System.Drawing.Size(888, 460)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Favorite Activity"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self._label1.Text = " My Favorite sport or activity is swimming, but I also enjoy martial arts and singing, and I do lessons for both."

    def Button3Click(self, sender, e):
        self._label1.Text = ""
        
    

    def Button1Click(self, sender, e):
        Application.Exit()