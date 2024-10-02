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
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(46, 60)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(156, 40)
        self._label1.TabIndex = 0
        self._label1.Text = "Number 1:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.BlueViolet
        self._label2.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Location = System.Drawing.Point(46, 110)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(156, 40)
        self._label2.TabIndex = 1
        self._label2.Text = "Number 2:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.BlueViolet
        self._label3.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label3.Location = System.Drawing.Point(46, 223)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(156, 40)
        self._label3.TabIndex = 3
        self._label3.Text = "Number 4:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Location = System.Drawing.Point(46, 166)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(156, 40)
        self._label4.TabIndex = 2
        self._label4.Text = "Number 3:"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(208, 60)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(134, 20)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(208, 110)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(134, 20)
        self._textBox2.TabIndex = 5
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(208, 166)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(134, 20)
        self._textBox3.TabIndex = 6
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(208, 223)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(134, 20)
        self._textBox4.TabIndex = 7
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Tai Le", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Location = System.Drawing.Point(373, 75)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(156, 40)
        self._label5.TabIndex = 8
        self._label5.Text = "Sum:"
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Tai Le", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label6.Location = System.Drawing.Point(373, 176)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(156, 40)
        self._label6.TabIndex = 9
        self._label6.Text = "Avg:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Thistle
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label7.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(482, 76)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(171, 39)
        self._label7.TabIndex = 10
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Thistle
        self._label8.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label8.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(482, 177)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(171, 39)
        self._label8.TabIndex = 11
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MediumPurple
        self._button1.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Beige
        self._button1.Location = System.Drawing.Point(72, 304)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(163, 56)
        self._button1.TabIndex = 12
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MediumPurple
        self._button2.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Beige
        self._button2.Location = System.Drawing.Point(287, 304)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(163, 56)
        self._button2.TabIndex = 13
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MediumPurple
        self._button3.Font = System.Drawing.Font("MS Reference Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Beige
        self._button3.Location = System.Drawing.Point(490, 304)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(163, 56)
        self._button3.TabIndex = 14
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.BlueViolet
        self.ClientSize = System.Drawing.Size(736, 395)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog54b"
        self.ResumeLayout(False)
        self.PerformLayout()


   

    

 

    def Button1Click(self, sender, e):
        Numone = int(self._textBox1.Text)
        Numtwo = int(self._textBox2.Text)
        Numthree = int(self._textBox3.Text)
        Numfour = int(self._textBox4.Text)
        Sum = Numone + Numtwo + Numthree + Numfour
        Avg = Sum/4.0
        self._label7.Text = str(Sum)
        self._label8.Text = str(Avg)
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()