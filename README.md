# Master's Thesis by Sagar Bhure
### Title 
Dispersion analysis of CNT/Epoxy composites and architecture of porous scaffold using Digital Image Processing

### Abstract
Carbon nanotube is well recognized as the strongest and stiffest material developed till date. However due to their nanoscopic size, the useful properties of CNTs can be utilized if they are homogeneously dispersed into matrices. Thus the application of CNT/Epoxy composites have been limited due to improper load transfer from matrix to CNT.

This improper load transfer can be attributed to the agglomeration of CNTs in nano composites and non-uniform dispersion of CNT into the host matrix. Current work focuses on the study of dispersion of CNTs in CNT/Epoxy composite using Digital Image processing. This work has been further extended to describe the architecture of scaffold and determine architectural properties of scaffold such as pore size, porosity and their biological relevance.

### Tools: 
- OpenCV
- ImajeJ
- Micor-CT
- AutoCAD

### Basic Requirement
 - Scaffold: A scaffold for tissue regeneration is a structure which is able to support and/or promote tissue regeneration. It should possess a 3D and well-defined macro-architecture and micro-architecture with an interconnected pore network. It should be biocompatible, and its mechanical properties should be similar to those of original bone tissue.

 ![](https://web.stanford.edu/group/mota/education/Physics%2087N%20Final%20Projects/Group%20Gamma/bone%20repair%20with%20coral.jpg)


### Algorithm Development
- Calibration :  In our case we have used a one rupee Indian coin as our reference object and we have also ensured that it is always the leftmost object in our image.
![](https://github.com/sagarbhure/MasterThesis/blob/master/Calib1.PNG)
![](https://github.com/sagarbhure/MasterThesis/blob/master/Calib2.PNG)

- Pore Detection : The image sjown below is the bitmap(or bmp) image obtained after micro-ct of the scaffold material obtained from Department of Mechanical Engineering IITK, thus after applying suitable image segmentation techniques  we have the binary image in which we can apply suitable feature extraction algorithms to extract pores and examine pore characteristic.In the following figure (to right) we extracted outermost contour as it has known dimension and it can be used as a reference dimension to calculate dimension of any pore inside the scaffold material.
![](https://github.com/sagarbhure/MasterThesis/blob/master/PoreDetection.PNG)

- Porosity : Measurement of porosity can be obtained in both 2D and 3D. The 2D calculation is made by dividing the area occupied by pores by the total area of the image this can be simply done by determining the ratio of pixels associated with pores PPi to the number contained in whole image PPt
![](https://github.com/sagarbhure/MasterThesis/blob/master/Porosity.PNG)

- InterConnectivity: Pore interconnectivity is is considered an important structural parameter that may affect the biological performance of a material by influencing fluid permeation, cell migration tissue ingrowth.
  - ##### Throat Detection Algorithm: 
                 
             Given any pore(or contour) our algorithm detects the presence of throat and returns the coordinate point of the throat which in turn can be used to find the diameter of the throat. 
![](https://github.com/sagarbhure/MasterThesis/blob/master/PoreDetection.PNG)
![](https://github.com/sagarbhure/MasterThesis/blob/master/AlgoPoredetection.PNG)
- Tortuosity: is a property of a curve being tortuous. There have been several attempts to quantify this property. Tortuosity is commonly used to describe diffusion and fluid flow in porous media, such as bones and snow.In scaffolds tortuosity in an important parameter that affects the cell migration, nutrient diffusion and waste removal. Calculation tortuosity in biological material is difficult.Tortiuosity describes the hinderance posed to the diffusion process geometrically complex medium(scaffold in our case) in comparison to environment free of any obstacles.
![](https://github.com/sagarbhure/MasterThesis/blob/master/tortursity_3D.Print.PNG)
![](https://github.com/sagarbhure/MasterThesis/blob/master/Torturisity.PNG)
### Future Scope and Refrences 
- S. Chakraborty, “Tailored carbon nanotubes for tissue engineering applications,” 2010.
- J. S. David J Apple, “Harold ridley and the invention of the intraocular lens,” 1996.
- E. Brey, “A book on vascularization: Regenerative medicine and tissue engineering,” 1999.
 - R. Szeliski, “A book on computer vision: Algorithms and applications,”

Feel free to write me on sagarbhureaerospace@gmail.com, for full source code and study guide. 
