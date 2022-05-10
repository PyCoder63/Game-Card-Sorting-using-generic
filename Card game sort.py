cards = ['Jack', 8, 2, 6, 'King', 5, 3, 'Queen']

required_output=[]
def SortedCard(cards):
	output = []
	
	for i in cards:
		if i=='Jack':
			i= 9
		elif i=='Queen':
			i=10
		elif i=='King':
			i=11
		output.append(i)
		output.sort()
	return output

def converString(output):
	for i in output:
		if i==9:
			i= 'Jack'
		elif i==10:
			i='Queen'
		elif i==11:
			i='King'
		required_output.append(i)
	return required_output

print('Sorted output: ',SortedCard(cards))
print('Required Output: ',converString(SortedCard(cards)))

"""The Case 1 remain the unsorted card"""
print('Case 1 unsorted: ',cards)

""" Case 2:"""
def case_two(Input):
	Case2 = SortedCard(Input)
	New_case = []
	for j in Case2:
		if j not in New_case:
			New_case.append(j)
	return converString(New_case)
Input1 = ['Jack', 8, 2, 6, 'King', 5, 3, 'Queen', 'Jack', 'King', 'Queen', 'Queen', 'King', 'Jack']
Test_case2 = case_two(Input1)
print('Case 2 output: ', Test_case2)

def case_three(inputs):
	sort=SortedCard(inputs)
	sort.reverse()
	sort1=converString(sort)
	return sort1
input2= ['Jack', 8, 6, 5, 3, 2]
Test_case3 = case_three(input2)
print('Case 3: ',Test_case3)
