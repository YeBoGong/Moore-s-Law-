'''
This program calculates a crude estimate of Moore's Law from
a starting number of transistors, starting year and total number of years
'''
#Creating a function in order to
def prefix_define(number):
    #creating an Array containing the prefixes for the flops
    prefixes = ["", "Kilo", "Mega", "Giga", "Tera", "Peta", "Exa", "Zetta", "Yotta"]
    #creating a variable called counter, it will keep track of the current prefix
    prefix_counter = 0
    #set dividednumber as the original number, it will be divded by a thousand
    divided_number = number

#while loop that will keep looping until the variable divided_number is greater or equal to 1000
# and prefix counter is lesser than the amount of prefixes there are
    while divided_number >= 1000 and prefix_counter < len(prefixes) - 1:
        #divide divided_number by 1000
        divided_number /= 1000
        #add 1 to prefix_counter
        prefix_counter = prefix_counter + 1
    #return the highest prefix and the  divided number after being divided by a thousand
    return prefixes[prefix_counter] + "FLOPS", divided_number
#print title of project
print("Moore's law calculator")
#have the user input the starting value of transistors
start_num = int(input("Starting Number of transistors: "))
#have the user input the starting year
start_year = int(input("Starting Year: "))
#have the user input the total number of years
total_year = int(input("Total Number of Years: "))
#set the end year as the starting year + the total years
end_year = int(start_year + total_year)
#calculate flops using the formula transistors*50
flops = start_num * 50
#set transitors as start_num so it is more understandable further in the code
transistors = start_num
#printing the titles
print("YEAR : TRANSISTORS : FLOPS : ")
#set the current year as the starting year, in order to have a counter go up
current_year = start_year
#while loop that repeats while the current year is lesser or equal to the end year
while current_year <= end_year:
    #format the transistors
    transistors_formatted = ('{:,}'.format(transistors))
    #get the flops unit, prefix from the function prefix_define)
    unit, value = prefix_define(flops)
    #format the flops number
    flops_number = ('{:,}'.format(flops))
    #format the flops with the prefix, add the prefix and the unit
    flops_formatted = "{:.2f} {}".format(value, unit)
    #print the current year, number of transistors, flops and the flops number
    print("%s %s %s %s" % (current_year, transistors_formatted, flops_formatted, flops_number))
    #add the current year by 2 since it is how many years it takes for transistors to double accoridng to moore's law
    current_year = current_year + 2
    #double the number transistors
    transistors = transistors * 2
    #double the number of flops
    flops = flops * 2

