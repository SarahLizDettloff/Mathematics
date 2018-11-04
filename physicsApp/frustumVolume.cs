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
    public partial class frustumVolume : Form
    {
        public frustumVolume()
        {
            InitializeComponent();
        }

        private void btnEnter_Click(object sender, EventArgs e)
        {
            double length = 0;
            double height = 0;
            double width = 0;
            double result = 0;

            try
            {
                height = double.Parse(txtHeight.Text);
                length = double.Parse(txtLength.Text);
                width = double.Parse(txtWidth.Text);
            }
            catch
            {
                MessageBox.Show("You did not enter all of the values. The empty variable will be assumed as null.", "Volume");
            }
            finally
            {
                result = (((3.333333333333) * height) * (length * length) * (length * width) * (width * width));
                lblResult.Text = result.ToString();
            }
        }

        private void frustumVolume_Load(object sender, EventArgs e)
        {

        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            txtHeight.Clear();
            txtWidth.Clear();
            txtLength.Clear();
            lblResult.Text = "";
        }

        private void btnBack_Click(object sender, EventArgs e)
        {
            main goBack = new main();
            goBack.Show();
            this.Close();
        }
    }
}
