# Q2.  A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.


c = 1
dis = 0
totalAmt = 0
while(c==1):
    ch = int(input("Enter the product code you want to purchase:-\n1. Battery Based Toys\n2. Key-based Toys\n3. Electrical Charging Based Toys: "))
    amt = int(input("Enter order amount: "))
    if(ch==1 and amt>1000):
        dis = (amt*10)/100
    
    elif(ch==2 and amt>100):
        dis = (amt*5)/100

    elif(ch==3 and amt>500):
        dis = (amt*10)/100

    totalAmt = amt-dis
    print("\nNet amount after discount= Rs." + str(totalAmt))

    c = int(input("\nDo you want to make another purchase? 1 for Yes/ 0 for No: "))