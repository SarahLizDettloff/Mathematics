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
    public partial class buoyancy : Form
    {
        double volume = 0;
        double liquidDensity = 0;
        double force = 0;

        public buoyancy()
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
            lb2.Show();
            lbl3.Show();
            txtVariable1.Show();
            txtVariable2.Show();
            txtVariables3.Show();
        }


        private void buoyancy_Load(object sender, EventArgs e)
        {
            checkboxWaterDensity.Checked = false;
            checkBox1.Checked = false;
        }



        public void btnEnter_Click(object sender, EventArgs e)
        {
            double result = 0;
            try
            {
                liquidDensity = double.Parse(txtVariable1.Text);
                force = double.Parse(txtVariable2.Text);
                volume = double.Parse(txtVariables3.Text);
            }
            catch
            {
                MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.", "Buoyancy");
            }
            finally
            {
                result = volume * liquidDensity * force;
                lblResult.Text = result.ToString() + " Newtons";
            }

        }

        private void btnBack_Click(object sender, EventArgs e)
        {
            main goBack = new main();
            goBack.Show();
            this.Close();
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            double volume = 0;
            double liquidDensity = 0;
            double force = 0;
            txtVariable1.Clear();
            txtVariable2.Clear();
            txtVariables3.Clear();
            lblResult.Text = "";
        }

        private void checkboxWaterDensity_CheckedChanged(object sender, EventArgs e)
        {
            liquidDensity = 1000;
            txtVariable1.Text = liquidDensity.ToString();
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            force = 9.81;
            txtVariable2.Text = force.ToString();
        }

        private void btnHelp_Click(object sender, EventArgs e)
        {
            volumeFrm volumeForm = new volumeFrm();
            volumeForm.Show();
        }
    }
}
