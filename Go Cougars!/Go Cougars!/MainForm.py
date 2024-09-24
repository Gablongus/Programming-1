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
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Azure
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Times New Roman", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(198, 103)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(324, 152)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PaleTurquoise
        self._button1.Font = System.Drawing.Font("Microsoft Tai Le", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(198, 307)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(121, 52)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PaleTurquoise
        self._button2.Font = System.Drawing.Font("Microsoft Tai Le", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(401, 307)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(121, 52)
        self._button2.TabIndex = 2
        self._button2.Text = "Hide"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Thistle
        self._button3.Font = System.Drawing.Font("Microsoft Tai Le", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(34, 36)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(102, 52)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Azure
        self._label2.Font = System.Drawing.Font("Nirmala UI", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(275, 225)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(157, 23)
        self._label2.TabIndex = 4
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Cyan
        self.ClientSize = System.Drawing.Size(719, 421)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Go Cougars!"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Go Cougars!!!"
        self._label2.Text = "I dont even go to Craig (yet)"

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

   