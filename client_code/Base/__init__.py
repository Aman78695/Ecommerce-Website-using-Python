from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from .Home import Home
from ..MyCourses import MyCourses

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Home())
    self.change_sign_in_text()

    # Any code you write here will run before the form opens.
  def change_sign_in_text(self):
    user=anvil.users.get_user()
    if user:
      email=user['email']
      self.sign_in_text=email
    else:
      self.sign_in_text='Sign In'

  def link_1_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Home())

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(MyCourses())

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.login_with_form()
    self.change_sign_in_text()
    
  
