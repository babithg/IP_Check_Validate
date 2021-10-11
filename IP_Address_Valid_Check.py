import re

def range_check(number):
    if number >= 0 and number <= 255:
        return True
    else :
        return False

def without_re():
    try:
        ip_address = input("Enter a IP Address : ")
        number_group = [int(x) for x in ip_address.split(".")]
        result = list(map(range_check, number_group))
        if len(result) == 4 and False not in result:
            print("Your IP address {} is valid".format(ip_address))
        else: 
            print("Your Entered value {} not valid IP address".format(ip_address))
    except ValueError:
        print("[ERROR] Invalid format please use . as a number seperation")
        print("Syntax: int.int.int.int")
    except Exception as e:
        print("[ERROR] Invalid input ", e)

def with_re():
    try:
        ip_address = input("Enter a IP Address: ")
        pattern = r"^\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}\s{0,}$"
        number_group = [int(x) for x in ip_address.split(".")]
        if re.match(pattern, ip_address) and all(list(map(range_check, number_group))):
            print("Matching the group {}".format(ip_address))
        else:
            print(f"Not Matching {ip_address}")
    except ValueError:
        print("Value error")
   
if __name__ == '__main__':
    print("\n", "**" * 25)
    print(" Welcome to Simple Program ","\n To check the input is a valid IP address or not")
    print("\n","**" * 25)
    #without_re()
    with_re()
