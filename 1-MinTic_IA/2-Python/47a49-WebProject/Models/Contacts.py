import csv
import os.path

# save_path = 'D:/David A/Repositories/Platzi/1-MinTic_IA/2-Python/47-WebProject/' #Inaltec
save_path = 'D:/Repositories/Platzi/1-MinTic_IA/2-Python/47a49-WebProject/' #Laptod
fileName = 'Contactos'
completeName = os.path.join(save_path, f"{fileName}.txt")

class Contact:

    def __init__(self, identification, name, phone, email):
        self._id = identification
        self._name = name
        self._phone = phone
        self._mail = email

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self,identification, name, phone, mail):
        contact = Contact(identification, name,phone, mail)
        self._contacts.append(contact)
        self._SaveContact()

    def ShowAll(self):
        for contact in self._contacts:
            self._PrintContact(contact)
    
    def DeleteContact(self, name):
        for idx, contact in enumerate(self._contacts): #enumarate obtengo indice y objeto
            if contact._name.lower() == name.lower():
                del self._contacts[idx]
                self._SaveContact() 
                break

    def SearchContact(self, name):        
        for idx, contact in  enumerate(self._contacts):
            if contact._name.lower() == name.lower():
                self._PrintContact(contact)
                return idx
        else: #Si el for no cae en el break, entra a este else
            self._NotFoundContact()
            return None

    def UpdateContact(self, contact, idx):
        self._contacts[idx] = contact
        self._SaveContact()

    def _NotFoundContact(self):
        print('*************')
        print('No encontramos el contacto')
        print('*************')

    def _SaveContact(self):
        with open(completeName, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(('id','name', 'phone', 'mail'))

            for contact in self._contacts:
                writer.writerow((contact._id, contact._name, contact._phone, contact._mail))
    
    def RetrieveContacts(self):
        self._contacts = []
        with open(completeName, 'r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):                
                if  index == 0:
                    continue
                self._contacts.append(Contact(row[0], row[1], row[2], row[3]))
        return self._contacts



    def _PrintContact(self, contact):
        print('--------*--------*--------*--------*--------*--------*------')
        print(f'Name: {contact._name}')
        print(f'Telefono: {contact._phone}')
        print(f'Email: {contact._mail}')
        print('--------*--------*--------*--------*--------*--------*------')
