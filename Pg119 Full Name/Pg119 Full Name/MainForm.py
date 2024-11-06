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
        self._textBox2 = System.Windows.Forms.TextBox()
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
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 2
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(141, 60)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 3
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkOrchid
        self.ClientSize = System.Drawing.Size(468, 354)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg119 Full Name"
        self.ResumeLayout(False)
        self.PerformLayout()

