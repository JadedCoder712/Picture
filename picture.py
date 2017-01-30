"""
picture.py
Author: Kyle Postans
Credit: none ever

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
rot = Color(0xff0000, 0.5)
grun = Color(0x00ff00, 1.0)
blau = Color(0x0000ff, 1.0)
schwartz = Color(0x000000, 1.0)
orange = Color(0xffa500, 1.0)
gelb = Color(0xffff00, 0.9)

porklein = LineStyle (1, schwartz)

lolwatchthisrectangle = RectangleAsset(190, 68, porklein, rot) #brick
lolrundiscircle = CircleAsset(68, porklein, orange) #face
lolelipticalpooltable = EllipseAsset(20, 65, porklein, gelb)

Sprite(lolwatchthisrectangle, (300, 300))
Sprite(lolrundiscircle, (190, 190))






# add your code here /\  /\  /\


myapp = App()
myapp.run()
