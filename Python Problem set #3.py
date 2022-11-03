def currencyConverter():
    Yuan = {"dollarY" : 0.14,
            "euroY" : 0.14,
            "liraY" : 2.56,
            "yuanY" : 1}
    Dollar = {"euroD" : 1.01,
              "yuanD" : 7.28,
              "liraD" : 18.60,
              "dollarD" : 1}
    Euro = {"dollarE" : 0.99,
            "yuanE" : 7.18,
            "liraE" : 18.35,
            "euroE" : 1}
    Lira = {"dollarL" : 0.054,
            "euroL" : 0.055,
            "yuanL" : 0.39,
            "liraL" : 1}

    oCurrency = input("Please enter which type of currency you have. Choose from the list:\n1. United States Dollar\n2. European Euro\n3. Chinese Yuan\n4. Turkish Lira\n")

    money = input("Please enter how much money you have:\n")
    money = float(money)

    fCurrency = input("Please enter which type of currency you would like to convert to. Choose from the list:\n1. United States Dollar\n2. European Euro\n3. Chinese Yuan\n4. Turkish Lira\n")
                      
    if float(oCurrency) == 1:
        if float(fCurrency) == 1:
            conversionFactor = Dollar.get("dollarD")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 2:
            conversionFactor = Dollar.get("euroD")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 3:
            conversionFactor = Dollar.get("yuanD")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 4:
            conversionFactor = Dollar.get("liraD")
            total = money * conversionFactor
            print(total)
    elif float(oCurrency) == 2:
        if float(fCurrency) == 1:
            conversionFactor = Euro.get("dollarE")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 2:
            conversionFactor = Euro.get("euroE")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 3:
            conversionFactor = Euro.get("yuanE")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 4:
            conversionFactor = Euro.get("liraE")
            total = money * conversionFactor
            print(total)

    elif float(oCurrency) == 1:
        if float(fCurrency) == 1:
            conversionFactor = Yuan.get("dollarY")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 2:
            conversionFactor = Yuan.get("euroY")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 3:
            conversionFactor = Yuan.get("yuanY")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 4:
            conversionFactor = Yuan.get("liraY")
            total = money * conversionFactor
            print(total)

    elif float(oCurrency) == 1:
        if float(fCurrency) == 1:
            conversionFactor = Lira.get("dollarL")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 2:
            conversionFactor = Lira.get("euroL")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 3:
            conversionFactor = Lira.get("yuanL")
            total = money * conversionFactor
            print(total)
        elif float(fCurrency) == 4:
            conversionFactor = Lira.get("liraL")
            total = money * conversionFactor
            print(total)
        
def groceryList(List):
    Groceries = {"apple" : 1.50,
                 "orange" : 1.00,
                 "banana" : 1.00,
                 "bagel" : 1.25,
                 "cabbage" : 1.50,
                 "spinach" : 4.25,
                 "milk" : 2.75,
                 "eggs" : 3.25,
                 "cake" : 8.00,
                 "pasta" : 3.50}
    total = 0
    for i in range(len(List)):
        v = Groceries.get(List[i])
        total = total + float(v)

    print(total)
        
    print ("You have purchased: ", List)
    print ("Your total is: $", total)
    

def main():
    #currencyConverter()
    groceryList(['orange','eggs','pasta'])

if __name__ == "__main__":
    main()
