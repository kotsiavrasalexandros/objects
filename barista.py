class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, receipt):
        self.receipt = receipt

    def add_item(self, item):
         self.receipt.append(item)
    def calculate_total(self):
        count = 0
        for i in range(len(self.receipt)):
            count += float(self.receipt[i].price)
        return float(count)
    def calculate_taxes(self):
         tax = self.calculate_total() * 0.07
         total = self.calculate_total() + tax
         return total
    def print_reciept(self):
         for i in range(len(self.receipt)):
              print(self.receipt[i].name + " " + str(self.receipt[i].price))
         print("Total: ", self.calculate_total())
         print("+ Tax: ", self.calculate_taxes())


def main():
   
   menu = [
       MenuItem("bagel", 3.00),
       MenuItem("burrito", 5.00),
       MenuItem("ramen", 1.50),
       MenuItem("gum", 0.50)
   ]
     
   order1 = Order([])
   order1.add_item(menu[1])
   order1.add_item(menu[1])
   order1.add_item(menu[3])

   total = order1.calculate_total()
   print("The total due is " + str(total))

   order1.print_reciept()
   

if __name__ == '__main__':
	main()
