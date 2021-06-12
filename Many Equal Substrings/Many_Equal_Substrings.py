def Many_Equal_Substrings():
   N,times = map(int,input().split())
   string = input()
   same_words_count = 0   
   word = 1
  
   while word < N:
       if string[word:] == string[:N-word]:
           same_words_count = N-word
           break
           
       word += 1
   output_string = string
   output_string += string[same_words_count:]*(times-1)
   return output_string
   
       
       
            
reamined_test_cases = 1         
# reamined_test_cases = int(input())
while reamined_test_cases > 0:
    print(Many_Equal_Substrings())
    reamined_test_cases -= 1 
