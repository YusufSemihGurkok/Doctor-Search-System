from doctor import Doctor

def bubble_sort(doctor_list) :
    """
    sorts the doctors according to their hospital name and specialty
    
    Parameters:
        doctor_list(list): a list of Doctor objects
    Return:
        doctor_list(list): sorted list of Doctor objects
    
    """
    issorted = False;
    a = 0
    while(a < len(doctor_list)-1 and not issorted):
        issorted = True;
        for k in range(len(doctor_list)-a-1):   
              if doctor_list[k].get_hospital()> doctor_list[k+1].get_hospital():
                     issorted = False
                     temp = doctor_list[k]
                     doctor_list[k] = doctor_list[k+1]
                     doctor_list[k+1] = temp
              elif  doctor_list[k].get_hospital() == doctor_list[k+1].get_hospital() and doctor_list[k].get_specialty()> doctor_list[k+1].get_specialty():
                     issorted = False
                     temp = doctor_list[k]
                     doctor_list[k] = doctor_list[k+1]
                     doctor_list[k+1] = temp
        
        a += 1
         
    return doctor_list

def binary_search(lis,doctorid,start,end):
    '''
    a recursive function return the index of the doctor with the given id or -1 if the doctor
    does not exist in the list.

    Parameters:
        lis(list): a list of Doctor objects
        doctorid(int): Input an id from the user
        start(int): starting index of the list to be searched
        end(int): ending index of the list to be searched
    Return:
        lis[mid](object): Doctor object

    '''
    if start> end:
        return -1
    else:
        mid = (start + end)//2
        if int(lis[mid].get_doctor_id()) == doctorid:
            return lis[mid]
        elif int(lis[mid].get_doctor_id())  > doctorid:
            return binary_search(lis,doctorid,start,mid-1)
        else:
            return binary_search(lis,doctorid,mid+1,end)
    
def read_doctors(infile):
    '''
    takes a file name as parameter, and using the file data, creates a list of Doctor
    objects from the data in the input file and returns the Doctor list
    
    Parameters:
        infile(string): input file
    Return:
        lis(list): a list of Doctor objects

    '''
    x = open(infile,'r')
    lis = []
    for i in x:
        data = i.strip().split(';')
        doc = Doctor(data[0],data[1],data[2],data[3])
        lis.append(doc)
    return lis

a = read_doctors('doctors.txt')
a.sort()    
idnum = int(input('Enter id of doctor to search: '))
if binary_search(a, idnum, 0,len(a) ) == -1:
    print('No such doctor')
else:
    print('Doctor with id' , idnum)
    print(binary_search(a, idnum, 0, len(a)-1))
    
print('Doctors by Hospital and Specialty:')
for i in bubble_sort(a):
    print(i)

