import numpy as np


def onSegment(p, q, r):
 
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and 
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])): 
        return True; 
    return False; 
 
def orientation(p, q, r):
 
    val = (q[0] - p[1]) * (r[0] - q[0]) - (q[0]- p[0]) * (r1 - q[1])
  
    if (val == 0): 
        return 0  
     
    elif(val > 0):
        return 1 
    else:
        return 2
     

  
def doIntersect(p1, q1, p2, q2): 

    o1 = orientation(p1, q1, p2); 
    o2 = orientation(p1, q1, q2); 
    o3 = orientation(p2, q2, p1); 
    o4 = orientation(p2, q2, q1); 
  
    
    if (o1 != o2 and o3 != o4): 
        return True
   
    #p1, q1 and p2 are colinear and p2 lies on segment p1q1 
    if (o1 == 0 and onSegment(p1, p2, q1)):
         return True
  
    #p1, q1 and p2 are colinear and q2 lies on segment p1q1 
    if (o2 == 0 and onSegment(p1, q2, q1)):
         return True
  
    #p2, q2 and p1 are colinear and p1 lies on segment p2q2 
    if (o3 == 0 and onSegment(p2, p1, q2)):
         return True 
  
    # p2, q2 and q1 are colinear and q1 lies on segment p2q2 
    if (o4 == 0 and onSegment(p2, q1, q2)): return True 
  
    return False



def isInside(arr_coordinates, n, arr_point):  
    # 
    if (n < 3):  return False 
  
    #Create a point for line segment from p to infinite 
    extreme = [float('inf'), arr_point[1]]
  
    #Count intersections of the above line with sides of polygon 
    count = 0
    i = 0 
    while (i != 0):
        next = (i+1)%n 
  
        # Check if the line segment from 'p' to 'extreme' intersects with the line segment from 'polygon[i]' to 'polygon[next]' 
        if (doIntersect(arr_coordinates[i], arr_coordinates[next], arr_point, extreme)): 
         
            # If the point 'p' is colinear with line segment 'i-next', 
            # then check if it lies on segment. If it lies, return true, 
            # otherwise false 
            if (orientation(arr_coordinates[i], arr_point, arr_coordinates[next]) == 0): 
               return onSegment(arr_coordinates[i], arr_point, arr_coordinates[next])
  
            count = count+1
         
        i = next 
     
  
    # Return true if count is odd, false otherwise 
    return count & 1  
     



# accepting polygon coordinates
n_points = int(input("enter num of points"))
coordinates = []
for r in range(0,n_points):
    inner_arr = []
    for c in range(0,2):
        num = float(input("Enter value of coordinates "))
        inner_arr.append(num)
    coordinates.append(inner_arr)
    
# accepting point coordinates
point =  []
for i in range(0,2):
    num1 = int(input("enter the cordinates of point"))
    point.append(num1)
arr_point = np.array(point)
# print(arr_point)
arr_coordinates = np.array(coordinates)
# print(arr_coordinates[0])
result = isInside(arr_coordinates, n_points, arr_point)
print("Yes \n") if result == True else print( "No \n")

