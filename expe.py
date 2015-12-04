import fun
mainfolder="folder"
conditions =["condition1", "condition2"]
row = 0
column = 2
expe1 = fun.Expe(mainfolder, conditions, row, column)
#expe1.get_items()
#expe1.laten()
expe1.to_csv('output.csv')
