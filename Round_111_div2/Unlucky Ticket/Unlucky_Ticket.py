def question2():
    total_digits = int(input())
    digits = input()
    digits = list(digits)
    first_half = digits[:total_digits]
    second_half = digits[total_digits:]
    first_half.sort()
    second_half.sort()
    unlucky = True

    if first_half[0] > second_half[0]:

        for digit in range(total_digits):
            if first_half[digit] <= second_half[digit]:
                unlucky = False
                return "NO"

    else:

        for digit in range(total_digits):
            if first_half[digit] >= second_half[digit]:
                unlucky = False
                return "NO"
    if unlucky:
        return "YES"
        
        
# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0:
    print(question2())
    remained_test_cases -= 1 