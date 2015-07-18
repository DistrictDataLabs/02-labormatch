# 02-labormatch
Private repo for team Labor Match

Summary of Problem: Using data from the Bureau of Labor Statistics, LaborMatch built an interactive site to help policy makers, investors, and the public. The team calculated job demand in ten major industries for each state. The user can choose any state and the program returns the number of jobs in ten industries for that state. LaborMatch provides a useful visualization and interface that allows users to explore their data state by state. They started by pulling the data via API. The team originally wanted to use data from Linkedin and Dice as well. However, although several scripts were written to ingest data from those sites, they decided to stick with only BLS data, After, they manipulated the data into JSON format. They built a lookup table from from a state name and an industry name. For the collection of series, the team extracted year long average values from the data for each month. This result was the input for their d3 visualization. They created an html file that incorporates this visualization. The website makes use of a linked map and bar plot.
 
[Check it out](http://ysun1.github.io/labormatch/)

#Software Architecture Diagram
![](http://i60.tinypic.com/14r4om.jpg)

#Data Flow Diagram
![](http://i57.tinypic.com/akaemt.jpg)

[Extra code](https://github.com/ysun1/ysun1.github.io)
