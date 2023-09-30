Object
######

Rotation Matrix
===============

Row-major object rotation matrix 3x3 in Blender (Cartesian) coordinate system. Properties are stored as double-precision floats, according to the IEEE-754 standard, so imported values ​​will not lose precision

Row: 1, Column: 1
-----------------

Represents 1 row and 1 column of row-major object rotation matrix 3x3 in Blender (Cartesian) coordinate system

Row: 1, Column: 2
-----------------

Represents 1 row and 2 column of row-major object rotation matrix 3x3 in Blender (Cartesian) coordinate system

Row: 1, Column: 3
-----------------

Represents 1 row and 3 column of row-major object rotation matrix 3x3 in Blender (Cartesian) coordinate system

Row: 2, Column: 1
-----------------

Represents 2 row and 1 column of row-major object rotation matrix 3x3 in Blender (Cartesian) coordinate system

Row: 2, Column: 2
-----------------

Represents 2 row and 2 column of row-major object rotation matrix 3x3 in Blender (Cartesian) coordinate system

Row: 2, Column: 3
-----------------

Represents 2 row and 3 column of row-major object rotation matrix 3x3 in Blender (Cartesian) coordinate system

Row: 3, Column: 1
-----------------

Represents 3 row and 1 column of row-major object rotation matrix 3x3 in Blender (Cartesian) coordinate system

Row: 3, Column: 2
-----------------

Represents 3 row and 2 column of row-major object rotation matrix 3x3 in Blender (Cartesian) coordinate system

Row: 3, Column: 3
-----------------

Represents 3 row and 3 column of row-major object rotation matrix 3x3 in Blender (Cartesian) coordinate system


Location
========

The position of the object in Blender's Cartesian coordinate system. Properties are stored as double-precision floats, according to the IEEE-754 standard, so imported values ​​will not lose precision

X
-

The position of the object in Blender's Cartesian coordinate system by X axis

Y
-

The position of the object in Blender's Cartesian coordinate system by Y axis

Z
-

The position of the object in Blender's Cartesian coordinate system by Z axis


RC X, Y, Alt
============

Representation of object position as Reality Capture X, Y, Alt coordinates. Values ​​are stored in double precision according to the IEEE-754 standard in Blender's coordinate system, but can also be displayed in double precision and converted as X, Y, Alt

X
-

The location of the object in the Reality Capture coordinate system along the X-axis. Corresponds to the value along the negative Y-axis in Blender's Cartesian coordinate system

Y
-

The location of the object in the Reality Capture coordinate system along the Y-axis. Corresponds to the value along the X-axis in Blender's Cartesian coordinate system

Alt
---

The location of the object in the Reality Capture coordinate system along the Alt-axis. Corresponds to the value along the X-axis in Blender's Cartesian coordinate system


RC Heading, Pitch, Roll
=======================

Representation of object orientation as Reality Capture Heading, Pitch, Roll. Values are stored in double precision according to the IEEE-754 standard in Blender's rotation matrix, but also can be displayed in double precision and converted as Heading, Pitch, Roll

Heading
-------

The object's heading value in the Reality Capture coordinate system. Corresponds to the matrix elements in to the Blender coordinate system according to the formula:

`Heading = degrees(-atan2(M₁₁, M₀₁))`

where `Mᵢⱼ` is an element of the rotation matrix

Pitch
-----

The object's pitch value in the Reality Capture coordinate system. Corresponds to the matrix elements in to the Blender coordinate system according to the formula:

`Pitch = degrees(asin(M₂₁))`

where `Mᵢⱼ` is an element of the rotation matrix

Roll
----

The object's roll value in the Reality Capture coordinate system. Corresponds to the matrix elements in to the Blender coordinate system according to the formula:

`Roll = degrees(-atan2(M₂₀, M₂₂))`

where `Mᵢⱼ` is an element of the rotation matrix


RC Omega, Phi, Kappa
====================


Omega
-----


Phi
---


Kappa
-----



RC Rotation Component
=====================


Item: 1 (Row: 1, Column: 1)
---------------------------


Item: 2 (Row: 1, Column: 2)
---------------------------


Item: 3 (Row: 1, Column: 3)
---------------------------


Item: 4 (Row: 2, Column: 1)
---------------------------


Item: 5 (Row: 2, Column: 2)
---------------------------


Item: 6 (Row: 2, Column: 3)
---------------------------


Item: 7 (Row: 3, Column: 1)
---------------------------


Item: 8 (Row: 3, Column: 2)
---------------------------


Item: 9 (Row: 3, Column: 3)
---------------------------



