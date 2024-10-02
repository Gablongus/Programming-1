import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(27, 34)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(300, 41)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Speed Limit:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(193, 45)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(123, 20)
        self._textBox1.TabIndex = 1
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(203, 98)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(112, 20)
        self._textBox2.TabIndex = 3
        self._textBox2.TextChanged += self.TextBox2TextChanged
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(27, 87)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(300, 41)
        self._label2.TabIndex = 2
        self._label2.Text = "Enter Vehicle Speed:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ControlLight
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Myanmar Text", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlDarkDark
        self._label3.Location = System.Drawing.Point(360, 34)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(219, 256)
        self._label3.TabIndex = 4
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Location = System.Drawing.Point(360, 45)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(219, 23)
        self._label4.TabIndex = 5
        self._label4.Text = "Ticket:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.Highlight
        self._button1.Font = System.Drawing.Font("Nirmala UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(27, 155)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(300, 57)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate Ticket"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button2.Font = System.Drawing.Font("Nirmala UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(27, 233)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(136, 57)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button3.Font = System.Drawing.Font("Nirmala UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(191, 233)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(136, 57)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ControlLight
        self._label5.Font = System.Drawing.Font("Myanmar Text", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlDarkDark
        self._label5.Location = System.Drawing.Point(379, 98)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(182, 27)
        self._label5.TabIndex = 9
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ControlLight
        self._label6.Font = System.Drawing.Font("Myanmar Text", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlDarkDark
        self._label6.Location = System.Drawing.Point(379, 134)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(182, 27)
        self._label6.TabIndex = 10
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.ControlLight
        self._label7.Font = System.Drawing.Font("Myanmar Text", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ControlDarkDark
        self._label7.Location = System.Drawing.Point(379, 201)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(182, 64)
        self._label7.TabIndex = 11
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonFace
        self.ClientSize = System.Drawing.Size(591, 320)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog82a"
        self.ResumeLayout(False)
        self.PerformLayout()


  

    def Button1Click(self, sender, e):
        Limit = int(self._textBox1.Text)
        Speed = int(self._textBox2.Text)
        AmountOver = int(Speed - Limit)
        Ticket = int(20.00 + AmountOver*5.00)
        self._label7.Text = "Fine------$" + str(float(Ticket))
 

    def TextBox1TextChanged(self, sender, e):
        self._label5.Text = "Speed Limit: " + str(self._textBox1.Text)

    def TextBox2TextChanged(self, sender, e):
        self._label6.Text = "Vehicle Speed: " + str(self._textBox2.Text)