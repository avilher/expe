
import os
import string
import csv
class Expe():
    def __init__(self, mainfolder, condiciones, n_lin, n_col):
        self.mainfolder = mainfolder
        self.condiciones = condiciones
        self.n_lin = n_lin
        self.n_col = n_col

    def get_items(self):
        ff=os.listdir(self.mainfolder)
        items = set()
        
        for g in ff:
            try:
                s=os.listdir(self.mainfolder+g)
                for i in self.condiciones:
                    for n in s:
                        
                        nn=string.split(n,'_')
                        
                        items.add(nn[1]+','+i)
            except OSError:
    			pass
        print items
        return list(items)
                    
        
    def laten(self):
        items = self.get_items()
        items.insert(0,'items,conditions')
        ff=os.listdir(self.mainfolder)#listado de los carpetas de sujetos en esta carpeta
    #por cada sujeto    
        todo = [] 
        
        for g in ff:
            
            suj=[]
            try:
                #intenta crear un listado de los archivos de estimulos
                s=os.listdir(self.mainfolder+g)
                
                for j in items:
                    jj=j.split(',')
                    
                        
                        #por cada archivo
                    for n in s:
                        if (jj[0] in n) and (jj[1] in n):
                                
                            f=open(self.mainfolder+g+"/"+n,"rb")
                            c=f.readlines()
                            cc=string.split(c[self.n_col])
                            ccc=cc[self.n_lin]
                            suj.append(ccc)
    				
    
    		#print suj
    			#exc(g,suj)
            except OSError:
                pass
                    
            if suj:
                suj.insert(0,g)
                todo.append(suj)
        todo.append(items)
        print todo
        return todo
    def to_csv(self, file_output):
        todo = self.laten()
        length = len(todo[0])
        f = open(file_output, 'wb')
        csv_writer = csv.writer(f)
        for y in range(length):
            csv_writer.writerow([x[y] for x in todo])
