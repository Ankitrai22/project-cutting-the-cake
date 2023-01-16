import re
mystr= "Tata Motors Ltd (Tata Motors), India's largest automobile manufacturer and the country's largest OEM (original equipment manufacturerarar) with a 76-year legacy, leads the commercial vehicles industry with over 45% market share. It is also amongst the top 3 brands in the passenger vehicles segment with a rapidly growing double-digit market share — more than double of last year. Globally, Tata Motors has a presence in over 125 countries with a worldwide network of over 8,400 touchpoints. Over 8.5 million Tata branded vehicles ply on the roads, offering the highest standards of quality, safety, environmental norms, and passengerarr comfort."
print(r"\n")
patt=re.compile(r"market")
matches= patt.finditer(mystr)
for match in matches:
    print(match)
patt= re.compile(r'(ar){1}|t')
matches= patt.finditer(mystr)
