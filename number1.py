import math

array = [[10,10],[20,10],[20,15]];
debug = False;


min = array[0];

i = 1;
while i<len(array):
  el1 = array[i-1];
  j = i;
  
  while j<len(array):
    el2 = array[j];  
    length = math.sqrt( math.pow( (el1[0] - el2[0]), 2 ) +  math.pow( (el1[1] - el2[1]) , 2 ) );
    j=j+1;
    if debug:
      print el1;
      print el2;
      print length;
    if length < min:
      min = length
    
  i=i+1;

if min.is_integer():
  min = int(min);
  
print min;