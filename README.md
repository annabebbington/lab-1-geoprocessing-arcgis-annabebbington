# LAB 1: GEOPROCESSING IN ARCGIS

This lab explored the different ways to code in the ArcGIS environment.

We began by using the ModelBuilder feature in ArcMap to clip the floodzone shapefile to the basin shapefile, and then select for areas in the special flood hazard areas. We then exported this model to python script, which we then were able to open in a code editor. See flooding.py in the repo. 

We used the the Python window in ArcMap to write a script to clip the soils shapefile to the basin shapefile, which output a shapefile of soils in the extent of the basin.

We then wrote python code to clip the lakes shapefile to the extent of the basin shapefile, using a code editor outside of the ArcGIS workspace. See my_Clip.py in the repo.

### Repo contents
flooding.py is a python script for use in ArcGIS that outputs a shapefile of special flood hazard areas in the basin. 

my_Clip.py is a python script for use in ArcGIS that outputs the lakes in the basin. 

lakes_myClip image is a PNG file showing the output of my_Clip.py, displayed in ArcMap
