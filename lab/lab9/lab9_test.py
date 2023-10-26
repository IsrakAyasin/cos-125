from lab.lab9.lab9_code import *


############################################################
# Name: DivideOnLessThan
# Header: def DivideOnLessThan(a,b)
# Parameters:
#   a: int or float
#   b: int or float
# Return:
#   float
# Description: This function has two parameters: a and b.
#   This function returns a/b if b < a. If b > a, then it
#   return 0.0

# WRITE TEST HERE
#print(DivideOnLessThan(0.1,0))#if b is 0 and b is less than a than there will be an error and it doesn't mention what happends if both of them are same

############################################################
# Name: AskYesOrNo
# Header: def AskYesOrNo():
# Parameters:
#   None
# Return:
#   Returns True if the user types any variant of yes or y
#   Returns False if the user types any variant of no or n
# Description:
#   Asks for yes or no repeatedly until the user gives an
#   accepted answer. Ignores case.

# WRITE TEST HERE
#AskYesOrNo()#(if you don't type anything you get an error) and (if you write anything start with y or n or yes or no it works, which it shouldn't)

############################################################
# Name: SearchListInReverse
# Header: def SearchListInReverse(alist, item)
# Parameters:
#   alist: a list
#   item: element to search for
# Return:
#   If item is in the list, returns index of item. 
#   If the item is not found in the list, None is returned.
# Description: This function searches through the list alist
#   for the element stored in item.

# WRITE TEST HERE
print(SearchListInReverse([77,2,"a",3,1,4,-2],77))#(if there is more than one element it won't work,) and it doesn't work for first item

############################################################
# Name: SplitStringAtPunctuation
# Header: def SplitStringAtPunctuation(astring)
# Parameters:
#   astring: a string that might or might not have punctuation.
# Return:
#   Returns a list containing the split strings with the punctuation
#   removed.
# Description: This function splits a string at punctuation.
#   Punctuation includes: . ? !
#   It does not remove whitespace before or after the splits.

# WRITE TEST HERE
#print(SplitStringAtPunctuation("amito.vlas . worw fsdg.d kdajf 112kldsajf?ouroi"))#(it also remove everything after the the last puntuation)

############################################################
# Name: ChoiceDiscrete
# Header: def ChoiceDiscrete(alist, problist):
# Parameters:
#   alist: a list of any type.
#   problist: a list of probabilities (ints or float). 
#       Must be the same size as alist.
# Return:
#   Returns a random element from alist. 
# Description: The probability
#   of each element being returned is given by the
#   problist. For example, if alist has two elements and
#   problist contains [1,8], then the second element in
#   alist is 8 times more likely to be returned than
#   the first element. In other words, probabilities are
#   relative.

# WRITE TEST HERE
#print(ChoiceDiscrete([1,2,3],[0,0,0]))#if you put 0% on on all of them you will get an error and x*x and y*y wrong method.(1,10)=(1,100) and negetive works