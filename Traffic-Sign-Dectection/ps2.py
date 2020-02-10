"""
CS6476 Problem Set 2 imports. Only Numpy and cv2 are allowed.
"""
import cv2
import math
import numpy as np


def traffic_detect(img_in, radii_range):
    temp_img = np.copy(img_in)
    img_gray   = cv2.cvtColor(temp_img,cv2.COLOR_BGR2GRAY)
    # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    # filtered_img = cv2.filter2D(img_gray, -1, kernel)
    blur = cv2.medianBlur(img_gray, 7)
    # cv2.imshow('detected circles',blur)
    # cv2.waitKey(0)
    minr = radii_range[0]
    maxr = radii_range[-1]+1
    print (minr, maxr, radii_range)

    # print("minr and maxr", minr, maxr)
    # edges = cv2.Canny(img_gray, 25, 150, apertureSize=5)
    # cv2.imshow('detected circles',edges)
    # cv2.waitKey(0)
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, \
                            param1=20, param2=10, \
                            minRadius=minr, maxRadius=maxr)

    if (circles is None):
        print (circles)
        return None
    
    # Remove outliers by comparing radius of circles, big circles will be removed
    max_radius = 0
    remove_element = 0
    if (len(circles[0]) >= 2):
        print ("before ", circles)
        circles = np.uint16(np.around(circles))
        # while (len(circles[0]) > 3):
        #     for i in range(len(circles[0])):
        #         if (max_radius < circles[0][i][2]):
        #             max_radius = circles[0][i][2]
        #             remove_element = i
            
        #     circles = np.delete(circles[0], remove_element, 0)
        # else:
        circles = circles[0]
        
        circMap = {}
        count = 0
        ind = []
        index = 0
        for circle in circles:
            res = circMap.get(circle[0])
            if (res is None):
                ind = [index, 1]
                circMap[circle[0]] = ind
            else:
                num = res[1] + 1
                ind = [index, num]
                circMap[circle[0]] = ind
            index +=1
        print (circMap)
        for values in circMap.values():
            if (values[1] == 1):
                circles = np.delete(circles, values[0], 0)
        sumx = 0
        sumy = 0


        # for circle in circles:
            # print ("circle 0 ", circle[0])
            # cv2.circle(img_in, (circle[0][0], circle[0][1]))
            # cv2.circle(img_in,(circle[0], circle[1]),10,(255,0,0),3)
        # cv2.imshow('circles',img_in)
        # cv2.waitKey(0)
        for circle in circles:
            print("circle", circle)
            sumx += circle[0]
            sumy += circle[1]
        
        center_cir = ((int(sumx / len(circles))), (int(sumy / len(circles))))
        # print (center_cir)
        # Get light with highest lums value
        hls = cv2.cvtColor(img_in, cv2.COLOR_BGR2HLS)
        index = 0
        count = 0
        x = 0
        y = 0
        lum=0

        for cir in circles:
            # print (cir[0], cir[1])
            x = cir[0]
            y = cir[1]
            # lum_value=hls[y][x]
            if hls[y][x][1] > lum:
                lum=hls[y][x][1]
                index = count
            count += 1


        if index == 0:
            # print ((x,y), 'red')
            cv2.circle(img_in,(center_cir[0],center_cir[1]),1,(255,0,0),3)
            # cv2.imshow('red circles',img_in)
            # cv2.waitKey(0)
            
            return (center_cir[0],center_cir[1]), 'red'
        elif index == 1:
            # print ((x,y), 'yellow')
            cv2.circle(img_in,(center_cir[0],center_cir[1]),1,(255,0,0),3)
            # cv2.imshow('yellow circles',img_in)
            # cv2.waitKey(0)
            return (center_cir[0],center_cir[1]), 'yellow'
            
        elif index == 2:
            # print ((x,y), 'green')
            cv2.circle(img_in,(center_cir[0],center_cir[1]),1,(255,0,0),3)
            # cv2.imshow('green circles',img_in)
            # cv2.waitKey(0)
            return (center_cir[0],center_cir[1]), 'green'
    # print ("highest lum is in ", indec)
    else:
        return None


