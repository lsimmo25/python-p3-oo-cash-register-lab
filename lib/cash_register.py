#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.transactions = []
    
  
  def apply_discount(self):
    discount_amount = (self.discount / 100) * self.total
    self.total -= discount_amount
    if discount_amount > 0:
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
  
  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(title)
      self.transactions.append(price * quantity)

  def void_last_transaction(self):
    self.items.pop()
    self.total -= self.transactions[-1]
    self.transactions.pop()