import math
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
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(38, 46)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "A:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(38, 83)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "B:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(38, 119)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "C:"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(89, 49)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(89, 85)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(89, 119)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 20)
        self._textBox3.TabIndex = 5
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(38, 49)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(8, 8)
        self._label4.TabIndex = 6
        self._label4.Text = "label4"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("MS Gothic", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label5.Location = System.Drawing.Point(271, 92)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(132, 50)
        self._label5.TabIndex = 7
        self._label5.Text = "Roots:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.ForestGreen
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label6.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label6.Location = System.Drawing.Point(396, 67)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(154, 38)
        self._label6.TabIndex = 8
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PaleGreen
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(38, 195)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(148, 58)
        self._button1.TabIndex = 9
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Lime
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(243, 195)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(148, 58)
        self._button2.TabIndex = 10
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MediumSpringGreen
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(443, 195)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(148, 58)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.ForestGreen
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label7.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label7.Location = System.Drawing.Point(396, 119)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(154, 38)
        self._label7.TabIndex = 12
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkGreen
        self.ClientSize = System.Drawing.Size(656, 288)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog58b"
        self.ResumeLayout(False)
        self.PerformLayout()


   

    def Button1Click(self, sender, e):
        A = int(self._textBox1.Text)
        B = int(self._textBox2.Text)
        C = int(self._textBox3.Text)
        Step1R1 = -B+math.sqrt(B*B-4*A*C)
        Step2R1 = Step1R1/2*A
        Step1R2 = -B-math.sqrt(B*B-4*A*C)
        Step2R2 = Step1R2/2*A        
        self._label6.Text = str(Step2R1)
        self._label7.Text = str(Step2R2)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()