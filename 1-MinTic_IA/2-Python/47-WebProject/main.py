from flask import Flask, render_template, request
from Models.Contacts import  ContactBook

app = Flask(__name__)
contact_book = ContactBook()


@app.route(r'/', methods=['GET']) #'r' para aceptar expresiones regulares
def Contact_Book():
    contacts = contact_book.RetrieveContacts()
    return render_template('contact_book.htm', contacts=contacts)

@app.route(r'/add', methods=['GET', 'POST'])
def AddContact():

    if request.form:
        contact_book.add(request.form.get('id'),
                        request.form.get('name'),
                        request.form.get('phone'),
                        request.form.get('email'))
    return render_template('add_contact.htm')

if __name__ == '__main__':
    app.run()