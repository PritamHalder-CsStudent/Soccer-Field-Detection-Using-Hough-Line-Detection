import cv2
import numpy as np
import random
import math

def find_intersections(lines):
    intersections = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            line1 = lines[i]
            line2 = lines[j]
            x1, y1, x2, y2 = line1[0]
            x3, y3, x4, y4 = line2[0]
            denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if denominator != 0:
                x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
                y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator
                intersections.append((int(x), int(y)))
    return intersections

def main():
    # Load the football field image
    image = cv2.imread('samout1.png')

    #Canny
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    # Apply Hough line transformation to detect lines
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, None, 50, 20)

    # Find intersection points
    intersections = find_intersections(lines)

    # Draw lines and intersection points on the image
    font = cv2.FONT_HERSHEY_SIMPLEX

    ori_points = []
    k = 1
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
        if k<=2:
            if abs(angle) < 20:
                # Horizontal line
                cv2.line(image, (x1, y1), (x2, y2), (0,255 , 255), 2)
            else:
                cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)    
                if(k%2!=0):
                    ori_points.append((int(x1),int(y1)))
                    ori_points.append((int(x2),int(y2)))
                    k=k+1
                else:
                    ori_points.append((int(x2),int(y2)))
                    ori_points.append((int(x1),int(y1)))
             
                    k=k+1       

    for point in intersections:
        cv2.circle(image, point, 5, (0, 0, 255), -1)

    # Display the image with lines and intersection points
    cv2.imshow('Football Field', image)
    cv2.imwrite('sam_out10.jpg',image)
    print(ori_points)
    
    #Saving Line Co-ordinates
    with open('outputco1.txt', 'w') as file:
        # Step 2: Convert the list elements to strings
        str_list = [str(element) for element in ori_points]
        
        # Step 3: Join the list elements into a single string
        list_string = '\n'.join(str_list)  # Separate elements by a new line
        
        # Step 4: Write the string to the file
        file.write(list_string)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()