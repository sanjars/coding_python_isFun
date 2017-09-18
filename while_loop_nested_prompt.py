# Small nested While loops with if else statements.
# At the prompt, it asks you to type one of the kinds of products that you would
# like to see.

import sys

vegetables = ['potato','tomato','onions','green pepper','cucumber']
fruits = ['apricot','apple','pineapple','strawberry','peach','banana']

while True:
	while True:
		answer_1 = input('\nPlease choose what kind of products you would like to see:' + '\n' + '\n1)Vegetables\n2)Fruits' + '\n' + '\nTo Exit the program type quit OR exit\nChoose 1 OR 2 >')
		if answer_1 == '1':
			print("\nVegetables are:")
			for name in vegetables:
				print('\n' + name.title())
			break
		elif answer_1 == '2':
			print("\nFruits are:")
			for name in fruits:
				print('\n' + name.title())
			break
		elif answer_1 == 'exit' or answer_1 == 'quit':
			sys.exit()
		else:
			print("\nIncorrect Option! Enter 1 OR 2")
	





