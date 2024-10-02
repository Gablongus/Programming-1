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
        self._label1.BackColor = System.Drawing.Color.Khaki
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Yu Gothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(545, 30)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(345, 396)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.SandyBrown
        self._button1.Font = System.Drawing.Font("Yu Gothic", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(33, 30)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(99, 69)
        self._button1.TabIndex = 1
        self._button1.Text = "Exit"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.BlanchedAlmond
        self._button2.Font = System.Drawing.Font("Yu Gothic", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(365, 53)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(139, 69)
        self._button2.TabIndex = 2
        self._button2.Text = "Show"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.BlanchedAlmond
        self._button3.Font = System.Drawing.Font("Yu Gothic", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(365, 156)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(139, 69)
        self._button3.TabIndex = 3
        self._button3.Text = "Hide"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Gold
        self.ClientSize = System.Drawing.Size(922, 448)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Phone Numbers"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self._label1.Text = "608-373-4989: Me \n 609-792-3607: Parents \n 608-754-0623: Taco Bell \n 847-252-5700: Obama \n 929-272-9263: Indian Scam Call Center"

    def Button3Click(self, sender, e):
        self._label1.Text = ""
        

    def Button1Click(self, sender, e):
        Application.Exit()