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
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightSkyBlue
        self._label1.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlText
        self._label1.Location = System.Drawing.Point(12, 10)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(126, 28)
        self._label1.TabIndex = 0
        self._label1.Text = "Pounds:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightSkyBlue
        self._label2.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlText
        self._label2.Location = System.Drawing.Point(12, 49)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(136, 44)
        self._label2.TabIndex = 1
        self._label2.Text = "Shillings:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightSkyBlue
        self._label3.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlText
        self._label3.Location = System.Drawing.Point(12, 88)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(126, 42)
        self._label3.TabIndex = 2
        self._label3.Text = "Pence:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(126, 11)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(158, 32)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(144, 49)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(158, 32)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(101, 87)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(158, 32)
        self._textBox3.TabIndex = 5
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightCyan
        self._button1.Location = System.Drawing.Point(12, 133)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(163, 68)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PaleTurquoise
        self._button2.Location = System.Drawing.Point(181, 133)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(163, 68)
        self._button2.TabIndex = 7
        self._button2.Text = "Reset"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Turquoise
        self._button3.Location = System.Drawing.Point(350, 133)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(163, 68)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(314, 11)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(222, 37)
        self._label4.TabIndex = 9
        self._label4.Text = "Decimal Pounds:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.SteelBlue
        self._label5.Font = System.Drawing.Font("Mongolian Baiti", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label5.Location = System.Drawing.Point(350, 62)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(136, 44)
        self._label5.TabIndex = 10
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.SteelBlue
        self._label6.Font = System.Drawing.Font("Mongolian Baiti", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label6.Location = System.Drawing.Point(433, 62)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(53, 44)
        self._label6.TabIndex = 11
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightSkyBlue
        self.ClientSize = System.Drawing.Size(548, 223)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "Prog65h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        self._label5.Text = ""
        Pounds = int(self._textBox1.Text)
        Shillings = int(self._textBox2.Text)
        Pence = int(self._textBox3.Text)
        PercentShillings = (Shillings*100 / 20)
        PercentPence = round(Pence*1000 / 240,-1)/10
        Step3 = (PercentShillings+PercentPence)//1
        self._label5.Text += "£" + str(Pounds) + "." + str(Step3) 

    def Button2Click(self, sender, e):
        self._label5.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""

   

    def Button3Click(self, sender, e):
        Application.Exit()