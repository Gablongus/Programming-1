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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(22, 23)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(113, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "First Name:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(22, 60)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(113, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Last Name:"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(141, 23)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(148, 20)
        self._textBox1.TabIndex = 2
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(141, 60)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(148, 20)
        self._textBox2.TabIndex = 3
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(21, 124)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(113, 23)
        self._label3.TabIndex = 4
        self._label3.Text = "Full Name:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Thistle
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Location = System.Drawing.Point(125, 124)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(216, 23)
        self._label4.TabIndex = 5
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Plum
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(22, 192)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(113, 60)
        self._button1.TabIndex = 6
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Plum
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(141, 192)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(113, 60)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Plum
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(260, 192)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(113, 60)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkOrchid
        self.ClientSize = System.Drawing.Size(396, 275)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg119 Full Name"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        FullName = self._textBox1.Text + " " + self._textBox2.Text
        self._label4.Text = str(FullName)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()