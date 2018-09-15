list = [10,-8,20,15,-10]
list = [int(x) for x in list]

next_list = list.copy()
next_list.pop(0)
period_delta = []

#for x in range(len(next_list)):
    #if (list[x] > 0 and next_list[x] > 0):
       # delta = next_list[x] - list[x]
        #period_delta.append(delta)
    #elif (list[x] > 0 and next_list[x] < 0):
        #delta = next_list[x] + list[x]
        #period_delta.append(delta)
    #elif (list[x] < 0 and next_list[x] < 0):
     #   delta = next_list[x] - list[x]
      #  period_delta.append(delta)

avg_list1 = sum(list)/(len(list))

print(avg_list1)



#print(list)
#print("Here's what you did:")
#print(next_list)

#print("Did it work?")
#print(period_delta)

list_abs = [abs(x) for x in list]
#print(list_abs)
#print(len(list))


