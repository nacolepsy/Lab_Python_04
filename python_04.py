#Question 1_a Code to add champagne
print "---------------Question 1_a Code to add champagne-----------------"
groceries = ['bananas','strawberries','apples','bread']
groceries.append('champagne')
print groceries,
print
print
#Question_1_b Remove Bread
print
print "----------------1_b Remove Bread----------------"
groceries.remove('bread')

print groceries

print
print
#Question_1_c
print "----------------Question_1_c--------------------"
print
store={'D':'Dorkunu','A':'Apple','B':'Bread','C':'Cocumber','S':'Strawberry','K':'Kenkey'}
#print store


def sortedDictValues1(adict):
    items = adict.items()
    items.sort()
    
    for i in items:
        print i
    return [value for key, value in items]
sortedDictValues1(store)

print

#Question 2_b
print '----------------------Question 2_b------------------------'
print
prices={'apples':'7.3','Bannanas':'5.5','Bread':'1.0','Carrots':'10.0','Champagne':'20.90','Strwberries':'32.6'}
#for price in prices:
print prices
print
print
#Question 2_c
prices ['Strwberries']=63.43
print
print
print prices
print "-------------Question 2_c---------------"
#Question 2_d
print
print '----------------------------------------------'
prices['Chicken']=6.5
print prices
print
print
print '-----------------------Question 3_a-----------------------'
#Question 3_a
print "The best data structure will be List"
print
print
print '-------------------Question 3_b---------------------------'

#Question 3_b
in_stock={'1':'Bread','2':'Banku','3':'Neat Fufu','4':'Cheese'}
print
print in_stock
print

print "-------------------Question 3_C------------------"

#Question 3_C
print "Tuples cannot be changed!"
print
print "-------------------------------------"
print
always_in_stock=('1: Bread','2: Banku','3: Neat Fufu','4: Cheese')
print always_in_stock
print
print
print "Come to shoprite! We always sell:"
for item in always_in_stock:
    print item


#def binary_insert(1.1,0.50, 1.25, 1.50):
#modifies the input list to include the new_float
    #return

    #print binary_insert


print
print
#Question_4_a
print "Question_4_a"
print
print "Dictionary Datastructure will be the best for storing different market prices associated with all the items on their grocery lists"
print
print

