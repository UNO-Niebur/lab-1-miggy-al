#FirstProgram.py
#Name: Miguel Alvarado
#Date: 1/22/2026
#Assignment: Lab 1

def main():
  print("First Program")
  #Say hello
print("hello")
  #Ask for the user's name
name= input("what is your name?")
  #Use the user's name in the program.
print("hello", name)
  #Ask the user for their age.
age= int(input("how old are you?"))
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
birthyear=2026-age-1
print("you were born in", birthyear,name)
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
