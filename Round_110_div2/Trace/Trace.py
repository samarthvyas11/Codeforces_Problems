def question2():

    number_of_circles = int(input())
    radius_of = list(map(int,input().split()))
    radius_of.sort(reverse = True)
    red_area = 0
    circle = 0
    pie = 3.1415926536

    while circle < number_of_circles:
        if circle+1 < number_of_circles:
           red_area += pie*(radius_of[circle]**2 - radius_of[circle+1]**2)
           circle += 2 
        else:
            red_area += pie*(radius_of[circle]**2)
            circle += 1
        
         
    return red_area    


# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0:
    print(question2())
    remained_test_cases -= 1 