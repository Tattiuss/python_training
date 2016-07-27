# -*- coding: utf-8 -*-
import pytest
from fixture.application_co import Application_co
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application_co()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ann", lastname="Smith", email="asm@gmail.com"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", email=""))
    app.session.logout()


