# Plotting China Map using Pyecharts

This repository shows how to utilize pyecharts (wrapper library for Apache Echarts in Javascript) to draw map in Python.

Different to other tutorials, this repository firstly shows how to use self-defined map to exclude some areas.

- Simple enough, you just need to mannually delete the parts in the Geojson file (china_full.json or china_wo_shandong.json) that you don't want to show in graph. Here, I exclude Shandong Province in China as an example. Of course, Shandong is inseparable from China.

This repository also shows how to map English province names into original Chinese ones to facilitate publishing on academic journals in English.

This code is written in OOP style to easy parameter passing across methods inside the Class. You could try to isolate each function as well by passing the same arguments repetitively into each function.

Results are in `Res/` folder as png files.
