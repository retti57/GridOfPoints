<h1>SPIDERPOINTS</h1>
<h2>SPIDERPOINTS is a reference grid of points helpful in <br>planing and plotting flightpath</h2>


<br>
The tool creates a square-shaped grid of points based on given coordinates, number of points in line 
and distance between nearest points.<br>
The grid is saved in two files that are readable by various navigation applications : .KML and .GPX .

<h2>Installation</h2>
To install package place the installation file in the root directory , then use this command: 
<code>pip install spiderpoints-0.0.9.tar.gz</code>
<br>

<h2>Usage</h2>
This tool is build in the way to be easy to use. <br>It only needs one method call and requires three input values of <b>string</b> type:
<ol>
<li>First point coordinates - This point is an top-left anchor point of whole grid - NOTE: The coords in format: <b>'52.42414, 18.23123'</b>. The comma is needed.</li>
<li>Number of points to be placed in each row</li>
<li>Distance between each point - NOTE: measure is in metric system</li></ol>
Firstly, import class SpiderPoints from spiderpoints module.<br> 
Next, feed the created object with three inputs and call the <code>create_kml_gpx()</code> method on it.<br>
<code>from spiderpoints.spiderpoints import SpiderPoints</code><br>
<code>SpiderPoints('52.42414, 18.23123', '5', '4').create_kml_gpx()</code><br>
Now you have two files named: "punkty.kml" and "punkty.gpx" on root directory level.



<h3>Dependencies</h3>
<ul>
<li>"geopy==2.4.1"</li>
<li>"gpxpy==1.6.2"</li>
<li>"simplekml==1.3.6"</li>
</ul>
