import os
from modules.emr.emr import *
from modules.generic.generic import *
from modules.instance.instance import *
from flask import *
app = Flask(__name__)

session = establish_session()

@app.route("/ec2-table1")
def show_vertical_tables():
    app.logger.info("Displaying instance details in vertical table format")
    data = create_instance_table(session)
    return render_template('ec2-table1.html',tables=[data.to_html(classes='metadata')],titles = ['Instance Details'])

@app.route("/ec2-table2")
def show_vertical_tables2():
    app.logger.info("Displaying instance details in vertical table format")
    data = create_instance_table2(session)
    return render_template('ec2-table2.html',tables=[data.to_html(classes='metadata')],titles = ['Instance Details'])

@app.route("/ec2-table3")
def show_horizontal_tables():
    app.logger.info("Displaying instance details in horizontal table format")
    data = create_horizontal_instance_table(session)
    return render_template('ec2-table3.html',tables=[data.to_html(classes='value')],titles = ['Instance Details'])

@app.route("/emr-table")
def emr_tables():
    app.logger.info("Displaying EMR details in horizontal table format")
    data1, data2 = create_emr_table(session)
    return render_template('emr-table.html',tables=[data1.to_html(classes='value'),data2.to_html(classes='value')],titles = ['EMR Details'])

@app.route("/")
def home():
    app.logger.info("Homepage")
    return render_template('index.html',titles = ['Flask Assignment'])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
