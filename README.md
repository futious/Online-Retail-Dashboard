<div id="top"></div>

# Online Retail Dashboard

  
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#how-to-use">How to Use</a>
        <ul>
          <li><a href="#homepage">Homepage</a></li>
        <li><a href="#item-information">Item Information</a></li>
         <li><a href="#customer-information">Customer Information</a></li>
      </ul>  
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

 <p>
  <img width="1000" align='left' src="https://github.com/futious/Online-Retail-Dashboard/blob/687fc900d0683d3f47d869dce0305ddbf490a8b3/assets/Homepage.png?raw=true">
</p>


 This dashboard is used to demonstrate the different components of dash. The goal is to give the viewer a visually appealing way to display data. The types of components used in this dashboard are as follows.
 
 1) Image displays
 2) Cards
 3) Tables
 4) Side bars
 5) Maps
 6) Line graphs
 7) Line graphs
 8) Drop down menus
 9) Scatter plots
 10) Bar graphs
 11) CSS Formating

Visual representation of data is indispensable in explaining data to people. The dashboard is versatile in displaying data. We can change color, placement and represent data using multiple modes.


<p align="right">(<a href="#top">back to top</a>)</p>


---
### Built With

* [Spyder version 4.2.5](https://www.spyder-ide.org)
* [Python version 3.8](https://www.python.org)

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started


To view the dashboard in its entirety you will need to download the following. 

1) Assets folder
2) OnlineRetail.csv.zip
3) app.py

or clone the repository 
```sh
git clone https://github.com/futious/Online-Retail-Dashboard.git
```

After you have downloaded all of these items and opened the zip file run the python code. The dashboard will run locally and requires you to use your internet browser to see it. Input http://127.0.0.1:8070 into your browser and the dashboard will populate only after the code has been run.



  ---
### Installation

To run the code you may need to download dash in your terminal using 

   ```sh
   pip install -r requirements.txt
   ```


  

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- How to Use -->
## How to Use

After you have downloaded all of these items and opened the zip file run the python code. The dashboard will run locally and requires you to use your internet browser to see it. Input http://127.0.0.1:8070 into your browser and the dashboard will populate only after the code has been run.



  ---
### Installation

To run the code you may need to download dash in your terminal using 
 <p>
  <img width="1000" align='left' src="https://github.com/futious/Online-Retail-Dashboard/blob/687fc900d0683d3f47d869dce0305ddbf490a8b3/assets/Homepage.png?raw=true">
</p>


To continue to other sections of the dashboard click on the categories on the left hand side bar, Home, Item Information, and Customer Information.

<!-- Item Information -->
### Item Information

The first part of the item information section is a choropleth map. This map shows the distribution of products sold around the world. This map has been modified so that if the country has more than 1000 items purchased, then they will be yellow. Note: The United Kingdom vastly out purchased the rest of the world at 496 thousand units.

  <img width="1000" align='left' src="https://github.com/futious/Online-Retail-Dashboard/blob/848e7b7756a7b2eedf51bd5895fc727054dfa6b3/assets/1st.png?raw=true">
</p>

The second graph in the item information section is a line graph.

  <img width="1000" align='left' src="https://github.com/futious/Online-Retail-Dashboard/blob/848e7b7756a7b2eedf51bd5895fc727054dfa6b3/assets/2nd.png?raw=true">
</p>

This graph is dependent on the two drop down menus. The first drop down menu changes the information type from total sales to quantity.

  <img width="1000" align='left' src="https://github.com/futious/Online-Retail-Dashboard/blob/848e7b7756a7b2eedf51bd5895fc727054dfa6b3/assets/3rd.png?raw=true">
</p>

The second drop down menu allows you to choose the country that you would like to know about.

  <img width="1000" align='left' src="https://github.com/futious/Online-Retail-Dashboard/blob/848e7b7756a7b2eedf51bd5895fc727054dfa6b3/assets/4th.png?raw=true">
</p>


The last visual in the item information section is a scatter plot.

  <img width="1000" align='left' src="https://github.com/futious/Online-Retail-Dashboard/blob/848e7b7756a7b2eedf51bd5895fc727054dfa6b3/assets/5th.png?raw=true">
</p>

This graph is dependent on a single drop down menu and allows you to change the item that you would like to see sales over time.

  <img width="1000" align='left' src="https://github.com/futious/Online-Retail-Dashboard/blob/848e7b7756a7b2eedf51bd5895fc727054dfa6b3/assets/6th.png?raw=true">
</p>

<!-- Customer Information -->
### Customer Information

There is currently only one visual in the customer information section. This is a bar graph that shows the top 5 customers based on total sales.

  <img width="1000" align='left' src="https://github.com/futious/Online-Retail-Dashboard/blob/848e7b7756a7b2eedf51bd5895fc727054dfa6b3/assets/7th.png?raw=true">
</p>


You can change the number of customers you would like to see using the drop down menu.


  <img width="1000" align='left' src="https://github.com/futious/Online-Retail-Dashboard/blob/848e7b7756a7b2eedf51bd5895fc727054dfa6b3/assets/8th.png?raw=true">
</p>



<!-- ROADMAP -->
## Roadmap



Some other components I would like to use in the future are
- [ ] Sunburst charts
- [ ] Tabs
- [ ] Markers for the line chart


<p align="right">(<a href="#top">back to top</a>)</p>
