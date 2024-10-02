import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Lucida Sans Typewriter", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(56, 61)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(128, 34)
        self._label1.TabIndex = 0
        self._label1.Text = "Radius:"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(34, 98)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(150, 20)
        self._textBox1.TabIndex = 1
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MidnightBlue
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(49, 146)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(121, 57)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.RoyalBlue
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(49, 237)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(121, 57)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightSkyBlue
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(49, 329)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(121, 57)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Lucida Sans Typewriter", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Location = System.Drawing.Point(271, 71)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(104, 34)
        self._label2.TabIndex = 5
        self._label2.Text = "Area:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Azure
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Microsoft YaHei UI", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(358, 71)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(181, 34)
        self._label3.TabIndex = 6
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Azure
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Microsoft YaHei UI", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(471, 132)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(181, 34)
        self._label4.TabIndex = 8
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Lucida Sans Typewriter", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Location = System.Drawing.Point(271, 134)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(222, 34)
        self._label5.TabIndex = 7
        self._label5.Text = "Circumfrence:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SlateGray
        self.ClientSize = System.Drawing.Size(713, 455)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog54c"
        self.ResumeLayout(False)
        self.PerformLayout()


   

    def Button1Click(self, sender, e):
        Radius = float(self._textBox1.Text)
        PI = 3.14159
        Circumfrence = 2 * PI * Radius
        Area = Radius * Radius * PI
        self._label3.Text = str(round(Area,3))
        self._label4.Text = str(round(Circumfrence,3))        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()