def traffic_light_detection(img_in, radii_range):
    """Finds the coordinates of a traffic light image given a radii
    range.

    Use the radii range to find the circles in the traffic light and
    identify which of them represents the yellow light.

    Analyze the states of all three lights and determine whether the
    traffic light is red, yellow, or green. This will be referred to
    as the 'state'.

    It is recommended you use Hough tools to find these circles in
    the image.

    The input image may be just the traffic light with a white
    background or a larger image of a scene containing a traffic
    light.

    Args:
        img_in (numpy.array): image containing a traffic light.
        radii_range (list): range of radii values to search for.

    Returns:
        tuple: 2-element tuple containing:
        coordinates (tuple): traffic light center using the (x, y)
                             convention.
        state (str): traffic light state. A value in {'red', 'yellow',
                     'green'}
    """
    
    temp_img = np.copy(img_in)
    img_gray   = cv2.cvtColor(temp_img,cv2.COLOR_BGR2GRAY)
    # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    # filtered_img = cv2.filter2D(img_gray, -1, kernel)
    # blur = cv2.medianBlur(img_gray, 7)
    # cv2.imshow('detected circles',blur)
    # cv2.waitKey(0)
    minr = radii_range[0]
    maxr = radii_range[-1]+1
    print (minr, maxr, radii_range)

    # print("minr and maxr", minr, maxr)
    # edges = cv2.Canny(img_gray, 25, 150, apertureSize=5)
    # cv2.imshow('detected circles',edges)
    # cv2.waitKey(0)
    circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, 50, \
                            param1=20, param2=10, \
                            minRadius=minr, maxRadius=maxr)

    if (circles is None):
        print (circles)
        return None
    
    # Remove outliers by comparing radius of circles, big circles will be removed
    max_radius = 0
    remove_element = 0
    if (len(circles[0]) >= 2):
        # print ("before ", circles)
        circles = np.uint16(np.around(circles))
        # while (len(circles[0]) > 3):
        #     for i in range(len(circles[0])):
        #         if (max_radius < circles[0][i][2]):
        #             max_radius = circles[0][i][2]
        #             remove_element = i
            
        #     circles = np.delete(circles[0], remove_element, 0)
        # else:
        circles = circles[0]
        
        circMap = {}
        count = 0
        ind = []
        index = 0
        for circle in circles:
            res = circMap.get(circle[0])
            if (res is None):
                ind = [index, 1]
                circMap[circle[0]] = ind
            else:
                num = res[1] + 1
                ind = [index, num]
                circMap[circle[0]] = ind
            index +=1
        print (circMap)
        for values in circMap.values():
            if (values[1] == 1):
                circles = np.delete(circles, values[0], 0)
        sumx = 0
        sumy = 0


        # for circle in circles:
            # print ("circle 0 ", circle[0])
            # cv2.circle(img_in, (circle[0][0], circle[0][1]))
            # cv2.circle(img_in,(circle[0], circle[1]),10,(255,0,0),3)
        # cv2.imshow('circles',img_in)
        # cv2.waitKey(0)
        for circle in circles:
            # print("circle", circle)
            sumx += circle[0]
            sumy += circle[1]
        
        center_cir = ((int(sumx / len(circles))), (int(sumy / len(circles))))
        # print (center_cir)
        # Get light with highest lums value
        hls = cv2.cvtColor(img_in, cv2.COLOR_BGR2HLS)
        index = 0
        count = 0
        x = 0
        y = 0
        lum=0

        for cir in circles:
            # print (cir[0], cir[1])
            x = cir[0]
            y = cir[1]
            # lum_value=hls[y][x]
            if hls[y][x][1] > lum:
                lum=hls[y][x][1]
                index = count
            count += 1


        if index == 0:
            # print ((x,y), 'red')
            # cv2.circle(img_in,(center_cir[0],center_cir[1]),1,(255,0,0),3)
            # cv2.imshow('red circles',img_in)
            # cv2.waitKey(0)
            
            return (center_cir[0],center_cir[1]), 'red'
        elif index == 1:
            # print ((x,y), 'yellow')
            # cv2.circle(img_in,(center_cir[0],center_cir[1]),1,(255,0,0),3)
            # cv2.imshow('yellow circles',img_in)
            # cv2.waitKey(0)
            return (center_cir[0],center_cir[1]), 'yellow'
            
        elif index == 2:
            # print ((x,y), 'green')
            # cv2.circle(img_in,(center_cir[0],center_cir[1]),1,(255,0,0),3)
            # cv2.imshow('green circles',img_in)
            # cv2.waitKey(0)
            return (center_cir[0],center_cir[1]), 'green'
    # print ("highest lum is in ", indec)
    else:
        return None

def line_intersection(line1, line2):
    x1, y1, x2, y2 = line1[0][0], line1[0][1], line1[1][0], line1[1][1]
    x3, y3, x4, y4 = line2[0][0], line2[0][1], line2[1][0], line2[1][1]

    x_intersect = ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
    y_intersect = ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )

    return (x_intersect, y_intersect)


def yield_sign_detection(img_in):
    """Finds the centroid coordinates of a yield sign in the provided
    image.

    Args:
        img_in (numpy.array): image containing a traffic light.

    Returns:
        (x,y) tuple of coordinates of the center of the yield sign.
    """
    # cv2.imshow('Yield sign',img_in)
    # cv2.waitKey(0)

    # blur_img = cv2.medianBlur(img_in, 31)
    # cv2.imshow('Yield sign',img_in)
    # cv2.waitKey(0)

    hsv = cv2.cvtColor(img_in, cv2.COLOR_BGR2HSV)

    lower_red = np.array([-5,50,50]) #example value
    upper_red = np.array([12,255,255]) #example value

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # cv2.imshow('red mask', img_in)
    # cv2.imshow('mask', mask)
    # cv2.waitKey(0)

    edges = cv2.Canny(mask, 50, 150, apertureSize=3)
    # cv2.imshow('edges', edges)
    # cv2.waitKey(0)

    # lines = cv2.HoughLinesP(edges, .5, 5 * np.pi / 180, 0)

    # for line in lines:
        
    #     x1, y1, x2, y2 = line[0]
    #     print (x1, y1, x2, y2)
    #     cv2.line(img_in, (x1, y1), (x2, y2), (255,0,0), 2)

    lines = cv2.HoughLines(edges, 1, 5 * np.pi / 180, 40)
    lineList = []

    lineListDict = {}


    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho

        # print ("rho, theta", rho, theta, int(math.degrees(theta)))

        x1 = int(x0 + 1000 * (-b))

        y1 = int(y0 + 1000 * (a))

        x2 = int(x0 - 1000 * (-b))

        y2 = int(y0 - 1000 * (a))
        lineList.append([x1, y1, x2, y2])
        
        lineLs = []
        if ( 88 < int(math.degrees(theta)) < 92):
            lineLs.append([x1, y1, x2, y2, rho, theta])
            lineListDict["90"] = lineLs
        elif (148 < int(math.degrees(theta)) < 151):
            lineLs.append([x1, y1, x2, y2, rho, theta])
            lineListDict["150"] = lineLs
        elif (28 < int(math.degrees(theta)) < 32):
            lineLs.append([x1, y1, x2, y2, rho, theta])
            lineListDict["30"] = lineLs

        # cv2.line(img_in, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
        # print (x1, y1, x2, y2)

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho

        # print ("rho, theta", rho, theta, int(math.degrees(theta)))

        x1 = int(x0 + 1000 * (-b))

        y1 = int(y0 + 1000 * (a))

        x2 = int(x0 - 1000 * (-b))

        y2 = int(y0 - 1000 * (a))
        lineList.append([x1, y1, x2, y2])
        
        lineLs = []
        if ( 88 < int(math.degrees(theta)) < 92):
            check = lineListDict.get("90")
            if rho <= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                lineListDict["90"] = lineLs
        elif (148 < int(math.degrees(theta)) < 151):
            check = lineListDict.get("150")
            if rho >= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                lineListDict["150"] = lineLs
        elif (28 < int(math.degrees(theta)) < 32):
            check = lineListDict.get("30")
            if rho >= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                lineListDict["30"] = lineLs

        # cv2.line(img_in, (x1, y1), (x2, y2), (255, 0, 0), 2)        
    
    # print (lineListDict)

    lineListA = lineListDict.get("90")
    lineListB = lineListDict.get("150")
    lineListC = lineListDict.get("30")

    # print (lineListA, lineListB, lineListC)
    # print(lineList)
    # cv2.line(img_in, (lineListA[0][0], lineListA[0][1]), (lineListA[0][2], lineListA[0][3]), (255, 0, 0), 2)
    # cv2.line(img_in, (lineListB[0][0], lineListB[0][1]), (lineListB[0][2], lineListB[0][3]), (0, 255, 0), 2)
    # cv2.line(img_in, (lineListC[0][0], lineListC[0][1]), (lineListC[0][2], lineListC[0][3]), (255, 0, 0), 2)
    # print(((lineList[0][0], lineList[0][1]), (lineList[0][2], lineList[0][3])), (lineList[1][0], lineList[1][1]), (lineList[1][2], lineList[1][3]))
    if (lineListA is not None and lineListB is not None and lineListC is not None):
        x1,y1 = line_intersection(((lineListA[0][0], lineListA[0][1]), (lineListA[0][2], lineListA[0][3])), ((lineListB[0][0], lineListB[0][1]), (lineListB[0][2], lineListB[0][3])))
        # print(x1,y1)
        x2,y2 = line_intersection(((lineListB[0][0], lineListB[0][1]), (lineListB[0][2], lineListB[0][3])), ((lineListC[0][0], lineListC[0][1]), (lineListC[0][2], lineListC[0][3])))
        # print(x2,y2)
        x3,y3 = line_intersection(((lineListA[0][0], lineListA[0][1]), (lineListA[0][2], lineListA[0][3])), ((lineListC[0][0], lineListC[0][1]), (lineListC[0][2], lineListC[0][3])))
        # print(x3,y3)

        centX = int((x1+x2+x3) / 3)
        centY = int((y1+y2+y3) / 3)

        print ((centX, centY))
        # cv2.circle(img_in,(centX, centY),1,(255,0,0),3)


        # cv2.imshow('image', img_in)
        # cv2.waitKey(0)
        # raise NotImplementedError
        return (centX, centY)
    else:
        return None


