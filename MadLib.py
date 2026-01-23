#MadLib.py
#Name: Miguel Alvarado
#Date: 1/22/2026
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
noun1 = input("Enter a noun: ")
adjective1 = input("Enter a adjective: ")
place1 = input("Enter a place: ")
adjective2 = input("Enter a adjective: ")
adjective3 = input("Enter a adjective: ")
noun2 = input("Enter a noun: ")
  #Print the story with the user supplied words.
print("I love to make" , noun1 + "!" , "They are very" , adjective1 +"!")
print("I usually eat them at my", place1 +".")
print("I like when it is", adjective2 + ".")
print("I don't like when it is", adjective3 +".")
print("Anyways thanks for listening my", noun2 +".")



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
