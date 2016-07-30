# -*- coding: utf-8 -*-
import pytest
from fixture.application_co import Application_co

@pytest.fixture
def app(request):
    fixture = Application_co()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()