<h1>SQLAlchemy Challenge</h1>
<ul>The following repository contains:</ul>
<li>Resources folder with the sqlite and csv files,</li>
<li>app.py file - Flask API,</li>
<li>3 Jupyter Notebooks</li>
<img src="https://github.com/DominikaRzez/sqlalchemy-challenge/blob/main/images/app.py.png?raw=true">
<img src="https://github.com/DominikaRzez/sqlalchemy-challenge/blob/main/images/climate_api.png?raw=true">
<br>
<p>The first Jupyter Notebook file - climate_analysis.ipynb - contains the main, required part of the homework. It is a basic climate analysis and data exploration of the climate database, including:</p>
<ul>
  <li>Retrieval of the last 12 months of precipitation data</li>
  <li>Graph presenting the results</li>
  <li>Finding the most active station</li>
  <li>Retrieval of the last 12 months of temperature observation data for this station</li>
  <li>Histogram displaying the results</li>
 </ul>
 <img src="https://github.com/DominikaRzez/sqlalchemy-challenge/blob/main/images/percipitation_over_12months.png?raw=true">
<br>
<p>The second Jupyter Notebook - temperature_analysis_bonus1.ipynb - includes temperature analysis for the months of June and December at all stations across all available years and the t-test to determine whether the difference in the means is statistically meaningful.</p>
<img src="https://github.com/DominikaRzez/sqlalchemy-challenge/blob/main/images/temperature_analysis.png?raw=true">
<br>
<p>The third Jupyter Notebook - temperature_analysis_bonus2.ipynb - contains the 2nd bonus task:
  <ul>
    <li>The calculation of the min, avg, and max temperatures for the specified time period</li>
    <li>Bar chart presenting the values</li>
    <li>Calculation of the rainfall per weather station</li>
    <li>Calculation of the tempreture daily normals</li>
    <li>Area plot for daily normals results</li>
 </ul>
 <img src="https://github.com/DominikaRzez/sqlalchemy-challenge/blob/main/images/area_plot.png?raw=true">
</p>
<br>
<p>All the queries were performed using SQLAlchemy ORM queries, Pandas, Matplotlib and Datetime libraries.</p>
