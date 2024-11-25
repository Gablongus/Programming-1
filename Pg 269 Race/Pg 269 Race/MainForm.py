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
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft YaHei UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 88)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(106, 55)
        self._label1.TabIndex = 0
        self._label1.Text = "Runner 1:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft YaHei UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 111)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(106, 55)
        self._label2.TabIndex = 1
        self._label2.Text = "Runner 2:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft YaHei UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(13, 134)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(106, 55)
        self._label3.TabIndex = 2
        self._label3.Text = "Runner 3:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(13, 2)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(251, 58)
        self._label4.TabIndex = 3
        self._label4.Text = "Enter the three runners' names and finishing times."
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(97, 89)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(84, 20)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(97, 112)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(84, 20)
        self._textBox2.TabIndex = 5
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(97, 134)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(84, 20)
        self._textBox3.TabIndex = 6
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft YaHei UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(105, 60)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(76, 28)
        self._label5.TabIndex = 7
        self._label5.Text = "Name:"
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(200, 133)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(51, 20)
        self._textBox4.TabIndex = 10
        # 
        # textBox5
        # 
        self._textBox5.Location = System.Drawing.Point(200, 111)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(51, 20)
        self._textBox5.TabIndex = 9
        # 
        # textBox6
        # 
        self._textBox6.Location = System.Drawing.Point(200, 88)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(51, 20)
        self._textBox6.TabIndex = 8
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft YaHei UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(200, 60)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(76, 28)
        self._label6.TabIndex = 11
        self._label6.Text = "Time:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.LightGoldenrodYellow
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label7.Font = System.Drawing.Font("Microsoft YaHei UI", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(25, 189)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(233, 127)
        self._label7.TabIndex = 12
        self._label7.Text = "Results:"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.LightGoldenrodYellow
        self._label8.Location = System.Drawing.Point(50, 287)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(69, 23)
        self._label8.TabIndex = 13
        self._label8.Text = "1st Place:"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.LightGoldenrodYellow
        self._label9.Location = System.Drawing.Point(49, 263)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(69, 23)
        self._label9.TabIndex = 14
        self._label9.Text = "2nd Place:"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.LightGoldenrodYellow
        self._label10.Location = System.Drawing.Point(50, 230)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(69, 23)
        self._label10.TabIndex = 15
        self._label10.Text = "3rd Place:"
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.SystemColors.Window
        self._label11.Location = System.Drawing.Point(105, 230)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(117, 23)
        self._label11.TabIndex = 16
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.SystemColors.Window
        self._label12.Location = System.Drawing.Point(105, 258)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(117, 23)
        self._label12.TabIndex = 17
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.SystemColors.Window
        self._label13.Location = System.Drawing.Point(105, 287)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(117, 23)
        self._label13.TabIndex = 18
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Gold
        self._button1.Location = System.Drawing.Point(25, 335)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(70, 55)
        self._button1.TabIndex = 19
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Gold
        self._button2.Location = System.Drawing.Point(111, 335)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(70, 55)
        self._button2.TabIndex = 20
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Gold
        self._button3.Location = System.Drawing.Point(194, 335)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(70, 55)
        self._button3.TabIndex = 21
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Yellow
        self.ClientSize = System.Drawing.Size(282, 404)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg 269 Race"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        Run1name = str(self._textBox1.Text)
        Run1time = str(self._textBox6.Text)
        Run2name = str(self._textBox2.Text)
        Run2time = str(self._textBox5.Text)
        Run3name = str(self._textBox3.Text)
        Run3time = str(self._textBox4.Text)
        
        if Run1time > Run2time and Run1time> Run3time:
            self._label11.Text = str(Run1name)
            if Run2time > Run3time:
                self._label12.Text = str(Run2name)
                self._label13.Text = str(Run3name)
            else:
                self._label13.Text = str(Run2name)
                self._label12.Text = str(Run3name)
        
        elif Run2time > Run1time and Run2time> Run3time:
            self._label11.Text = str(Run2name)
            if Run1time > Run3time:
                self._label12.Text = str(Run1name)
                self._label13.Text = str(Run3name)
            else:
                self._label13.Text = str(Run1name)
                self._label12.Text = str(Run3name)
        elif Run3time > Run2time and Run3time> Run1time:
            self._label11.Text = str(Run3name)
            if Run1time > Run2time:
                self._label12.Text = str(Run1name)
                self._label13.Text = str(Run2name)
            else:
                self._label13.Text = str(Run1name)
                self._label12.Text = str(Run2name)
        
