def maior_primo(n):
    i = 2
    j = 1
    ok = 0
    primo = True
    while i < n:
        while primo:
            if i > n:
                return p
                primo = False
            if i == 2:
                i = i + 1
            if i % j == 0:
                j = j + 1
                ok = ok + 1
            else:
                j = j + 1
            if j == i:
                p = i
                j = 1
                ok = 0
                i = i + 1
            if ok > 1:
                ok = 0 
                j = 1
                i = i + 1
                
                
    
            
    
        
            

