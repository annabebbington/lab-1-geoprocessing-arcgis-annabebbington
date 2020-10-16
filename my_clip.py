'''
Anna Bebbington
Created: 16/10/2020
Description: writing a script for Lab 1, geoprocessing using a code editor
'''
import arcpy
arcpy.env.workspace = "C:\Programming for GIS\Lab_1_Geoprocessing_ArcGIS"
arcpy.Clip_analysis("Data_Lab_1_Geoprocessing_ArcGIS/lakes.shp","Data_Lab_1_Geoprocessing_ArcGIS/basin.shp","Results/lakes_myClip.shp")
