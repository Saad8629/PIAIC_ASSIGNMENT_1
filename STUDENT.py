verifyage=False
verifyname=False

while verifyage==False or verifyname==False:
    
  name=str(input('PLEASE ENTER THE NAME\n'))
  
      
  age=int(input('PLEASE ENTER THE AGE\n'))
  if not type(name)==str or type(age)!=int :
    print('INVALID cridentials\n')
  elif type(name)==str and name.strip() and type(age)==int:
    verifyname=True

    verifyage=True
   
  if verifyname==True and verifyage==True:
      print ('NAME',' ',name)
      print ('AGE',' ',age)
      break
      
      
      
