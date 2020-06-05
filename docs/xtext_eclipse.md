# Xtext and Eclipse

Xtext is integrated in Eclipse.
To run this tutorial (using Xtext) you need to install Eclipse with the 
appropriate plugins.

Note: The parser "Antlr" is not distributed with eclipse. You need to install
it manually [(itemis update site)](http://download.itemis.de/updates),
else it will be downloaded for every Xtext project you create.


## Download and install

Download the package
["Eclipse Modeling"](http://www.eclipse.org/downloads/packages/).
Unpack the archive to make eclipse available.

    ::shell
    root@xtext:~/Download# ls
    eclipse-modeling-xxx-linux-gtk-x86_64.tar.gz
    root@xtext:~/Download# tar xzf eclipse-modeling-xxx-linux-gtk-x86_64.tar.gz
    root@xtext:~/Download# mv eclipse /opt/
    root@xtext:~/Download# /opt/eclipse/eclipse &


To complete the installation you need "Install New Software" from the
"Help" menu entry. 

 * Enter the URL of the itemis update site (see above)
    in the field "work with" and press enter. 
 * Then select "Xtext" and "Xtext Antlr" and install the selected software.


