from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
from firebase import firebase

firebase1 = firebase.FirebaseApplication(
    'https://nri-wellbeing-default-rtdb.asia-southeast1.firebasedatabase.app/',
    None
)

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = firebase1.get('server_email', None)
app.config['MAIL_PASSWORD'] = firebase1.get('server_pass', None)
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    address = firebase1.get('address', None)
    phone = firebase1.get('phoneNumber', None)
    projects1 = firebase1.get('projects', None)
    clients = firebase1.get('clients', None)
    members = firebase1.get('members', None)

    return render_template(
        'home.html',
        projects1=projects1,
        clients=clients,
        members=members,
        address=address,
        phone=phone
    )


@app.route('/enquiry', methods=['GET', 'POST'])
def services1():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get('email')
        service = request.form.get('service')
        message = request.form.get('message')

        msg = (
            f"CLIENT RESPONSE\n\n\n"
            f"Name : {name}\n"
            f"Email : {email}\n"
            f"Service Requested : {service}\n"
            f"Message : {message}"
        )

        client_email = firebase1.get('email', None)

        msg_send = Message(
            subject=f"New Enquiry from {name}",
            body=msg,
            sender=app.config['MAIL_USERNAME'],
            recipients=[client_email]
        )

        mail.send(msg_send)

        return render_template('enquiry.html')

    return render_template('enquiry.html')


@app.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')


@app.route('/faqs', methods=['GET', 'POST'])
def faq():
    return render_template('faqs.html')


@app.route('/about-us', methods=['GET', 'POST'])
def about():
    return render_template('about-us.html')


# ----- services ------------ #

@app.route('/construction-of-dream-houses', methods=['GET', 'POST'])
def const_dream_house():
    return render_template('construction-of-dream-houses.html')


@app.route('/facility-management', methods=['GET', 'POST'])
def facility_mng():
    return render_template('facility-management.html')


@app.route('/family-welfare', methods=['GET', 'POST'])
def family_welfare():
    return render_template('family-welfare.html')


@app.route('/financial-services', methods=['GET', 'POST'])
def financial_services():
    return render_template('financial-services.html')


@app.route('/leasing-services', methods=['GET', 'POST'])
def leasing_services():
    return render_template('leasing-services.html')


@app.route('/liaison-documentation-services', methods=['GET', 'POST'])
def liaison_documentation():
    return render_template('liaison-documentation-services.html')


@app.route('/logistics-tours-travel-services', methods=['GET', 'POST'])
def logistics():
    return render_template('logistics-tours-travel-services.html')


@app.route('/onboardservices', methods=['GET', 'POST'])
def onboard():
    return render_template('onboardservices.html')


@app.route('/properties-development', methods=['GET', 'POST'])
def prop_dev():
    return render_template('properties-development.html')


@app.route('/property-assets-management', methods=['GET', 'POST'])
def prop_assets_mng():
    return render_template('property-assets-management.html')


@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template('projects.html')


if __name__ == "__main__":
    app.run(threaded=True, debug=True)