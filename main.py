import pytest
import enum

from enum import Enum
class MachineState(Enum):
  idle = 0              # Display "insert coin"
  interact = 1          # Display "50 cent"git 
  serve = 2             # Display "Serving..." or "30 cent missing"

pytest.inventory = {"cola" : (1.00, 23),
                    "chips": (0.50,  0),
                    "candy": (0.65, 13)}

pytest.amount_received = 0
pytest.system_State = MachineState.idle
pytest.selected_product = ""
pytest.current_display_text = "insert coin"

def reset():
  pytest.amount_received = 0
  pytest.system_State = MachineState.idle

def insert_coin(weight, diameter):
  pytest.amount_received = pytest.amount_received + 0.25
  pytest.current_display_text = str(pytest.amount_received)
  pytest.system_State=MachineState.interact
 
#def display_insert_coin():

def product_selection(what):
  price,qty = pytest.inventory[what]
  if qty >= 1:
    pytest.selected_product = what
    #Check price
    pytest.system_State = MachineState.serve
    pytest.current_display_text = "serving"
  else :
    pytest.system_State = MachineState.interact
    pytest.selected_product = ""
    pytest.current_display_text = "sold out"

def test_insert_coin_25_cent():
  insert_coin(20, 10)
  assert pytest.system_State == MachineState.interact
  assert pytest.amount_received == 0.25
  assert pytest.current_display_text == "0.25"

def test_insert_coin_25_centAgain():
  insert_coin(20, 10)
  assert pytest.system_State == MachineState.interact
  assert pytest.amount_received == 0.50
  assert pytest.current_display_text == "0.5"


def test_product_selection():
  product_selection("cola")
  assert pytest.selected_product == "cola"
  assert pytest.system_State == MachineState.serve
  assert pytest.current_display_text == "serving"

def test_product_selection_noQty():
  product_selection("chips")
  assert pytest.selected_product == ""
  assert pytest.system_State == MachineState.interact
  assert pytest.current_display_text == "sold out"

# def test_product_selection_not_enough_coins():
