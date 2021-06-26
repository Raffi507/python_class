#1
h = int(input("tell me the height of the triangle\n>>> "))
s = int(input("Now tell me the side of the triangle\n>>> "))
	
def height(h):
	
	if h > 0:
		print("ok")
	else:
		print("You made a typo or just for simplity let me explain that the height of a triangle can't be less or equal to zero.")

def side(s):
	
	if s > 0:
		print("ok")
	else:
		print("You made a typo or just for simplity let me explain that the side of a triangle can't be less or equal to zero.")

	S = s * h /2
	print(S)

height(h)
side(s)


#2
a = input("Tell me something\n>>> ")

def reverse():

	print(">>>", a[ : : -1])

reverse()


#3


#4
text = input("Tell me something\n>>> ")

def checking(text):
	if text == text[ : : -1]:
		print("The text that you've written is palindrome")
	else:
		print("The text that you've written is not palindrome")


checking(text)
