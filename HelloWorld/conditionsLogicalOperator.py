#Candidate has "Good Credit" and "High Income Level", then he is eligible for a loan
#Above condition can be implemented using "and" operator



has_good_credit = True
high_income_level = True
has_criminal_record = False

if has_good_credit and high_income_level:
    print("Eligible for loan1")

#using the "not" operator reverses the set value(Now both condition becomes true)

if has_good_credit and not has_criminal_record:
    print("Eligible for loan2")