def stop_sign_detection(img_in):
    """Finds the centroid coordinates of a stop sign in the provided
    image.

    Args:
        img_in (numpy.array): image containing a traffic light.

    Returns:
        (x,y) tuple of the coordinates of the center of the stop sign.
    """
    blur_img = cv2.medianBlur(img_in, 27)
    # cv2.imshow('Do not enter sign',blur_img)
    # cv2.waitKey(0)
    hsv = cv2.cvtColor(blur_img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,43,46]) #example value
    upper_red = np.array([6,255,230]) #example value

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # cv2.imshow('red mask', img_in)
    # cv2.imshow('mask', mask)
    # cv2.waitKey(0)

    

    # gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(mask, 50, 150, apertureSize=3)
    # cv2.imshow('edges', edges)
    # cv2.waitKey(0)
    # lines = cv2.HoughLines(edges, 1, 5 * np.pi / 180, 40)
    # 

    minr, maxr = 10, 70
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 50, \
                            param1=20, param2=10, \
                            minRadius=minr, maxRadius=maxr)

    # print ("before circles", circles)
    circles = np.uint16(np.around(circles))
    # print ("circles", circles)
    return (circles[0, 0][0], circles[0, 0][1])

    
    # print("lines", lines)

    # for line in lines:
    #     x1, y1, x2, y2 = line[0]
    #     cv2.line(img_in, (x1, y1), (x2, y2), (255,0,0), 2)

    # for line in lines:
    #     rho, theta = line[0]
    #     a = np.cos(theta)
    #     b = np.sin(theta)
    #     x0 = a * rho
    #     y0 = b * rho

    #     x1 = int(x0 + 1000 * (-b))

    #     y1 = int(y0 + 1000 * (a))

    #     x2 = int(x0 - 1000 * (-b))

    #     y2 = int(y0 - 1000 * (a))

    #     cv2.line(img_in, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # cv2.imshow('image', img_in)
    # cv2.waitKey(0)

    raise NotImplementedError




# print line_intersection((A, B), (C, D))


