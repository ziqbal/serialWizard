serialWizard
============

A single python script to transport serial port data and serve it via http to a web client with several demos to visualise the data.

On Microsoft Windows copy the files into a folder in your PythonXYZ installation.

This is alpha version code running on a cliff edge so it may work out of the box or fail completely.

Prerequisites are Python and pySerial - tested using 2.7 so may or may not work on other versions.

serialwizard.py
---------------

- Modify SERIALPORT to match the port the Arduino is using

- Modify NETWORKPORT if you have to

- Run script from the command line using python

- Or double click .bat file on Microsoft Windows

- View User Interface in web browser using http://127.0.0.1:8888 (or whatever port you chose)


