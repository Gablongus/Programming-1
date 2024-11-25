import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._listBox1 = System.Windows.Forms.ListBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label1.Font = System.Drawing.Font("Microsoft Yi Baiti", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(22, 18)
        self._label1.Name = "label1"
        self._label1.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label1.Size = System.Drawing.Size(211, 133)
        self._label1.TabIndex = 0
        self._label1.Text = "Quantity Sold:"
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(254, 15)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(163, 251)
        self._listBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label2.Font = System.Drawing.Font("Microsoft Yi Baiti", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(34, 52)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(78, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "Package A:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label3.Font = System.Drawing.Font("Microsoft Yi Baiti", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(34, 84)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(78, 23)
        self._label3.TabIndex = 3
        self._label3.Text = "Package B:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label4.Font = System.Drawing.Font("Microsoft Yi Baiti", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(34, 110)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(78, 23)
        self._label4.TabIndex = 4
        self._label4.Text = "Package C:"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(119, 52)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(119, 81)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(119, 110)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 20)
        self._textBox3.TabIndex = 7
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button1.Font = System.Drawing.Font("Microsoft Yi Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(22, 155)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(211, 48)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button2.Font = System.Drawing.Font("Microsoft Yi Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(22, 209)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(109, 48)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button3.Font = System.Drawing.Font("Microsoft Yi Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(137, 209)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(96, 48)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(429, 274)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg 269 Sales"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    

    def Button1Click(self, sender, e):
        #Todo: All of this
        A
        B
        C