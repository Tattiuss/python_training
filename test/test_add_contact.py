# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="",
    email="", email2="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
    address=random_string("address", 20), homephone=random_string("homephone", 15),
    mobilephone=random_string("mobilephone", 15), email=random_string("email", 20), email2=random_string("email2", 20))
    for i in range(7)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", lastname="", email="")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


