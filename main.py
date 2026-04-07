from requests import get
from api import api_key



base_url = "https://v6.exchangerate-api.com/v6/"

def display_codes():
    print("\n----------------------AVAIALBlE CODES----------------------\n")
    url = f"{base_url}{api_key}/codes"
    response = get(url)

    if response.status_code != 200:
        print("API Error!!")
        return

    data = response.json()
    codes = data['supported_codes']

    for i in range(0,len(codes),2):
        left = f"{codes[i][0]} - {codes[i][1]}"
        
        if i+1<len(codes):
            right = f"{codes[i+1][0]} - {codes[i+1][1]}"
            print(f"{left:<60}  {right}")

        else:
            print(f"{left}")

    return codes



def currency_convertor():
    
    codes = display_codes()
    if not codes:
        return
    valid_codes = [code for code, _ in codes]

    print("\n----------------------PLEASE ENTER THE BASE CURRENCY CODE----------------------\n")
    base_code = input("Base Code : ").upper()

    if base_code not in valid_codes :
        print("Invalid base currency")
        return

    print("\n----------------------PLEASE ENTER THE AMOUNT----------------------\n")
    amount = float(input("Amount : "))
    print("\n----------------------PLEASE ENTER THE CONVERTOR CURRENCY CODE----------------------\n")
    converted_code = input("Convertor Code : ").upper()

    if converted_code not in valid_codes :
        print("Invalid convertor currency")
        return

    print("\nFetching rates..........\n")

    url2 = f"{base_url}{api_key}/latest/{base_code}"
    response2 = get(url2)

    if response2.status_code != 200:
        print("API Error!!")
        return
    data = response2.json()

    rate = data['conversion_rates'][converted_code]
    total_amount = (rate*amount)

    print(f"\n\nThe net converted amount is {total_amount:,.2f}")
    print(f"(1-{base_code} = {rate:.2f}-{converted_code})\n\n")

    with open("history.txt", "a") as f:
        f.write(f"{amount} {base_code} -> {converted_code} = {total_amount:.2f}\n")



    
print("\n----------------------HELLO WELCOME TO EXCHANGE RATE CONVERTER----------------------\n")

while(True):
    print("1. Convert currency")
    print("2. View history")
    print("3. Exit")

    option = int(input("\nSelect the option you want to choose : "))

    if(option == 1):
        currency_convertor()
    elif(option == 2):
        try:
            with open("history.txt","r") as f:
                print("\n")
                for line in f:
                    print(line.strip())
                print("\n\n")
        except :
            print("No history found.\n\n")
    elif(option == 3):
        break
    else:
        print("Invalid option\n\n")



