from itertools import count


listaUsuarios=[{1},{3},{4},{56},{8},{4},{3},{2},{5},{7},{8},{4},{2},{9},{6}]

def total_elements(listaUsuarios):
    count = 1
    for i in listaUsuarios:
        count += 1
    return count

print("The total number of elements in the list: ", total_elements(listaUsuarios))