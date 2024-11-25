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
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("MV Boli", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(30, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(264, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Number of Calories in food:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("MV Boli", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(12, 52)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(289, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter Number of Fat Grams in food:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("MV Boli", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(110, 110)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(264, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "Percentage of Calories from Fat"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightBlue
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlText
        self._label4.Location = System.Drawing.Point(194, 142)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 3
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(301, 9)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(301, 52)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 5
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PowderBlue
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(42, 226)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(86, 48)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PowderBlue
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(194, 226)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(86, 48)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.PowderBlue
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(329, 226)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(86, 48)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DeepSkyBlue
        self.ClientSize = System.Drawing.Size(475, 298)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg 268 Fat Calc"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        fatgrams = float(self._textBox2.Text)
        calories = float(self._textBox1.Text)
        caloriesfromfat = fatgrams * 9
        percent = float(caloriesfromfat/calories)
        
        self._label4.Text  = str(float(percent * 100)) + "%"

    def Button2Click(self, sender, e):
        self._textBox1.Text  = ""
        self._textBox2.Text  = ""
        self._label4.Text  = ""

    def Button3Click(self, sender, e):
        Application.Exit()