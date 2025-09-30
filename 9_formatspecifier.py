# format specifiers = {: flags } format a avlue based on what flags are inserted


# :.(num)f = round to that many decimal places
# :(num) = allocate that many spces #  $   123.453
# :03 = aalocate and zero pad that many spaces #$0123.453
# :< = left justify
# :> = right justify
# :^ = center allign same as :(num)
# :+ = use a plus sign to indicate positive value
# :=  = place sign to leftmost position # default
# :  = insert a space before positive numbers
# :, = comma seperator for whole number not decimal


p1 = 12223.453456
p2 = -43.1

print(f"The p1 is ${p1:+,.3f}")
print(f"the p2 is ${p2:,}")