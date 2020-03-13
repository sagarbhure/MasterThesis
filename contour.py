import numpy as np
import cv2
from numpy import array


im = cv2.imread('thresh224.jpg')   									##### Read binary image

#########################################
# Create a blank image same as input size
#########################################
a = array(im)
s=list(a.shape)

blank_image = np.ones((s[0],s[0],3), np.uint8)

cv2.imshow('im2',blank_image)
cv2.waitKey(0)

########################
ans=0
for i in range(len(im[0])):
	if sum(im[0][i])!=0:
		ans=ans+1
	#print im[0][i]
#print ans

cv2.imshow('input file',im)
cv2.waitKey(0)

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,70,255,0)							##### Convert it to binary (just for convineance)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)	##### find the contour first one is source image, second is contour 													retrieval mode, third is contour approximation method. And it outputs the 													contours and hierarchy. contours is a Python list of all the contours in 													the image. Each individual contour is a Numpy array of (x,y) coordinates 													of boundary points of the object.
#print len(contours)
cv2.imshow('tsh',ret)
cv2.waitKey(0)
#print contours



###################
text_file = open("contour_list.txt", "w")							##### Write the coordinates (x,y) of a contour in an txt file python 
text_file.write("List of Contours: %s" % contours) 
text_file.close()
######################


cv2.drawContours(im, contours,-1, (0,255,0),1)						#####It can also be used to draw any shape provided you have its boundary points. 												Its first argument is source image, second argument is the contours which 												should be passed as a Python list, third argument is index of contours 												(To draw all contours, pass -1) and remaining arguments are color, thickness etc.

##########################

#cv2.imwrite('result_boundary.jpg',im)
cv2.imshow('im',im)
cv2.waitKey(0)


##########################
#Centeroid & Area code below
##########################

area=[]
t=0
s=0
g=0
centroid=[[]]

for i in range(len(contours)):
	s=t									##### Using Image moments help you to calculate some features like center 												of mass of the object, area of the object etc
	cnt = contours[i]
	M = cv2.moments(cnt)
	
	if M['m00']!=0:
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
	
		#print cx ,'cx'
		#print cy ,'cy'
		centroid.append([cx,cy])

		area.append(cv2.contourArea(cnt))					##### Area calculated by cv2.contourArea(cnt) has same value as M['m00']


#print sum(area)-max(area)

##########################
#for i in range(len(contours)):
	#cv2.drawContours(blank_image, contours[len(contours)-i-1],-1, (0,255,0),-1)
	#cv2.imshow('rst',blank_image)
	#cv2.waitKey(0)
	#cv2.imwrite('result1_contour'+str(i)+'.jpg',blank_image)

#######################################
##Detect Biggest Contour COde
#######################################
areaArray=[]	
for i, c in enumerate(contours):
    area = cv2.contourArea(c)
    areaArray.append(area)
sorteddata = sorted(zip(areaArray, contours), key=lambda x: x[0], reverse=True)
b=0
s=0
m=0
for i in range(1,len(contours)):
	secondlargestcontour = sorteddata[i][1]
	#M = cv2.moments(secondlargestcontour)
	#print cv2.contourArea(secondlargestcontour)
	cnt = secondlargestcontour
	#cv2.drawContours(blank_image, secondlargestcontour,-1, (10+(i*10),30+(i*20),255),1)

	#print cv2.contourArea(cnt)
	if cv2.contourArea(cnt) >250 :
		b=b+1
	elif cv2.contourArea(cnt) < 250 and cv2.contourArea(cnt)>100:
		m=m+1
	elif cv2.contourArea(cnt) < 100 and cv2.contourArea(cnt)!=0:
		s=s+1
	#cv2.fillPoly(blank_image, pts =[secondlargestcontour], color=(255,255,255))
	#cv2.imshow('rst',blank_image)
	#cv2.waitKey(0)
cv2.imshow('rst',blank_image)
cv2.waitKey(0)
secondlargestcontour = sorteddata[5][1]

#########
sets1=secondlargestcontour
a=[]

for i in xrange(len(sets1)):
    b=[]
    for j in xrange(len(sets1[i])):
        for k in xrange(len(sets1[i][j])):
            if(sets1[i][j][k] not in b ):
                b.append(sets1[i][j][k])
	print b[0],b[1]
    a.append(b)
print a




###########





cv2.drawContours(blank_image, secondlargestcontour,-1, (0,255,0),-1)
cv2.imshow('sagar',blank_image)
cv2.waitKey(0)
cv2.imwrite('result1_contour.jpg',blank_image)
print 'small:',s
print 'big:',b
print 'medium:',m
##################################################


###################
# ADD CODE HERE #
########

text_file = open("area_List.txt", "w")								##### Write the coordinates (x,y) of a contour in an txt file python 
text_file.write("List of areas: %s" % areaArray) 
text_file.close()

text_file = open("centroid_List.txt", "w")							##### Write the coordinates (x,y) of a contour in an txt file python 
text_file.write("List of centroid: %s" % centroid) 
text_file.close()




