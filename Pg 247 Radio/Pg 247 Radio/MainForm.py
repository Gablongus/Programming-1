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
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightCyan
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(155, 168)
        self._label1.TabIndex = 0
        self._label1.Text = "Radio Buttons"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightCyan
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(173, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(155, 168)
        self._label2.TabIndex = 1
        self._label2.Text = "Check Boxes"
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.LightCyan
        self._radioButton1.Font = System.Drawing.Font("Microsoft YaHei UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(24, 36)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(104, 24)
        self._radioButton1.TabIndex = 2
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Choice 1"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.LightCyan
        self._radioButton2.Font = System.Drawing.Font("Microsoft YaHei UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(24, 80)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(104, 24)
        self._radioButton2.TabIndex = 3
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Choice 2"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.LightCyan
        self._radioButton3.Font = System.Drawing.Font("Microsoft YaHei UI", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(24, 129)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(104, 24)
        self._radioButton3.TabIndex = 4
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Choice 3"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # checkBox1
        # 
        self._checkBox1.BackColor = System.Drawing.Color.LightCyan
        self._checkBox1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(191, 35)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(104, 24)
        self._checkBox1.TabIndex = 5
        self._checkBox1.Text = "Choice 4"
        self._checkBox1.UseVisualStyleBackColor = False
        # 
        # checkBox2
        # 
        self._checkBox2.BackColor = System.Drawing.Color.LightCyan
        self._checkBox2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(191, 80)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(104, 24)
        self._checkBox2.TabIndex = 6
        self._checkBox2.Text = "Choice 5"
        self._checkBox2.UseVisualStyleBackColor = False
        # 
        # checkBox3
        # 
        self._checkBox3.BackColor = System.Drawing.Color.LightCyan
        self._checkBox3.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(191, 130)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(104, 24)
        self._checkBox3.TabIndex = 7
        self._checkBox3.Text = "Choice 6"
        self._checkBox3.UseVisualStyleBackColor = False
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightCyan
        self._button1.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(63, 191)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(84, 40)
        self._button1.TabIndex = 8
        self._button1.Text = "Ok"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightCyan
        self._button2.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(191, 191)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(84, 40)
        self._button2.TabIndex = 9
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.PaleTurquoise
        self.ClientSize = System.Drawing.Size(339, 242)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._checkBox3)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg 247 Radio"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        
        Message = ""
        
        if self._radioButton1.Checked == True:
            Message = "You selected choice 1"
        if self._radioButton2.Checked == True:
            Message = "You selected choice 2"
        if self._radioButton3.Checked == True:
            Message = "You selected choice 3"
            
        if self._checkBox1.Checked == True:
            Message += " and choice 4"
        if self._checkBox2.Checked == True:
            Message += " and choice 5"
        if self._checkBox3.Checked == True:
            Message += " and choice 6"
            
        MessageBox.Show(Message + ".")

    def Button2Click(self, sender, e):
        Application.Exit()