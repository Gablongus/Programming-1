import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(209, 31)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(147, 20)
        self._textBox1.TabIndex = 1
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(77, 31)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(137, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Annual Salary:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(27, 58)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(215, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "Pay Periods Per Year:"
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(209, 57)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(147, 20)
        self._textBox2.TabIndex = 3
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(27, 111)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(215, 23)
        self._label3.TabIndex = 4
        self._label3.Text = "Salary Per Pay Period:"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button1.Font = System.Drawing.Font("Microsoft YaHei UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(141, 137)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(111, 48)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Location = System.Drawing.Point(209, 106)
        self._label4.Name = "label4"
        self._label4.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label4.Size = System.Drawing.Size(147, 23)
        self._label4.TabIndex = 7
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlLight
        self.ClientSize = System.Drawing.Size(410, 198)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Salary Calc"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        
        AnnualSalary = 0.0
        PayPeriods   = 0.0
        Salary       = 0.0
        
        try:
        AnnualSalary = float(self._textBox1.Text)
        PayPeriods   = int(self._textBox2.Text)
        except:
            MessageBox.Show("The input files must contain nonzero numeric values.", "Error")