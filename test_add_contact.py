# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_co import Application_co

@pytest.fixture
def app(request):
    fixture = Application_co()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Ann", lastname="Smith", email="asm@gmail.com"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", lastname="", email=""))
    app.logout()


