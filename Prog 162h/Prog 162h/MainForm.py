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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(230, 40)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter # of Guests"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(267, 13)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(230, 40)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter # of Seats"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(161, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 2
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(416, 13)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 3
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightCyan
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 37)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(131, 50)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightCyan
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(194, 37)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(131, 50)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightCyan
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(382, 39)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(131, 50)
        self._button3.TabIndex = 6
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 111)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(230, 40)
        self._label3.TabIndex = 7
        self._label3.Text = "Possible Arrangements:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 163)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(230, 40)
        self._label4.TabIndex = 8
        self._label4.Text = "Guests Standing:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightCyan
        self._label5.Font = System.Drawing.Font("Microsoft YaHei UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(212, 102)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(150, 36)
        self._label5.TabIndex = 9
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightCyan
        self._label6.Font = System.Drawing.Font("Microsoft YaHei UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(161, 154)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(150, 36)
        self._label6.TabIndex = 10
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightSkyBlue
        self.ClientSize = System.Drawing.Size(525, 204)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog 162h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        Guests = int(self._textBox1.Text)
        Seats  = int(self._textBox2.Text)
        Total = Guests
        for num in range(0, 4):
            Total = Total + Guests * (Guests - 1)
            Guests = (Guests - 1)
            Seats = Seats - 1
        self._label5.Text = str(6*5*4*3)    
        self._label6.Text = str(Guests-Seats)
        

    def Button2Click(self, sender, e):
        self._label5.Text = ""    
        self._label6.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text + ""

    def Button3Click(self, sender, e):
        Application.Exit()