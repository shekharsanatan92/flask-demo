import os
from modules.assignment import *
from flask import *
app = Flask(__name__)

@app.route("/vertical")
def show_vertical_tables():
    app.logger.info("Displaying instance details in vertical table format")
    data = create_instance_table()
    return render_template('index_vertical.html',tables=[data.to_html(classes='metadata')],titles = ['Instance Details'])

@app.route("/horizontal")
def show_horintal_tables():
    app.logger.info("Displaying instance details in horizontal table format")
    data = create_horizontal_instance_table()
    return render_template('index_horizontal.html',tables=[data.to_html(classes='value')],titles = ['Instance Details'])

@app.route("/emr")
def emr_tables():
    app.logger.info("Displaying EMR details in horizontal table format")
    data1, data2 = emr_details()
    return render_template('emr_details.html',tables=[data1.to_html(classes='value'),data2.to_html(classes='value')],titles = ['EMR Details'])

@app.route("/")
def home():
        app.logger.info("Homepage")
        return render_template('home.html',titles = ['Instance Details'])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(debug=True, host='0.0.0.0', port=port)
