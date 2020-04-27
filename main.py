from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    mentor_city = request.args.get('mentor-city')
    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif mentor_city:
        mentor_details = data_manager.get_mentors_by_city(mentor_city)
    else:
        mentor_details = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('mentors.html', mentors=mentor_details)



@app.route('/applicants')
def applicants_list():
    applicant_details = data_manager.get_applicants()
    return render_template('applicants.html',applicants=applicant_details)


@app.route('/applicants-phone')
def applicants_phone():
    applicant_name = request.args.get('applicant-name')
    applicant_email = request.args.get('applicant-email')
    if applicant_name:
        applicant_phone = data_manager.get_applicant_data_by_name(applicant_name)
    elif applicant_email:
        applicant_phone = data_manager.get_applicant_data_by_email(applicant_email)
    return render_template('applicants-phone.html',applicant_name=applicant_phone)

@app.route('/applicants/<code>', methods=['GET','POST'])
def applicant_code(code):
    if request.method == 'POST':
        phone_no = request.form['new-phone']
        data_manager.update_phone_number(phone_no, code)
        return redirect('/applicants/' + code)
    else:
        applicant_details = data_manager.get_applicant_by_code(code)
    return render_template('applicants-update.html', applicants=applicant_details, code=code)


@app.route('/applicants/<code>/delete')
def delete_applicant(code):
    data_manager.delete_applicant(code)
    return redirect('/applicants')

@app.route('/applicants/deleteEmail', methods=['GET','POST'])
def delete_applicant_by_email():
    if request.method == 'POST':
        delete = request.form['delete-by-email']
        data_manager.delete_applicant_by_email(delete)
        return redirect('/applicants')
    return render_template('applicants.html')


@app.route('/add-applicants', methods=['GET','POST'])
def add_applicant():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        phone_number = request.form['phone-number']
        email = request.form['email']
        data_manager.add_applicant(first_name, last_name, phone_number, email)
        code = data_manager.get_max_id()
        code_data = code[0].get('max','')
        app_code = data_manager.get_application_code_by_id(code_data)
        applicant_code = app_code[0].get('application_code', '')
        return redirect('/applicants/' + str(applicant_code))
    return render_template('add-applicants.html')


if __name__ == '__main__':
    app.run(debug=True)
