def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and len(s) >= 2 and len(s) <= 6:
        if (not s[3:-2].isnumeric() and not s[-1].isnumeric()) and s.isalnum():
            return True
    else:
        return False

main()
