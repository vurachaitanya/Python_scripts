your_list=["a","b","c"]
print your_list
type(your_list)
len(your_list)
"a" in your_list
print your_list[0]
your_list.append("d")
print your_list
#===============================================^
#===============================================^
#===============================================^
#===============================================^
name=["chaitu","bindhu"]
print name
name.append("nidhi")
print name
name[0]="darpad"
print name[0]
name.append("anuradha")
print name
print name[len(name) -1]
print name[-1]
print name[-2]
print "anuradha" in name
for names in name:
    print names
for names in name:
    print ("hello " +  names)
for names in name:
    if names[0] in "aeiou":
        print ( names + " starts with Vowels")
