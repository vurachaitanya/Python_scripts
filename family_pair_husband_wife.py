family_names={
'chaitu' : 'bindhu',
'ramu' : 'roja',
'sudhir' : 'sindhu',
'hanumantharao' : 'anuradha',
}
import random
husband = list(family_names.keys())
for i in [ 1, 2, 3, 4]:
    husband_names = random.choice(husband)
    wife_names = family_names[husband_names]
    wife_guess = raw_input("what is the wifes name of" + husband_names + "? ")
#    print (wife_names)

    if wife_guess == wife_names:
        print (" Correct ! Nice job")
    else:
        print ("Incorrect . Correct husband name of " + husband_names + "is " + wife_names)
print ("All Done")
