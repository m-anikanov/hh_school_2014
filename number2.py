
array = [2,3,4,5,6];
debug = False;
equalTo = 100;

helpArray = [];
equalFlag = False;
for i in range(len(array)):  
  helpArray.append(0)


def recursion (iteration,deep):
  global equalFlag;
  
  if iteration<deep:
    fnNumber = 1 if iteration == 0 else 2;
    
    while helpArray[iteration] < fnNumber:
      
      if iteration+1 == deep:
        left = 0;
        right = 0;
        total = 0;
        leftPrint='';
        rightPrint='';
        debugStr = '';
        for (i, el) in enumerate(helpArray):
          debugStr = debugStr + ' '+ str(el);
          if el == 0:
            left = left+array[i];
            total = total + array[i];
            leftPrint = leftPrint + str(array[i]) + ' ';
          else:
            right = right+array[i];
            rightPrint = rightPrint + str(array[i]) + ' ';
        if debug:
          print debugStr;
          
        if total == equalTo:
          equalFlag = True;
        if left == right:
          print leftPrint+'- '+rightPrint;
          
          

      recursion(iteration+1,deep);
      
      
      helpArray[iteration] = helpArray[iteration] + 1;
    helpArray[iteration] = 0;
    


recursion(0,len(array));       

print 'yes' if equalFlag else 'no';

        