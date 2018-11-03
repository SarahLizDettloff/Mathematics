using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Mathematics
{
    public partial class volumeFrm : Form
    {
        public volumeFrm()
        {
            InitializeComponent();
            if (Control.ModifierKeys == Keys.Escape)
            {
                ActiveForm.Close();
                this.Close();
            }
        }

        public void showVariables()
        {
            lb1.Show();
            txtVariable1.Show();
        }

        private void volumeFrm_Load(object sender, EventArgs e)
        {
            rbCone.TabStop = false;
            rbCube.TabStop = false;
            rbRectangularPrism.TabStop = false;
            rbCylinder.TabStop = false;
            rbPyramid.TabStop = false;
            rbSphere.TabStop = false;

            lb1.Hide();
            txtVariable1.Hide();

            lb2.Hide();
            txtVariable2.Hide();

            lbl3.Hide();
            txtVariables3.Hide();
        }

        private void rbCube_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Length of one of the sides of the cube in meters:";
                    showVariables();
                }
            }
        }

        private void rbRectangularPrism_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Length in meters:";
                    lb2.Text = "Width in meters:";
                    lbl3.Text = "Height in meters:";
                    txtVariables3.Show();
                    txtVariable2.Show();
                    txtVariable1.Show();
                    lb1.Show();
                    lb2.Show();
                    lbl3.Show();

                }
            }
        }

        private void rbCylinder_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Diameter of the cylinder in meters:";
                    lb2.Text = "Height in meters:";
                    txtVariable2.Show();
                    txtVariable1.Show();
                    lb1.Show();
                    lb2.Show();
                    lbl3.Hide();
                    txtVariables3.Hide();

                }
            }
        }

        private void rbPyramid_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Length of the base of the square pyramid in meters:";
                    lb2.Text = "Height in meters:";
                    txtVariable2.Show();
                    txtVariable1.Show();
                    lb1.Show();
                    lb2.Show();
                    lbl3.Hide();
                    txtVariables3.Hide();

                }
            }
        }

        private void rbCone_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Diameter in meters:";
                    lb2.Text = "Height in meters:";
                    txtVariable2.Show();
                    txtVariable1.Show();
                    lb1.Show();
                    lb2.Show();
                    lbl3.Hide();
                    txtVariables3.Hide();

                }
            }
        }


        private void rbSphere_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Diameter in meters:";
                    showVariables();
                }
            }
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is RadioButton)
            {
                RadioButton radioButton = (RadioButton)sender;
                if (radioButton.Checked)
                {
                    lb1.Text = "Diameter in meters:";
                    lb2.Text = "Height in meters:";
                    txtVariable2.Show();
                    txtVariable1.Show();
                    lb1.Show();
                    lb2.Show();
                    lbl3.Hide();
                    txtVariables3.Hide();

                }
            }
        }

        private void btnEnter_Click(object sender, EventArgs e)
        {
            double height = 0;
            double width = 0;
            double length = 0;
            double diameter = 0;
            double result = 0;

            if (rbCube.Checked)
            {
                try
                {
                    length = double.Parse(txtVariable1.Text);
                }
                catch
                {
                    MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.", "Volume");
                }
                finally
                {
                    result = length * length * length;
                    lblResult.Text = result.ToString() +" meters^3";
                }

            }
            else if (rbRectangularPrism.Checked)
            {
                try
                {
                    length = double.Parse(txtVariable1.Text);
                    width = double.Parse(txtVariable2.Text);
                    height = double.Parse(txtVariables3.Text);
                }
                catch
                {
                    MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.", "Volume");
                }
                finally
                {
                    result = length * width * height;
                    lblResult.Text = result.ToString() + " meters^3";
                }

            }
            else if (rbCylinder.Checked)
            {
                try
                {
                    diameter = double.Parse(txtVariable1.Text);
                    height = double.Parse(txtVariable2.Text);
                }
                catch
                {
                    MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.", "Volume");
                }
                finally
                {
                    result = 3.14159265359 * (diameter / 2) * height;
                    lblResult.Text = result.ToString() +" meters^3";
                }
            }
            else if (rbPyramid.Checked)
            {
                try
                {
                    length = double.Parse(txtVariable1.Text);
                    height = double.Parse(txtVariable2.Text);

                }
                catch
                {
                    MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.", "Volume");
                }
                finally
                {
                    length = length * length;
                    result = (length * height) * (1/3);
                    lblResult.Text = result.ToString() + " meters^3";
                }
            }
            else if (rbCone.Checked)
            {
                double radius = 0;
                try
                {
                    diameter = double.Parse(txtVariable1.Text);
                    height = double.Parse(txtVariable2.Text);
                }
                catch
                {
                    MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.", "Volume");
                }
                finally
                {
                    radius = diameter / 2;
                    radius = radius * radius;
                    result = (1/3) * (3.14159265359 * radius * height);
                    lblResult.Text = result.ToString() + " meters^3";
                }
            }
            else if (rbSphere.Checked)
            {
                try
                {
                    diameter = double.Parse(txtVariable1.Text);
                }
                catch
                {
                    MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.", "Volume");
                }
                finally
                {
                    result = (4/3) * ((diameter/2)  *(diameter/2)) * 3.14159265359;
                    lblResult.Text = result.ToString() + " meters^3";
                }
            }
            else
            {
                MessageBox.Show("Click on a radio button to execute the equation of your choice.", "Volume");
            }
        }


        private void btnBack_Click(object sender, EventArgs e)
        {
            this.Close();
        }


        private void btnClear_Click(object sender, EventArgs e)
        {
            rbCone.TabStop = false;
            rbCube.TabStop = false;
            rbRectangularPrism.TabStop = false;
            rbCylinder.TabStop = false;
            rbPyramid.TabStop = false;
            rbSphere.TabStop = false;

            lblResult.Text = "";
            txtVariable1.Clear();
            txtVariable2.Clear();
            txtVariables3.Clear();

            lb1.Hide();
            txtVariable1.Hide();

            lb2.Hide();
            txtVariable2.Hide();

            lbl3.Hide();
            txtVariables3.Hide();
        }
    }
}
