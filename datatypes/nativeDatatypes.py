#type,isInstance
#gives type of the argument
print(type(1))
#checks if first arg is instance of second arg.Returns boolean
print(isinstance(1,int))


#coersing float to int(converts towards a value closer to zero)
print(int(2.5)) #op=>2
print(int(-2.5)) #op=>-2

#// division does not always returns int.If one of the number is float,a complete float is returned
print(2.0//1) #op=>2.0
print(2//1.0) #op=>2.0
print(21.1//5) #op=>4.0


#slicing a list using negative indices
#As normal slicing works [inclusive,exclusive),the same way this works too.
a_list=[1,2,2.1,"Jasdeep","Thursday"]
#from second element(index 1) till before the last element(last element has index -1)
print(a_list[1:-1]) #op=>[2, 2.1, 'Jasdeep']

#adding items to a list
b_list=["May",10]
#to use plus operator.This is inefficient as it is concatination + assignment
a_list=a_list+b_list
print(a_list)#op=>[1, 2, 2.1, 'Jasdeep', 'Thursday', 'May', 10]
#using append
a_list.append(2018)
print(a_list)#op=>[1, 2, 2.1, 'Jasdeep', 'Thursday', 'May', 10, 2018]
#using insert(inserts at specific index{first argument})
a_list.insert(0,"This is new first element")
print(a_list)#op=>['This is new first element', 1, 2, 2.1, 'Jasdeep', 'Thursday', 'May', 10, 2018]
#using extend(Merges two lists)
a_list.extend(["This","is",1,"extension"])#op=>['This is new first element', 1, 2, 2.1, 'Jasdeep', 'Thursday', 'May', 10, 2018, 'This', 'is', 1, 'extension']
print(a_list)

#Searching in list
#returns count of value in list
print(a_list.count(1))#op=>2

#returns index of first occourance.Throws error if element does not exists.
print(a_list.index(1))#op=>1

#removing element from list
#throws ValueError for element not in list.
a_list.remove("Jasdeep")
print(a_list)#op=>['This is new first element', 1, 2, 2.1, 'Thursday', 'May', 10, 2018, 'This', 'is', 1, 'extension']

#if called with no arguments,pop removes and returns last element of list
#if called with argument(number),it returns and removes value at that index
print(a_list.pop())#op=>extension
print(a_list)#op=>['This is new first element', 1, 2, 2.1, 'Thursday', 'May', 10, 2018, 'This', 'is', 1]

print(a_list.pop(2))#op=>2
print(a_list)#op=>['This is new first element', 1, 2.1, 'Thursday', 'May', 10, 2018, 'This', 'is', 1]

#tuples don't change.So have obly access to index() method.Rest all same as lists(slicing,accessing)
a_tuple=("Jasdeep","is","23","years","old")
print(a_tuple.index("is"))#op=>1

#assigning multiple values at once
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print(THURSDAY)#op=>3

#SETS

a_set={1}
#empty_set is not {} because it is empy dictionary
empty_set=set()

#adding an element to set
a_set.add(2)
#if element already exists nothing adds
a_set.add(1)
print(a_set)#op=>{1, 2}
#update-adds elements of both the sets.
a_set.update({1,2,3,4,5,6,7})
print(a_set)#op=>{1, 2, 3, 4, 5, 6, 7}

#update can also take lists
a_set.update([7,8,9])
print(a_set)#op=>{1, 2, 3, 4, 5, 6, 7, 8, 9}

#to remove element from set,discard and remove are methods
#discard removes the element if exists and if does not exists,does nothing
a_set.discard(3)
a_set.discard(11)
print(a_set)#op=>{1, 2, 4, 5, 6, 7, 8, 9}
#remove will also act exactly same as discard,just would return a KeyError if element dne.
a_set.remove(4)
print(a_set)#op=>{1, 2, 5, 6, 7, 8, 9}

#pop method removes any random value from set since it is unordered.
print(a_set.pop())#op=>1
print(a_set)#op=>{2, 5, 6, 7, 8, 9}

#clear method clears all elements from set.
a_set.clear()
print(a_set)#op=>set()

#set operations
#Draw a typical venn diagram with two circles
#The individual components are A,B and intersection C
#(where A or B do not include C)
#Union=>A+B+C
#intersection=>C
#difference=>either A or B
#symmetric_difference=>A+B(elements in exactly one of the sets)

x_set={1,2,3,4,5}
y_set={4,5,6,7,8}

print(x_set.union(y_set))#op=>{1, 2, 3, 4, 5, 6, 7, 8}
print(x_set.intersection(y_set))#op=>{4,5}
print(x_set.difference(y_set))#op=>{1,2,3}
print(y_set.difference(x_set))#op=>{6,7,8}
print(x_set.symmetric_difference(y_set))#op=>{1,2,3,6,7,8}


#Comparing sets
print(x_set.issubset(y_set))

#boolean value of None is False
print(bool(not None))









