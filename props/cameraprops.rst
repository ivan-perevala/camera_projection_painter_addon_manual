Camera
######

Image
=====

Camera binded image. It will be used as a paint brush. Also, its size affects the distortion parameters in the pixel coordinate system (in which way - described in more detail for the corresponding parameters), and therefore - also the possibility of exporting to certain file formats

Millimeters Focal Length
========================

Focal length of the camera in millimeters. The value is stored and can be displayed with double precision

Pixels Focal Length
===================

The focal length of the camera in pixels. The value can be displayed with double precision. Calculated by the formula:

`Pixels Focal Lens = F * P / S`

where `F` is the focal length in millimeters, `P` is the larger side of the image, `S` is the size of the camera sensor in millimeters

Sensor
======

The size of the camera sensor in millimeters, taking into account the larger side of the attached image. This means that if the sensor fit option is set to horizontal - the width of the sensor will be used for calculations, for vertical fit type - height accordingly. These values can be set manually. But for when working with photogrammetric scenes, it is necessary to use the automatic type of sensor adjustment. In this case, if the image has a landscape orientation (or the sides are equal), the width of the sensor will be used, and in the case of a portrait - the height of the sensor. As you can see, there are opportunities for using non-standard workflows, but the main mode of operation is the automatic sensor type. Also note the camera-bound image, this is important for importing and exporting to some file formats. The value is stored and can be displayed with double precision

Millimeters Skew
================

The horizontal skew of the image in millimeters relative to its center, excluding principal deviation

Pixels Skew
===========

Horizontal skew of the image in pixels relative to its center without taking into account deviation. Calculated by the formula:

`Pixels Skew = S * P`

where `S` is the skew value in millimeters, `P` is the size of the larger side of the image

Aspect Ratio
============

Image aspect ratio correction factor. It means the ratio of the height of the image to its width - that is, values ​​greater than 1.0 will stretch it vertically, smaller values ​​will compress it

Millimeters Principal X
=======================

The deviation from the center of the image in millimeters along the X axis. Calculated by the formula:

`Millimeters Principal X = Px * S`

where `Px' is the deviation factor, `S' is the size of the camera sensor

Millimeters Principal Y
=======================

The deviation from the center of the image in millimeters along the Y axis. Calculated by the formula:

`Millimeters Principal Y = Py * S`

where `Py' is the deviation factor, `S' is the size of the camera sensor

Pixels Principal
================

The deviation from the center of the image in pixels. Calculated by the formula:

`Pixels Principal = Pxy * L + (Sxy / 2)`

where `Pxy` is the deviation factor, `L` is the larger side of the image, `Sxy` is the image size

Distortion Model
================

Mathematical model of lens distortion. Note that distortion coefficients may be inconsistent between different distortion models

None
 No distortion, only correction

Division
 The division model with two radial distortion coefficients. This is the simplest mathematical model of linear division of image coordinates, which can be used if the distortion is small, for example, for scenes where the shooting took place close to the object

Polynomial
 A polynomial model with four radial and two tangential distortion coefficients. It uses polynomial functions instead of simple linear division, so it is a more accurate and flexible model that can be used for complex scenes with significant lens distortions

Brown-Conrady
 Brown-Conrady polynomial model with four with four radial and two tangential distortion coefficients. It is the most accurate and flexible model that can be used for complex scenes with significant lens distortions. In general, it is used when a simple linear division model is no longer sufficient

K1
==

Represents linear radial distortion. It corrects or introduces distortion that increases linearly with radial distance

K2
==

Represents cubic radial distortion. It corrects or introduces distortion that increases with the cube of the radial distance

K3
==

Represents quintic (fifth-order) radial distortion. It corrects or introduces distortion that increases with the fifth power of the radial distance

K4
==

Represents seventh-order radial distortion. It corrects or introduces distortion that increases with the seventh power of the radial distance

P1
==

Represents linear tangential distortion. Corrects or introduces distortion that increases linearly with the distance from the image center

P2
==

Represents quadratic tangential distortion. Corrects or introduces distortion that increases with the square of the distance from the image center

Bind History
============

Images that were previously binded to this camera. The option is used if, for example, it is necessary to draw some area from another image, and then return to the previous one. Of course, this is not a standard workflow, but it is used sometimes

Image
-----

The image that was previously attached to this camera


RC Metadata XMP
===============

Reality Capture "Metadata XMP" properties

Export Mode
-----------

Depending on how much you trust your registration, you can select the following options or you can also choose not to export camera poses for Reality Capture (XMP)

Do Not Export
 Do not export camera poses

Draft
 This will treat poses as an imperfect draft to be optimized in the future. The draft mode functions also as a flight log

Exact
 If you trust the alignment absolutely. By choosing this option, you are saying to the application that poses are precise, but the global position, orientation, and scale is not known

Locked
 This is the same as the exact option with the difference that the camera position and calibration will not be changed, when locked

Calibration Group
-----------------

By defining a group for Reality Capture (XMP) we state that all images in this group have the same calibration properties, e.g. the same focal length, the same principal point. Use "-1" if you do not want to group the parameters

Distortion Group
----------------

By defining a group for Reality Capture (XMP) we state that all images in this group have the same lens properties, e.g. the same lens distortion coefficients. Use "-1" if you do not want to group the parameters

In Texturing
------------

Whether to use an image to create an object texture for Reality Capture (XMP)

In Meshing
----------

Whether to use an image to create the object mesh data for Reality Capture (XMP)


