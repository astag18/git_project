import string

def open_file(filename):
    a_string = ""
    my_file = open(filename, "r")
    new_14list = []
    new_15list = []
    new_16list = []
    new_17list = []
    new_18list = []
    new_19list = []
    line_list = []
    for line in my_file:
        a_string += line
    line_list = a_string.strip().split("\n")
    for i in line_list:
        a,b = i.strip().split("|")
        
        if "2019" in b and "2019-01" not in b:
            if a == "":
                a = 0
            else:
                a = float(a)
                new_19list.append(a)
        elif "2018" in b and "2018-01" not in b:
            if a == "":
                a = 0
            else:
                a = float(a)
                new_18list.append(a)
        elif "2017" in b and "2017-01" not in b:
            if a == "":
                a = 0
            else:
                a = float(a)
                new_17list.append(a)
        elif "2016" in b and "2016-01" not in b:
            if a == "":
                a = 0
            else:
                a = float(a)
                new_16list.append(a)
        elif "2015" in b and "2015-01" not in b:
            if a == "":
                a = 0
            else:
                a = float(a)
                new_15list.append(a)
        elif "2014" in b and "2014-01" not in b:
            if a == "":
                a = 0
            else:
                a = float(a)
                new_14list.append(a)
    the_14sum = 0
    the_15sum = 0
    the_16sum = 0
    the_17sum = 0
    the_18sum = 0
    the_19sum = 0
    for x in new_14list:
        the_14sum += x
    for x in new_15list:
        the_15sum += x
    for x in new_16list:
        the_16sum += x
    for x in new_17list:
        the_17sum += x
    for x in new_18list:
        the_18sum += x
    for x in new_19list:
        the_19sum += x
    the_19sum = (the_19sum/8)*11
    num14 = str(round(the_14sum))
    num15 = str(round(the_15sum))
    num16 = str(round(the_16sum))
    num17 = str(round(the_17sum))
    num18 = str(round(the_18sum))
    num19 = str(round(the_19sum))
    print("Fyrir utan janúar:")
    print("Heildarinnkoma fyrir árið 2014: €{}.{}".format(num14[0:3], num14[3:6]))
    print("Heildarinnkoma fyrir árið 2015: €{}.{}".format(num15[0:3], num15[3:6]))
    print("Heildarinnkoma fyrir árið 2016: €{}.{}".format(num16[0:3], num16[3:6]))
    print("Heildarinnkoma fyrir árið 2017: €{}.{}".format(num17[0:3], num17[3:6]))
    print("Heildarinnkoma fyrir árið 2018: €{}.{}".format(num18[0:3], num18[3:6]))
    print("Heildarinnkoma fyrir árið 2019: €{}.{}".format(num19[0:3], num19[3:6]))

def main():
    filename = input("Skrá: ")
    open_file(filename)

main()