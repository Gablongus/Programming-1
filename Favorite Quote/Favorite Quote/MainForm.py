import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightGreen
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Rockwell", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(280, 110)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(366, 189)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Honeydew
        self._label2.Font = System.Drawing.Font("Palatino Linotype", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(372, 73)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(183, 37)
        self._label2.TabIndex = 1
        self._label2.Text = "My Favorite Quote"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Pink
        self._button1.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(46, 40)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(87, 70)
        self._button1.TabIndex = 2
        self._button1.Text = "Exit"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Lime
        self._button2.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(255, 335)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(143, 70)
        self._button2.TabIndex = 3
        self._button2.Text = "Show"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Lime
        self._button3.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(525, 335)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(143, 70)
        self._button3.TabIndex = 4
        self._button3.Text = "Hide"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Green
        self.ClientSize = System.Drawing.Size(897, 462)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Favorite Quote"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self._label1.Text = "My favorite Quote originates from the hard problem of conciousness Which suggests that The human experience cannot be explained my mechanical proccecess."

    def Button3Click(self, sender, e):
        self._label1.Text = ""
        
    

    def Button1Click(self, sender, e):
        Application.Exit()