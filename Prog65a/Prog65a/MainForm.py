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
        self._label3 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
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
        self._label1.BackColor = System.Drawing.Color.RosyBrown
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("NSimSun", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(119, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(189, 72)
        self._label1.TabIndex = 0
        self._label1.Text = "European Dating App!!"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.MistyRose
        self._label2.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(55, 112)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(326, 40)
        self._label2.TabIndex = 1
        self._label2.Text = "Insert Date:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.White
        self._textBox1.ForeColor = System.Drawing.Color.Black
        self._textBox1.Location = System.Drawing.Point(162, 129)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(55, 20)
        self._textBox1.TabIndex = 2
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(216, 125)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 3
        self._label3.Text = "/"
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.White
        self._textBox2.ForeColor = System.Drawing.Color.Black
        self._textBox2.Location = System.Drawing.Point(236, 128)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(55, 20)
        self._textBox2.TabIndex = 4
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(290, 125)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(27, 23)
        self._label4.TabIndex = 6
        self._label4.Text = "/"
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.White
        self._textBox3.ForeColor = System.Drawing.Color.Black
        self._textBox3.Location = System.Drawing.Point(313, 128)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(55, 20)
        self._textBox3.TabIndex = 7
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("MS Reference Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(166, 113)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(48, 15)
        self._label5.TabIndex = 8
        self._label5.Text = "Month"
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("MS Reference Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(246, 112)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(48, 15)
        self._label6.TabIndex = 9
        self._label6.Text = "Day"
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("MS Reference Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(320, 112)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(48, 15)
        self._label7.TabIndex = 10
        self._label7.Text = "Year"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.MistyRose
        self._label8.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(27, 206)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(326, 40)
        self._label8.TabIndex = 11
        self._label8.Text = "European Date:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(217, 213)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(100, 23)
        self._label9.TabIndex = 12
        self._label9.Text = "/"
        # 
        # label10
        # 
        self._label10.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(236, 219)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(67, 28)
        self._label10.TabIndex = 13
        self._label10.Text = "Month"
        # 
        # label11
        # 
        self._label11.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(172, 217)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(48, 32)
        self._label11.TabIndex = 14
        self._label11.Text = "Day"
        # 
        # label12
        # 
        self._label12.Font = System.Drawing.Font("MS Reference Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(313, 220)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(48, 15)
        self._label12.TabIndex = 15
        self._label12.Text = "Year"
        # 
        # label13
        # 
        self._label13.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(288, 215)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(27, 23)
        self._label13.TabIndex = 16
        self._label13.Text = "/"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Thistle
        self._button1.Font = System.Drawing.Font("Myanmar Text", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(27, 306)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(122, 60)
        self._button1.TabIndex = 17
        self._button1.Text = "Convert"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Thistle
        self._button2.Font = System.Drawing.Font("Myanmar Text", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(155, 306)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(122, 60)
        self._button2.TabIndex = 18
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Thistle
        self._button3.Font = System.Drawing.Font("Myanmar Text", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(283, 306)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(122, 60)
        self._button3.TabIndex = 19
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.MistyRose
        self.ClientSize = System.Drawing.Size(432, 379)
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
        self.Controls.Add(self._label5)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog65a"
        self.ResumeLayout(False)
        self.PerformLayout()

    

    

    def Button1Click(self, sender, e):
        Day = int(self._textBox2.Text)
        Month = int(self._textBox1.Text)
        Year = int(self._textBox3.Text)
        self._label11.Text = str(Day)
        self._label10.Text = str(Month)
        self._label12.Text = str(Year)

   

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label11.Text = "Day"
        self._label10.Text = "Month"
        self._label12.Text = "Year"

    def Button3Click(self, sender, e):
        Application.Exit()