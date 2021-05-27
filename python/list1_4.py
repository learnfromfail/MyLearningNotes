friends = ["Kevin", "Karen", "Jim"]
friends2 = ["Kevin", 2, True, 38]
print(friends2[2]) #== -1 is the last one
print(friends2[-1])
print(friends2[1:]) #empty means all [after] the certain
print(friends2[2:1]) #empty

lucky_num = [4, 5, - 90 , 11, 77, 99]
lucky_num.extend(friends2)
lucky_num.append(12000)
lucky_num.insert(1, "haha")
lucky_num.remove("haha")
print(lucky_num)
lucky_num.pop() #remove the last element
print(lucky_num.index(2))
print(lucky_num.sort()) #throw error if str and int both exist
#sort #count #reverse
friends3 = friends2.copy() # if-else !!!
lucky_num.clear()