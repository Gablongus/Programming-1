﻿import System.Drawing
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
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
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
        self._label1.BackColor = System.Drawing.Color.CornflowerBlue
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Ebrima", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(400, 321)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Three Test Scores"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.CornflowerBlue
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(83, 82)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(95, 29)
        self._label2.TabIndex = 1
        self._label2.Text = "Score 1:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.CornflowerBlue
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(83, 142)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(95, 29)
        self._label3.TabIndex = 2
        self._label3.Text = "Score 2:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.CornflowerBlue
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Location = System.Drawing.Point(83, 202)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(95, 29)
        self._label4.TabIndex = 3
        self._label4.Text = "Score 3:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(184, 83)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 24)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(184, 142)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 24)
        self._textBox2.TabIndex = 5
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(184, 203)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 24)
        self._textBox3.TabIndex = 6
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.CornflowerBlue
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label5.Location = System.Drawing.Point(83, 275)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(95, 29)
        self._label5.TabIndex = 7
        self._label5.Text = "Average:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.AliceBlue
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlText
        self._label6.Location = System.Drawing.Point(184, 275)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(106, 29)
        self._label6.TabIndex = 8
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSteelBlue
        self._button1.Font = System.Drawing.Font("Ebrima", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(11, 357)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(193, 67)
        self._button1.TabIndex = 9
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSteelBlue
        self._button2.Font = System.Drawing.Font("Ebrima", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(210, 357)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(200, 67)
        self._button2.TabIndex = 10
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightSteelBlue
        self._button3.Font = System.Drawing.Font("Ebrima", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(102, 430)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(200, 67)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label7
        # 
        self._label7.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label7.Location = System.Drawing.Point(127, 331)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(141, 23)
        self._label7.TabIndex = 12
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.RoyalBlue
        self.ClientSize = System.Drawing.Size(429, 499)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg 198 Score Average"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        box1 = int(self._textBox1.Text)
        box2 = int(self._textBox2.Text)
        box3 = int(self._textBox3.Text)
        avg  = round((box3 + box2 + box1)/3,2)
        self._label6.Text = str(avg)
        if avg > 95:
            self._label7.Text = "Congratulations! Great Job!"

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label6.Text   = ""
        self._label7.Text   = ""
        

    def Button3Click(self, sender, e):
        Application.Exit()  