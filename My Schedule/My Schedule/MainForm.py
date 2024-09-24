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
        self._label1.BackColor = System.Drawing.Color.LightCyan
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(146, 21)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(375, 394)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PowderBlue
        self._button1.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._button1.Location = System.Drawing.Point(4, 95)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(136, 68)
        self._button1.TabIndex = 1
        self._button1.Text = "Show Schedule"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PowderBlue
        self._button2.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._button2.Location = System.Drawing.Point(4, 169)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(136, 70)
        self._button2.TabIndex = 2
        self._button2.Text = "Hide Schedule"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightCoral
        self._button3.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._button3.Location = System.Drawing.Point(31, 21)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(81, 68)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit Program"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightBlue
        self.ClientSize = System.Drawing.Size(550, 434)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "My Schedule"
        self.ResumeLayout(False)


    

    def Button1Click(self, sender, e):
        self._label1.Text = "1st Hour: Engineering and Tech \n 2nd Hour: Choir \n 3rd Hour: Algebra \n 4th Hour: Social Studies \n 5th Hour: ELA \n 6th Hour: Flex \n 7th Hour: Coding  "

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label1.Text = ""

   

    