def rev_list(org_list):
    new_list=[]
    while org_list:
        new_list.append(org_list.pop(-1))

    return new_list

sett=input("Enter list elements seperating with commas: ").split(',')

print (rev_list(sett))