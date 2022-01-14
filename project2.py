import string

class VMmanager:
    def __init__(self):
        self.pm = [0]*(1024*512)
 
    def fill_pm(self, line1, line2):
        """initialized the pa without demand paging"""
        if line2 == []:
            return
        else:           
            line1_arr = []  
            segment_index = line1[0]*2 
            segment_size_index = segment_index + 1 
            segment_size = line1[1] 
            page_no = line1[2] 
            self.pm[segment_index] = segment_size 
            self.pm[segment_size_index] = page_no 
            line1_arr.append(line1[0])  
            line1_arr.append(line1[1]) 
            line1_arr.append(line1[2])        
            to_append = []
            to_page = self.recursive_lines(to_append, line1_arr, line2)
            if to_page != None:
                p_length = len(to_page)
                for j in range(0, p_length-1, 3):
                    pm_index = page_no * 512 + to_page[j+1] 
                    self.pm[pm_index] = to_page[j+2]
                return self.fill_pm(line1[3:], line2[p_length:])
            else:
                return
            
    def recursive_lines(self, to_append, line1, line):
        """recursive function that collects a list 
        of numbers belonging to the same segment"""
        if line == []:
            return to_append                             
        
        if line1[0] != line[0]:
            if to_append == []:
                return None
            else:
                return to_append
        else:          
            to_append.append(line[0])   
            to_append.append(line[1])   
            to_append.append(line[2])   
            return self.recursive_lines(to_append, line1, line[3:])    
  
    def open_file(self, filename):
        """opens the file, reads it, converst to list 
        and returns a list of binary numbers"""
        my_file = open(filename, "r")
        line_list = []
        for line in my_file:
            line_list += line.strip().split(" ")
        a_list = []
        for i in range(len(line_list)):
            an_int = int(line_list[i])
            a_list.append(an_int)
        return a_list

    def open_init_file(self, filename):
        """function that opens the initialization file 
        and returns a list of two lines"""
        my_file = open(filename, "r")
        line_list = []
        for line in my_file:
            a_line = line.strip().split()
            line_list.append(a_line)
        int_list = self.int_lists(line_list)
        return int_list

    def int_lists(self, line_list):
        """converst numbers in strings to integers"""
        one = line_list[0]
        two = line_list[1]
        one_i_list = []
        two_i_list = []
        for i in range(len(one)):
            temp = int(one[i])
            one_i_list.append(temp)
        for j in range(len(two)):
            temp = int(two[j])
            two_i_list.append(temp)
        return one_i_list, two_i_list   

    def binary_list(self, va_list):
        """funcion that calls the decimal to binary function 
        and creates a list of binary numbers"""
        bin_va_list = []
        for j in range(len(va_list)):
            bin_va = self.dec_to_bin(va_list[j])
            bin_va_list.append(bin_va)
        return bin_va_list

    def binary_to_decimal(self, binary): 
        """converts binary to decimal"""
        binary1 = binary 
        decimal, i, n = 0, 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        return decimal    

    def split_va(self, va_list):
        """splits the va list into s p and w"""     
        spw_list = []
        for i in range(len(va_list)):   
            spw_four = []
            va_listy = va_list[i]      
            lengd = len(va_listy)
            str_va_list = str(va_listy).strip("[")
            str_va_list = str_va_list.strip("]")

            if lengd < 27:
                adds = 27-lengd
                str_adds = "0"*adds
                va_strings = str_adds + str_va_list

            s = int(va_strings[0:9])
            p = int(va_strings[9:18])
            w = int(va_strings[18:27])
            pw = int(va_strings[9:27])

            sd = self.binary_to_decimal(s)
            pd = self.binary_to_decimal(p)
            wd = self.binary_to_decimal(w)
            pwd = self.binary_to_decimal(pw)

            spw_four.append(sd)
            spw_four.append(pd)
            spw_four.append(wd)
            spw_four.append(pwd)
            spw_list.append(spw_four)

        return spw_list    

    def dec_to_bin(self, my_int):
        """"converts decimals to integers"""
        a_str = ''
        my_quota = my_int
        while 0 < my_int:
            quota = my_int // 2
            the_rest = my_int % 2  
            a_str = str(the_rest) + a_str
            my_int = quota           
        if my_quota == 0:
            a_str = '0'
        return a_str

    def find_pa(self, spw_list):
        """identifies the physical address in the array"""
        pa_list = []
        for row in spw_list:
            pm = self.pm
            s = row[0]
            p = row[1]
            w = row[2]
            pw = row[3]
            if pw >= pm[2*s]:
                pa_list.append(-1)
            else:
                pa = pm[pm[2*s+1]*512+p]*512 + w
                pa_list.append(pa)
        self.add_to_file(pa_list)
    
    def add_to_file(self, pa_list):
        """writes the output to a txt file"""
        my_pa_file = open("output-no-dp.txt", "w")
        for i in pa_list:
            str_i = str(i) + " "
            my_pa_file.write(str_i)
        my_pa_file.close()

def main():
    vmm = VMmanager()

    inital_filename = "init-no-dp.txt"
    init_list = vmm.open_init_file(inital_filename)
    line1 = init_list[0]
    line2 = init_list[1]
    vmm.fill_pm(line1, line2)
    
    va_filename = "input-no-dp.txt"
    va_list = vmm.open_file(va_filename)
    va_bin = vmm.binary_list(va_list)
    spw_list = vmm.split_va(va_bin) 
    vmm.find_pa(spw_list)
  
main()
