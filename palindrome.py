def palindrome(n):
    if n==n[::-1]:
        print("Palindrome number!")
    else: 
        print("Not a palindrome number")
def main():
    n=input("Enter number: ")
    palindrome(n)
main()
#Code verified
