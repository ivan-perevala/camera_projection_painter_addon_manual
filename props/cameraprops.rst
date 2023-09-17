Camera
######

Image
=====

Camera binded image. It will be used as a paint brush. Also, its size affects the distortion parameters in the pixel coordinate system (in which way - described in more detail for the corresponding parameters), and therefore - also the possibility of exporting to certain file formats

Millimeters Focal Length
========================

Camera focal length in millimeters

Pixels Focal Length
===================

Camera focal length in pixels

Sensor
======

The size of the camera sensor in millimeters, taking into account the larger side of the binded image

Millimeters Skew
================

Horizontal camera skew in millimeters

Pixels Skew
===========

Horizontal camera skew in pixels

Aspect Ratio
============

Camera aspect ratio correction factor

Principal X
===========

Deviation of the camera principal point X

Principal Y
===========

Deviation of the camera principal point Y

Millimeters Principal X
=======================

Deviation of the camera principal point X in millimeters

Millimeters Principal Y
=======================

Deviation of the camera principal point Y in millimeters

Pixels Principal
================

Deviation of the camera principal point in pixels

Distortion Model
================

Camera mathematical lens distortion model

None
 No distortion, only correction

Division
 Division lens distortion model with two radial distortion coefficients

Polynomial
 Polynomial lens distortion model with four radial and two tangential lens distortion coefficients

Brown
 Brown-Conrady lens distortion model with four radial and two tangential lens distortion coefficients

K1
==

First radial coefficient

K2
==

Second radial coefficient

K3
==

Third radial coefficient

K4
==

Fourth radial coefficient

P1
==

First tangential coefficient

P2
==

Second tangential coefficient

Bind History
============

Images that were once binded to this camera

Image
-----

Image


RC Metadata XMP
===============

Reality Capture "Metadata XMP" properties

Export Mode
-----------

Depending on how much you trust your registration, you can select the following options or you can also choose not to export camera poses

Do Not Export


Draft
 This will treat poses as an imperfect draft to be optimized in the future. The draft mode functions also as a flight log

Exact
 If you trust the alignment absolutely. By choosing this option, you are saying to the application that poses are precise, but the global position, orientation, and scale is not known

Locked
 This is the same as the exact option with the difference that the camera position and calibration will not be changed, when locked

Calibration Group
-----------------

By defining a group we state that all images in this group have the same calibration properties, e.g. the same focal length, the same principal point. Use "-1" if you do not want to group the parameters

Distortion Group
----------------

By defining a group we state that all images in this group have the same lens properties, e.g. the same lens distortion coefficients. Use "-1" if you do not want to group the parameters

In Texturing
------------


In Meshing
----------



