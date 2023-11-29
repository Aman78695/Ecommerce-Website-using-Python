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
    #self.change_sign_in_text()
  def toggle_my_course_link(self):
    self.link_2.visible=anvil.users.get_user()!=None

  # Any code you write here will run before the form opens.
  def change_sign_in_text(self):
    user=anvil.users.get_user()
    
    if user:
      email=user['email']
      self.link_3.text=email
      self.toggle_my_course_link()

    
      
    # else:
    #   self.link_3.text='Sign In'

  def link_1_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Home())

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(MyCourses())

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    user=anvil.users.get_user()
    if user:
      logout=confirm('Do you want to logout')
      if logout:
        anvil.users.logout()
        self.content_panel.clear()
        self.content_panel.add_component(Home())
    else:
      anvil.users.login_with_form()
      self.change_sign_in_text()
      
  
