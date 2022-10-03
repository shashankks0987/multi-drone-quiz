# multi-drone-quiz

## Problem 1
 - Approach: Meijster's distance transform
 - Reference used : http://fab.cba.mit.edu/classes/S62.12/docs/Meijster_distance.pdf
 - My understandings:
   - Linear time algorithm to find the closest point that has a '1' (in image processing. here, obstacles)
   - Uses parabola and envelope technique to reduce computation of distance for every point.
   - Has 2 phases: 
       - Phase 1: each column is separately scanned: For each point in the column, the distance to the nearest points is determined
       - Phase 2: each row is separately scanned: the minimum of (x-x')^2 + G(x',y) is found. The G is determined in the first phase.
 ## Problem 2
   - Initial thoughts:
     - A 3D EDT can be created so that at every point when the drone moves a O(1) lookup can be done to get the location of the nearest obstacle from the current position of the drone.
     - A related paper in 3D EDT : https://www.worldscientific.com/doi/abs/10.1142/S0218001410008202
     - A Voronoi diagram can help in faster lookup as it is done in mobile networks to find the nearest cell tower
## Problem 3
 - K-nearest neighbor path planning algorithm


## Problem 4
-  