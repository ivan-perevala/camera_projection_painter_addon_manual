Data Cleanup
############

Operator to clear existing data before starting a new scene setup.

If the scene contains only data from a standard file, namely 3 objects: a cube with standard material, a camera and a lamp, then the operator will automatically offer to clear this data (of course, there is a chance that someone will work with it, but it is small). The same goes for images. If the file contains only one standard image that is reserved for the render result, it will also be prompted to delete it.

When it comes to the context setting order, this statement is always executed first. If you do not need to clear the data, you just need to remove both flags and agree to the execution. In this case, all the data will remain in place - this can be useful for resetting the context for the current scene (for example, if you need to finish the context setting interrupted at one of the following stages).

Cleanup Data
============

Delete object, mesh, material, texture, light and camera data-blocks

Cleanup Images
==============

Delete all image data-blocks

