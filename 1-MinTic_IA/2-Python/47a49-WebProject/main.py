from flask import Flask, render_template, request, flash, redirect
from Models.Contacts import  ContactBook

app = Flask(__name__)
contact_book = ContactBook()
app.secret_key = 'some_secret' #Para manejar la seguridad


@app.route(r'/', methods=['GET']) #'r' para aceptar expresiones regulares
def Contact_Book():
    contacts = contact_book.RetrieveContacts()
    return render_template('contact_book.htm', contacts=contacts)

@app.route(r'/add', methods=['GET', 'POST'])
def AddContact():

    if request.form:
        name = request.form.get('name')
        contact_book.add(request.form.get('id'),
                        request.form.get('name'),
                        request.form.get('phone'),
                        request.form.get('email'))
        flash('Contacto añadido {} con exito'.format(request.form.get('name')))
    return render_template('add_contact.htm')


@app.route(r'/contacts/<identification>', methods=['GET'])
def ContactDetails(identification):
    # Recupero el contacto del archivo buscando por el parametro recivido 
    contact = Contact.get_by_id(int(identification)) #utilizando app engine de google

    if not contact:
        return redirect('/', code=301)

    return render_template('contactDetail.html', contact=contact)


@app.route(r'/delete', methods=['POST'])
def delete_contact():
    contact = Contact.get_by_id(int(request.form.get('uid')))
    contact.key.delete()
    return redirect('/contacts/{}'.format(contact.key.id()))

if __name__ == '__main__':
    app.run()