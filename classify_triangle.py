def classify_triangle(a,b,c):
    result = ""
    if(isinstance(a,int) or (isinstance(a, float))):
        if(isinstance(b,int) or (isinstance(b, float))):
            if(isinstance(c,int) or (isinstance(c, float))):
                if(a<=0 or b <= 0 or c <= 0):
                    result = "Cannot have values of zero or negative"
                    return result
                #check for equilateral
                if(a == b == c):
                    result = result + "This triangle is equilateral"
                #check for isosceles
                elif(a==b or b==c or a==c):
                    result = result + "This triangle is isosceles"
                #scalene
                else:
                    result = result + "This triangle is scalene"
                #check for right triangle
                if(round(a*a,2) + round(b*b,2) == round(c*c,2)):
                    result = result + " this triangle is also a right triangle"
                

                
            else: 
                result = "Please set parameter c to be an integer or float"
        else:
            result = "Please set parameter b to be an integer or float"
    else:
        result = "Please set parameter a to be an integer or float"
    return result