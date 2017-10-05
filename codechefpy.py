#python codechef
  n = input()
   l = []
   
 for i in range(1,n):

       d=0
       d = input()
       l.extend(d)
       i++
    
         for i in range(1,n):

             j=1
             fact = 1
             while(j < l[i]):

               fact *= j
               j++

               print(fact)

            i++   