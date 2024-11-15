def indices_cible(T,a):
    for i in range(len(T)):
        B=T[i]
        for j in range(i+1,len(T)):
            if a==B+T[j]:
                return(f'the indices are {i} and {j}')
               # break 