def warning_sign_detection(img_in):
    """Finds the centroid coordinates of a warning sign in the
    provided image.

    Args:
        img_in (numpy.array): image containing a traffic light.

    Returns:
        (x,y) tuple of the coordinates of the center of the sign.
    """
    # cv2.imshow('Warning sign',img_in)
    # cv2.waitKey(0)

    hsv = cv2.cvtColor(img_in, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([26,43,46])
    upper_orange = np.array([41,255,255]) 
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # cv2.imshow('red mask', img_in)
    # cv2.imshow('warning mask', mask)
    # cv2.waitKey(0)

      # gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(mask, 50, 150, apertureSize=3)
    # cv2.imshow('edges', edges)
    # cv2.waitKey(0)
    lines = cv2.HoughLines(edges,1, 5* np.pi/180, threshold = 40)
    # print(lines)

    lineList = []
    lineListDict = {}
    if (lines is not None):
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho

            # print ("rho, theta", rho, theta, int(math.degrees(theta)))

            x1 = int(x0 + 1000 * (-b))

            y1 = int(y0 + 1000 * (a))

            x2 = int(x0 - 1000 * (-b))

            y2 = int(y0 - 1000 * (a))
            # lineList.append([x1, y1, x2, y2])
            lineLs = []
            checkDict = {}
            if ( 42 < int(math.degrees(theta)) < 46):
                # check = lineListDict.get("44")
                # if rho <= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                if (lineListDict.get("A") is not None):
                    checkDict = lineListDict.get("A")    
                checkDict[rho] = lineLs
                lineListDict["A"] = checkDict
            elif (133 < int(math.degrees(theta)) < 137):
                # check = lineListDict.get("150")
                # if rho >= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                if (lineListDict.get("B") is not None):
                    checkDict = lineListDict.get("B")
                checkDict[rho] = lineLs
                lineListDict["B"] = checkDict


            # cv2.line(img_in, (x1, y1), (x2, y2), (255, 0, 0), 2)  
        
        angleA = lineListDict.get("A")
        angleB = lineListDict.get("B")

        sortA = sorted(angleA.keys())
        sortB = sorted(angleB.keys())

        # print (sortA)
        # print (sortB)

        lineA1 = angleA.get(sortA[0])
        lineA2 = angleA.get(sortA[2])

        lineB1 = angleB.get(sortB[0])
        lineB2 = angleB.get(sortB[2])
        # print(int((lineA1[0][2] + lineA2[0][2]) / 2), int((lineA1[0][3] + lineA2[0][3]) / 2))

        lineAa = (int((lineA1[0][0] + lineA2[0][0]) / 2), (int((lineA1[0][1] + lineA2[0][1]) / 2)))
        lineAb = (int((lineA1[0][2] + lineA2[0][2]) / 2), (int((lineA1[0][3] + lineA2[0][3]) / 2)))

        lineBa = (int((lineB1[0][0] + lineB2[0][0]) / 2), (int((lineB1[0][1] + lineB2[0][1]) / 2)))
        lineBb = (int((lineB1[0][2] + lineB2[0][2]) / 2), (int((lineB1[0][3] + lineB2[0][3]) / 2)))

        # print(lineAa, lineAb, lineBa, lineBb)
        x,y = line_intersection((lineAa, lineAb), (lineBa,lineBb))

        # cv2.circle(img_in,(int(x), int(y)),1,(0,0,255),3)

        return (int(x), int(y))
    else:
        return None

def construction_sign_detection(img_in):
    """Finds the centroid coordinates of a construction sign in the
    provided image.

    Args:
        img_in (numpy.array): image containing a traffic light.

    Returns:
        (x,y) tuple of the coordinates of the center of the sign.
    """
    hsv = cv2.cvtColor(img_in, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([12,41,47])
    upper_orange = np.array([25,255,255]) 
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(mask, 50, 150, apertureSize=3)
    # lines = cv2.HoughLines(edges,1, 5* np.pi/180, threshold = 40)
    # print(lines)

        #print(lines)

    lines = cv2.HoughLines(edges,1, 5* np.pi/180, threshold = 40)
    # print(lines)

    lineList = []
    lineListDict = {}
    if (lines is not None):
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho

            # print ("rho, theta", rho, theta, int(math.degrees(theta)))

            x1 = int(x0 + 1000 * (-b))

            y1 = int(y0 + 1000 * (a))

            x2 = int(x0 - 1000 * (-b))

            y2 = int(y0 - 1000 * (a))
            # lineList.append([x1, y1, x2, y2])
            lineLs = []
            checkDict = {}
            if ( 42 < int(math.degrees(theta)) < 46):
                # check = lineListDict.get("44")
                # if rho <= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                if (lineListDict.get("A") is not None):
                    checkDict = lineListDict.get("A")    
                checkDict[rho] = lineLs
                lineListDict["A"] = checkDict
            elif (133 < int(math.degrees(theta)) < 137):
                # check = lineListDict.get("150")
                # if rho >= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                if (lineListDict.get("B") is not None):
                    checkDict = lineListDict.get("B")
                checkDict[rho] = lineLs
                lineListDict["B"] = checkDict


            # cv2.line(img_in, (x1, y1), (x2, y2), (255, 0, 0), 2)  
        
        angleA = lineListDict.get("A")
        angleB = lineListDict.get("B")

        sortA = sorted(angleA.keys())
        sortB = sorted(angleB.keys())

        # print (sortA)
        # print (sortB)

        lineA1 = angleA.get(sortA[0])
        lineA2 = angleA.get(sortA[2])

        lineB1 = angleB.get(sortB[0])
        lineB2 = angleB.get(sortB[2])
        # print(int((lineA1[0][2] + lineA2[0][2]) / 2), int((lineA1[0][3] + lineA2[0][3]) / 2))

        lineAa = (int((lineA1[0][0] + lineA2[0][0]) / 2), (int((lineA1[0][1] + lineA2[0][1]) / 2)))
        lineAb = (int((lineA1[0][2] + lineA2[0][2]) / 2), (int((lineA1[0][3] + lineA2[0][3]) / 2)))

        lineBa = (int((lineB1[0][0] + lineB2[0][0]) / 2), (int((lineB1[0][1] + lineB2[0][1]) / 2)))
        lineBb = (int((lineB1[0][2] + lineB2[0][2]) / 2), (int((lineB1[0][3] + lineB2[0][3]) / 2)))

        # print(lineAa, lineAb, lineBa, lineBb)
        x,y = line_intersection((lineAa, lineAb), (lineBa,lineBb))

        # cv2.circle(img_in,(int(x), int(y)),1,(0,0,255),3)

        return (int(x), int(y))
    else:
        return None


def do_not_enter_sign_detection(img_in):
    """Find the centroid coordinates of a do not enter sign in the
    provided image.

    Args:
        img_in (numpy.array): image containing a traffic light.

    Returns:
        (x,y) typle of the coordinates of the center of the sign.
    """

    # cv2.imshow('Do not enter sign',img_in)
    # cv2.waitKey(0)
    hsv = cv2.cvtColor(img_in, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,20,220])
    upper_red = np.array([0,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    minr, maxr = 10, 50
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 50, \
                            param1=20, param2=10, \
                            minRadius=minr, maxRadius=maxr)

    # print ("before circles", circles)
    circles = np.uint16(np.around(circles))
    # print ("Circles", (circles[0, 0][0], circles[0, 0][1]))

    return (circles[0, 0][0], circles[0, 0][1])


def traffic_sign_detection(img_in):
    """Finds all traffic signs in a synthetic image.

    The image may contain at least one of the following:
    - traffic_light
    - no_entry
    - stop
    - warning
    - yield
    - construction

    Use these names for your output.

    See the instructions document for a visual definition of each
    sign.

    Args:
        img_in (numpy.array): input image containing at least one
                              traffic sign.

    Returns:
        dict: dictionary containing only the signs present in the
              image along with their respective centroid coordinates
              as tuples.

              For example: {'stop': (1, 3), 'yield': (4, 11)}
              These are just example values and may not represent a
              valid scene.
    """

    
    ret = {}
    if (do_not_enter_sign_detection(img_in) is not None):
        x, y = do_not_enter_sign_detection(img_in)
        ret['no_entry'] = x,y
        cv2.circle(img_in,(x, y),1,(255,0,0),3)
    
    if (stop_sign_detection(img_in) is not None):
        x,y = stop_sign_detection(img_in)
        ret['stop'] = x,y
        cv2.circle(img_in,(x, y),1,(255,0,0),3)

    if (yield_sign_detection(img_in) is not None):
        x,y = yield_sign_detection(img_in)
        ret['yield'] = x,y
        cv2.circle(img_in,(x, y),1,(255,0,0),3)

    if (construction_sign_detection(img_in) is not None):
        x,y = construction_sign_detection(img_in)
        ret['construction'] = x,y
        cv2.circle(img_in,(x, y),1,(255,0,0),3)

    if (warning_sign_detection(img_in) is not None):    
        x,y = warning_sign_detection(img_in)
        ret['warning'] = x,y
        cv2.circle(img_in,(x, y),1,(255,0,0),3)

    if (traffic_detect(img_in, (8,13)) is not None):
        xy, light = traffic_detect(img_in, (7,13))
        # print(xy, light)
        ret['traiffic_light'] = xy[0],xy[1]
        cv2.circle(img_in,(xy[0], xy[1]),1,(255,0,0),3)
    else:
        print ("is none ")

        
    print ("all signs ret:", ret)


    # cv2.imshow('Traffic signs',img_in)
    # cv2.waitKey(0)

    return ret

    raise NotImplementedError

def yield_sign_detection_noisy(img_in):
    """Finds the centroid coordinates of a yield sign in the provided
    image.

    Args:
        img_in (numpy.array): image containing a traffic light.

    Returns:
        (x,y) tuple of coordinates of the center of the yield sign.
    """
    # cv2.imshow('Yield sign',img_in)
    # cv2.waitKey(0)
    img_in = cv2.medianBlur(img_in, 13)
    # cv2.imshow('Yield sign',img_in)
    # cv2.waitKey(0)

    hsv = cv2.cvtColor(img_in, cv2.COLOR_BGR2HSV)

    lower_red = np.array([-5,50,50]) #example value
    upper_red = np.array([12,255,255]) #example value

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # cv2.imshow('red mask', img_in)
    # cv2.imshow('mask', mask)
    # cv2.waitKey(0)

    edges = cv2.Canny(mask, 50, 150, apertureSize=3)
    # cv2.imshow('yield edges', edges)
    # cv2.waitKey(0)

    # lines = cv2.HoughLinesP(edges, .5, 5 * np.pi / 180, 0)

    # for line in lines:
        
    #     x1, y1, x2, y2 = line[0]
    #     print (x1, y1, x2, y2)
    #     cv2.line(img_in, (x1, y1), (x2, y2), (255,0,0), 2)

    lines = cv2.HoughLines(edges, 1, 5 * np.pi / 180, 40)
    lineList = []

    lineListDict = {}


    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho

        # print ("rho, theta", rho, theta, int(math.degrees(theta)))

        x1 = int(x0 + 1000 * (-b))

        y1 = int(y0 + 1000 * (a))

        x2 = int(x0 - 1000 * (-b))

        y2 = int(y0 - 1000 * (a))
        lineList.append([x1, y1, x2, y2])
        
        lineLs = []
        if ( 88 < int(math.degrees(theta)) < 92):
            lineLs.append([x1, y1, x2, y2, rho, theta])
            lineListDict["90"] = lineLs
        elif (148 < int(math.degrees(theta)) < 151):
            lineLs.append([x1, y1, x2, y2, rho, theta])
            lineListDict["150"] = lineLs
        elif (28 < int(math.degrees(theta)) < 32):
            lineLs.append([x1, y1, x2, y2, rho, theta])
            lineListDict["30"] = lineLs

        cv2.line(img_in, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
        # print (x1, y1, x2, y2)
    # cv2.imshow('yield houghLines', img_in)
    # cv2.waitKey(0)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho

        # print ("rho, theta", rho, theta, int(math.degrees(theta)))

        x1 = int(x0 + 1000 * (-b))

        y1 = int(y0 + 1000 * (a))

        x2 = int(x0 - 1000 * (-b))

        y2 = int(y0 - 1000 * (a))
        lineList.append([x1, y1, x2, y2])
        
        lineLs = []
        if ( 88 < int(math.degrees(theta)) < 92):
            check = lineListDict.get("90")
            if rho <= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                lineListDict["90"] = lineLs
        elif (148 < int(math.degrees(theta)) < 151):
            check = lineListDict.get("150")
            if rho >= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                lineListDict["150"] = lineLs
        elif (28 < int(math.degrees(theta)) < 32):
            check = lineListDict.get("30")
            if rho >= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                lineListDict["30"] = lineLs

        # cv2.line(img_in, (x1, y1), (x2, y2), (255, 0, 0), 2)        
    
    # print (lineListDict)

    lineListA = lineListDict.get("90")
    lineListB = lineListDict.get("150")
    lineListC = lineListDict.get("30")

    # print (lineListA, lineListB, lineListC)
    # print(lineList)
    # cv2.line(img_in, (lineListA[0][0], lineListA[0][1]), (lineListA[0][2], lineListA[0][3]), (255, 0, 0), 2)
    # cv2.line(img_in, (lineListB[0][0], lineListB[0][1]), (lineListB[0][2], lineListB[0][3]), (0, 255, 0), 2)
    # cv2.line(img_in, (lineListC[0][0], lineListC[0][1]), (lineListC[0][2], lineListC[0][3]), (255, 0, 0), 2)
    # print(((lineList[0][0], lineList[0][1]), (lineList[0][2], lineList[0][3])), (lineList[1][0], lineList[1][1]), (lineList[1][2], lineList[1][3]))
    if (lineListA is not None and lineListB is not None and lineListC is not None):
        x1,y1 = line_intersection(((lineListA[0][0], lineListA[0][1]), (lineListA[0][2], lineListA[0][3])), ((lineListB[0][0], lineListB[0][1]), (lineListB[0][2], lineListB[0][3])))
        # print(x1,y1)
        x2,y2 = line_intersection(((lineListB[0][0], lineListB[0][1]), (lineListB[0][2], lineListB[0][3])), ((lineListC[0][0], lineListC[0][1]), (lineListC[0][2], lineListC[0][3])))
        # print(x2,y2)
        x3,y3 = line_intersection(((lineListA[0][0], lineListA[0][1]), (lineListA[0][2], lineListA[0][3])), ((lineListC[0][0], lineListC[0][1]), (lineListC[0][2], lineListC[0][3])))
        # print(x3,y3)

        centX = int((x1+x2+x3) / 3)
        centY = int((y1+y2+y3) / 3)

        print ((centX, centY))
        # cv2.circle(img_in,(centX, centY),1,(255,0,0),3)


        # cv2.imshow('image', img_in)
        # cv2.waitKey(0)
        # raise NotImplementedError
        return (centX, centY)
    else:
        return None


def warning_sign_detection_noisy(img_in):
    """Finds the centroid coordinates of a warning sign in the
    provided image.

    Args:
        img_in (numpy.array): image containing a traffic light.

    Returns:
        (x,y) tuple of the coordinates of the center of the sign.
    """
    # cv2.imshow('Warning sign',img_in)
    # cv2.waitKey(0)

    hsv = cv2.cvtColor(img_in, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([20,50,50])
    upper_orange = np.array([35,255,255]) 
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # cv2.imshow('red mask', img_in)
    # cv2.imshow('warning mask', mask)
    # cv2.waitKey(0)

      # gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(mask, 50, 150, apertureSize=7)
    lines = cv2.HoughLines(edges,1, 5* np.pi/180, threshold = 40)
    # print(lines)

    lineList = []
    lineListDict = {}
    if (lines is not None):
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho

            # print ("rho, theta", rho, theta, int(math.degrees(theta)))

            x1 = int(x0 + 1000 * (-b))

            y1 = int(y0 + 1000 * (a))

            x2 = int(x0 - 1000 * (-b))

            y2 = int(y0 - 1000 * (a))
            # lineList.append([x1, y1, x2, y2])
            lineLs = []
            checkDict = {}
            if ( 42 < int(math.degrees(theta)) < 46):
                # check = lineListDict.get("44")
                # if rho <= check[0][4]:
                # print ("angle is 44")
                lineLs.append([x1, y1, x2, y2, rho, theta])
                if (lineListDict.get("A") is not None):
                    checkDict = lineListDict.get("A")    
                checkDict[rho] = lineLs
                lineListDict["A"] = checkDict
            elif (133 < int(math.degrees(theta)) < 137):
                # check = lineListDict.get("150")
                # if rho >= check[0][4]:
                # print ("angle is 135")
                lineLs.append([x1, y1, x2, y2, rho, theta])
                if (lineListDict.get("B") is not None):
                    checkDict = lineListDict.get("B")
                checkDict[rho] = lineLs
                lineListDict["B"] = checkDict


            # cv2.line(img_in, (x1, y1), (x2, y2), (255, 0, 0), 2)  
        
        # cv2.imshow('warning output', img_in)
        # cv2.waitKey(0)
        angleA = lineListDict.get("A")
        angleB = lineListDict.get("B")
        sortA = sorted(angleA.keys())
        sortB = sorted(angleB.keys())
        
        # print (sortA)
        # print (sortB)

        lineA1 = angleA.get(sortA[0])
        lineA2 = angleA.get(sortA[1])

        lineB1 = angleB.get(sortB[0])
        lineB2 = angleB.get(sortB[1])
        # print(int((lineA1[0][2] + lineA2[0][2]) / 2), int((lineA1[0][3] + lineA2[0][3]) / 2))

        lineAa = (int((lineA1[0][0] + lineA2[0][0]) / 2), (int((lineA1[0][1] + lineA2[0][1]) / 2)))
        lineAb = (int((lineA1[0][2] + lineA2[0][2]) / 2), (int((lineA1[0][3] + lineA2[0][3]) / 2)))

        lineBa = (int((lineB1[0][0] + lineB2[0][0]) / 2), (int((lineB1[0][1] + lineB2[0][1]) / 2)))
        lineBb = (int((lineB1[0][2] + lineB2[0][2]) / 2), (int((lineB1[0][3] + lineB2[0][3]) / 2)))

        # print(lineAa, lineAb, lineBa, lineBb)
        x,y = line_intersection((lineAa, lineAb), (lineBa,lineBb))

        # cv2.circle(img_in,(int(x), int(y)),1,(0,0,255),3)
        # cv2.imshow('warning output', img_in)
        # cv2.waitKey(0)

        return (int(x), int(y))
    else:
        return None

def traffic_detect_noisy(img_in, radii_range):
    temp_img = np.copy(img_in)
    img_gray   = cv2.cvtColor(temp_img,cv2.COLOR_BGR2GRAY)
    # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    # filtered_img = cv2.filter2D(img_gray, -1, kernel)
    # blur = cv2.medianBlur(img_gray, 7)
    # edges = cv2.Canny(img_gray, 50, 150, apertureSize=7)
    # cv2.imshow('detected circles',img_gray)
    # cv2.waitKey(0)
    minr = radii_range[0]
    maxr = radii_range[-1]+1
    print (minr, maxr, radii_range)
    circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, 10, \
                            param1=20, param2=10, \
                            minRadius=minr, maxRadius=maxr)

    if (circles is None):
        print (circles)
        return None
    
    # Remove outliers by comparing radius of circles, big circles will be removed
    max_radius = 0
    remove_element = 0
    if (len(circles[0]) >= 2):
        
        circles = np.uint16(np.around(circles))
        circles = circles[0]
        # print ("before ", circles)
        circMap = {}
        count = 0
        ind = []
        index = 0
        traffic_x = 0
        for circle in circles:
            res = circMap.get(circle[0])
            if (res is None):
                ind = [index, 1]
                circMap[circle[0]] = ind
            else:
                num = res[1] + 1
                ind = [index, num]
                circMap[circle[0]] = ind
                traffic_x = circle[0]
            index +=1
        # print ("circle map", circMap)
        dele = []
        for circle in circles:
            res = circMap.get(circle[0])
            if (res[1] == 1):
                dele.append(res[0])
                # circles = np.delete(circles, res[0], 0)
        if (len(dele) > 0):
            # print ("dfdsfddffdf delete", dele)
            circles = np.delete(circles, dele, 0)
        sumx = 0
        sumy = 0

        for circle in circles:
            # print("circle", circle)
            sumx += circle[0]
            sumy += circle[1]
        
        # center_cir = ((int(sumx / len(circles))), (int(sumy / len(circles))))
        center_cir = (circles[0][0], circles[0][1])
        hls = cv2.cvtColor(img_in, cv2.COLOR_BGR2HLS)
        index = 0
        count = 0
        x = 0
        y = 0
        lum=0

        for cir in circles:
            # print (cir[0], cir[1])
            x = cir[0]
            y = cir[1]
            # lum_value=hls[y][x]
            if hls[y][x][1] > lum:
                lum=hls[y][x][1]
                index = count
            count += 1


        if index == 0:
            # print ((x,y), 'red')
            cv2.circle(img_in,(center_cir[0],center_cir[1]),1,(255,0,0),3)
            # cv2.imshow('red circles',img_in)
            # cv2.waitKey(0)
            
            return (center_cir[0],center_cir[1]), 'red'
        elif index == 1:
            # print ((x,y), 'yellow')
            cv2.circle(img_in,(center_cir[0],center_cir[1]),1,(255,0,0),3)
            # cv2.imshow('yellow circles',img_in)
            # cv2.waitKey(0)
            return (center_cir[0],center_cir[1]), 'yellow'
            
        elif index == 2:
            # print ((x,y), 'green')
            cv2.circle(img_in,(center_cir[0],center_cir[1]),1,(255,0,0),3)
            # cv2.imshow('green circles',img_in)
            # cv2.waitKey(0)
            return (center_cir[0],center_cir[1]), 'green'
    else:
        return None

def construction_sign_noisy(img_in):
    """Finds the centroid coordinates of a construction sign in the
    provided image.

    Args:
        img_in (numpy.array): image containing a traffic light.

    Returns:
        (x,y) tuple of the coordinates of the center of the sign.
    """
    hsv = cv2.cvtColor(img_in, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([12,41,47])
    upper_orange = np.array([25,255,255]) 
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(mask, 50, 150, apertureSize=3)

    lines = cv2.HoughLines(edges,1, 5* np.pi/180, threshold = 40)

    lineList = []
    lineListDict = {}
    if (lines is not None):
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho

            # print ("rho, theta", rho, theta, int(math.degrees(theta)))

            x1 = int(x0 + 1000 * (-b))

            y1 = int(y0 + 1000 * (a))

            x2 = int(x0 - 1000 * (-b))

            y2 = int(y0 - 1000 * (a))
            # lineList.append([x1, y1, x2, y2])
            lineLs = []
            checkDict = {}
            if ( 42 < int(math.degrees(theta)) < 46):
                # check = lineListDict.get("44")
                # if rho <= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                if (lineListDict.get("A") is not None):
                    checkDict = lineListDict.get("A")    
                checkDict[rho] = lineLs
                lineListDict["A"] = checkDict
            elif (133 < int(math.degrees(theta)) < 137):
                # check = lineListDict.get("150")
                # if rho >= check[0][4]:
                lineLs.append([x1, y1, x2, y2, rho, theta])
                if (lineListDict.get("B") is not None):
                    checkDict = lineListDict.get("B")
                checkDict[rho] = lineLs
                lineListDict["B"] = checkDict


            # cv2.line(img_in, (x1, y1), (x2, y2), (255, 0, 0), 2)  
        
        if (lineListDict.get("A") is not None or  lineListDict.get("B") is not None):
            # cv2.imshow('Construction sign',img_in)
            # cv2.waitKey(0)
            angleA = lineListDict.get("A")
            angleB = lineListDict.get("B")

            sortA = sorted(angleA.keys())
            sortB = sorted(angleB.keys())

            # print (sortA)
            # print (sortB)

            lineA1 = angleA.get(sortA[0])
            lineA2 = angleA.get(sortA[1])

            lineB1 = angleB.get(sortB[0])
            lineB2 = angleB.get(sortB[1])
            # print(int((lineA1[0][2] + lineA2[0][2]) / 2), int((lineA1[0][3] + lineA2[0][3]) / 2))

            lineAa = (int((lineA1[0][0] + lineA2[0][0]) / 2), (int((lineA1[0][1] + lineA2[0][1]) / 2)))
            lineAb = (int((lineA1[0][2] + lineA2[0][2]) / 2), (int((lineA1[0][3] + lineA2[0][3]) / 2)))

            lineBa = (int((lineB1[0][0] + lineB2[0][0]) / 2), (int((lineB1[0][1] + lineB2[0][1]) / 2)))
            lineBb = (int((lineB1[0][2] + lineB2[0][2]) / 2), (int((lineB1[0][3] + lineB2[0][3]) / 2)))

            # print(lineAa, lineAb, lineBa, lineBb)
            x,y = line_intersection((lineAa, lineAb), (lineBa,lineBb))

            # cv2.circle(img_in,(int(x), int(y)),1,(0,0,255),3)
            print ("construction sign ", (int(x), int(y)))
            return (int(x), int(y))
        else:
            return None
    else:
        return None

def stop_sign_detection_noisy(img_in):
    """Finds the centroid coordinates of a stop sign in the provided
    image.

    Args:
        img_in (numpy.array): image containing a traffic light.

    Returns:
        (x,y) tuple of the coordinates of the center of the stop sign.
    """
    blur_img = cv2.medianBlur(img_in, 27)
    # cv2.imshow('Do not enter sign',blur_img)
    # cv2.waitKey(0)
    hsv = cv2.cvtColor(blur_img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,43,46]) #example value
    upper_red = np.array([6,255,230]) #example value

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # cv2.imshow('red mask', img_in)
    # cv2.imshow('mask', mask)
    # cv2.waitKey(0)

    

    # gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(mask, 50, 150, apertureSize=3)
    # cv2.imshow('edges', edges)
    # cv2.waitKey(0)
    # lines = cv2.HoughLines(edges, 1, 5 * np.pi / 180, 40)
    # 

    minr, maxr = 25, 70
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 50, \
                            param1=20, param2=10, \
                            minRadius=minr, maxRadius=maxr)

    # print ("before circles", circles)
    if (circles is not None):
        circles = np.uint16(np.around(circles))
        # print ("circles", circles)
        return (circles[0, 0][0], circles[0, 0][1])
    else:
        return None

    
    # print("lines", lines)

    # for line in lines:
    #     x1, y1, x2, y2 = line[0]
    #     cv2.line(img_in, (x1, y1), (x2, y2), (255,0,0), 2)

    # for line in lines:
    #     rho, theta = line[0]
    #     a = np.cos(theta)
    #     b = np.sin(theta)
    #     x0 = a * rho
    #     y0 = b * rho

    #     x1 = int(x0 + 1000 * (-b))

    #     y1 = int(y0 + 1000 * (a))

    #     x2 = int(x0 - 1000 * (-b))

    #     y2 = int(y0 - 1000 * (a))

    #     cv2.line(img_in, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # cv2.imshow('image', img_in)
    # cv2.waitKey(0)

    raise NotImplementedError



def traffic_sign_detection_noisy(img_in):
    """Finds all traffic signs in a synthetic noisy image.

    The image may contain at least one of the following:
    - traffic_light
    - no_entry
    - stop
    - warning
    - yield
    - construction

    Use these names for your output.

    See the instructions document for a visual definition of each
    sign.

    Args:
        img_in (numpy.array): input image containing at least one
                              traffic sign.

    Returns:
        dict: dictionary containing only the signs present in the
              image along with their respective centroid coordinates
              as tuples.

              For example: {'stop': (1, 3), 'yield': (4, 11)}
              These are just example values and may not represent a
              valid scene.
    """
    

    blurred = cv2.GaussianBlur(img_in, (5, 5), 0)
    img_in=cv2.fastNlMeansDenoisingColored(blurred,None,10,10,7,21)
    # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    # img_in = cv2.filter2D(img_in, -1, kernel)
    # cv2.imshow('Traffic signs',denoised)
    # cv2.waitKey(0)
    # cv2.imshow('Original Image',img_in)
    # cv2.waitKey(0)

    ret = {}
    if (do_not_enter_sign_detection(img_in) is not None):
        x, y = do_not_enter_sign_detection(img_in)
        ret['no_entry'] = x,y
        cv2.circle(img_in,(x, y),1,(255,0,0),3)
    
    if (stop_sign_detection_noisy(img_in) is not None): # cv2.imshow('Original Image',img_in)
    # cv2.waitKey(0)
        x,y = stop_sign_detection_noisy(img_in) # cv2.imshow('Original Image',img_in)
    # cv2.waitKey(0)
        ret['stop'] = x,y
        cv2.circle(img_in,(x, y),1,(255,0,0),3)
    
    if (yield_sign_detection_noisy(img_in) is not None):
        x,y = yield_sign_detection_noisy(img_in)
        ret['yield'] = x,y
        cv2.circle(img_in,(x, y),1,(255,0,0),3)
    
    if (construction_sign_noisy(img_in) is not None):
        x,y = construction_sign_noisy(img_in)
        ret['construction'] = x,y
        cv2.circle(img_in,(x, y),1,(255,0,0),3)

    if (warning_sign_detection_noisy(img_in) is not None):    
        x,y = warning_sign_detection_noisy(img_in)
        ret['warning'] = x,y
        cv2.circle(img_in,(x, y),1,(255,0,0),3)

    if (traffic_detect_noisy(img_in, (8,13)) is not None):
        xy, light = traffic_detect_noisy(img_in, (8,13))
        # print(xy, light)
        ret['traiffic'] = xy[0],xy[1]
        cv2.circle(img_in,(xy[0], xy[1]),1,(255,0,0),3)
    else:
        print ("is none ")
    print ("noisy signs", ret)
    # cv2.imshow('Traffic signs',img_in)
    # cv2.waitKey(0)
    return ret
    raise NotImplementedError


def traffic_sign_detection_challenge(img_in):
    """Finds traffic signs in an real image

    See point 5 in the instructions for details.

    Args:
        img_in (numpy.array): input image containing at least one
                              traffic sign.

    Returns:
        dict: dictionary containing only the signs present in the
              image along with their respective centroid coordinates
              as tuples.

              For example: {'stop': (1, 3), 'yield': (4, 11)}
              These are just example values and may not represent a
              valid scene.
    """
    raise NotImplementedError
