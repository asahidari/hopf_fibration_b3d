# Hopf fibration in Blender with add-ons

## Description

This project is inspired by https://github.com/nilesjohnson/hopf_fibration (https://nilesjohnson.net/hopf-production.html). The original fibration is written for [sagemath](https://www.sagemath.org) environment. This project repository aims to create the 3d fibration models in [Blender](https://www.blender.org).

## Installation

### With sverchok add-on

* Install Blender and [sverchok add-on](https://github.com/nortikin/sverchok).
* Enable the add-on with Menu->Edit->Preferences...-> add-ons.
* Open sverchok node editor, select Editor Type-> 'sverchok nodes', click '+ New' on header parts, push 'n' key to open side menu and open 'sverchok' tab.
* Import json files in this repository from the tab menu.

### With Animation nodes add-on

* Install Blender and [animation nodes add-on](https://animation-nodes.com).
* Enable the add-on with Menu->Edit->Preferences...-> add-ons.
* Open animation nodes editor, select Editor Type-> 'animation nodes', click '+ New' on header parts.
* Create node tree following images in this repository (Animation nodes add-on (2.1.7) used this time cannot import/export node trees in json format ).

## Usage

### With sverchok add-on

There are four types of fibration following the original source. Select each json file for your purpose. You can change parameters of each nodes at the left side of the each node tree.
#### hopf_fibration_greatcircle_sv.blend.json -> GreatCircle

|Image|Node tree|
|---|---|
|![Hopf Fibration GreatCircle Image](./sverchok/images/hopf_fibration_great_circle_image_sv.png)|![Hopf Fibration GreatCircle](./sverchok/images/hopf_fibration_great_circle_sv.png)|
#### hopf_fibration_latitude_sv.blend.json -> Lattitude
|Image|Node tree|
|---|---|
|![Hopf Fibration Latitude Image](./sverchok/images/hopf_fibration_latitude_image_sv.png)|![Hopf Fibration Latitude](./sverchok/images/hopf_fibration_latitude_sv.png)|
#### hopf_fibration_spiral_sv.blend.json -> Spiral
|Image|Node tree|
|---|---|
|![Hopf Fibration Spiral Image](./sverchok/images/hopf_fibration_spiral_image_sv.png)|![Hopf Fibration Spiral](./sverchok/images/hopf_fibration_spiral_sv.png)|
#### hopf_fibration_flower_sv.blend.json -> Flower
|Image|Node tree|
|---|---|
|![Hopf Fibration Flower Image](./sverchok/images/hopf_fibration_flower_image_sv.png)|![Hopf Fibration Flower](./sverchok/images/hopf_fibration_flower_sv.png)|

Next one is multiple version of lattice. 
#### hopf_fibration_multiple_latitudes_sv.blend.json -> Multiple Lattitudes
(**WARNING** this node tree may be broken when loaded because using too many nodes. If you encounter some erros, please recreate the nodes around the 'error' nodes (these nodes color will be changed if they have some errors))
|Image|Node tree|
|---|---|
|![Hopf Fibration Multiple Latitudes Image](./sverchok/images/hopf_fibration_multiple_latitudes_image_sv.png)|![Hopf Fibration Multiple Latitudes](./sverchok/images/hopf_fibration_multiple_latitudes_sv.png)|

Additionally, there are python scripts for sverchok 'Script Node Lite' node. These can be used in your own node tree.
* hopf_fibration_sv.py
* hopf_fibration_greatcircle_sv.py
* hopf_fibration_latitude_sv.py
* hopf_fibration_spiral_sv.py
* hopf_fibration_flower_sv.py

### With Animation nodes add-on

To make the 3d models, create the node trees following images and using scripts in this repository.

#### Configuring script nodes
![Configuring script nodes Image](./animationnodes/images/hopf_fibration_scripts_an.png)

#### Fibration Loop (creating rings from original vertices)
![Fibration Loop Image](./animationnodes/images/hopf_fibration_fibrationloop_an.png)
#### Defining Colors from original vertex-locations
![Defining Colors Image](./animationnodes/images/hopf_fibration_verts_color_loop_an.png)

#### Mesh Instance Loop (Configuration of mesh objects with vertex color)
![Mesh Instance Loop Image](./animationnodes/images/hopf_fibration_mesh_instance_loop_an.png)

#### Spheres for original vertices
![Spheres Image](./animationnodes/images/hopf_fibration_spheres_an.png)

#### Great Circle Node Tree
|Image|Node Tree|
|---|---|
|![Great Circle Image](./animationnodes/images/hopf_fibration_great_circle_image_an.png)|![Great Circle Node Tree](./animationnodes/images/hopf_fibration_great_circle_an.png)|

#### Latitude Node Tree
|Image|Node Tree|
|---|---|
|![Latitude Image](./animationnodes/images/hopf_fibration_latitude_image_an.png)|![Latitude Node Tree](./animationnodes/images/hopf_fibration_latitude_an.png)|

#### Spiral Node Tree
|Image|Node Tree|
|---|---|
|![Spiral Image](./animationnodes/images/hopf_fibration_spiral_image_an.png)|![Spiral Node Tree](./animationnodes/images/hopf_fibration_spiral_an.png)|

#### Flower Node Tree
|Image|Node Tree|
|---|---|
|![Flower Image](./animationnodes/images/hopf_fibration_flower_image_an.png)|![Flower Node Tree](./animationnodes/images/hopf_fibration_flower_an.png)|


#### Multiple Latitude Node Tree
|Image|Node Tree|
|---|---|
|![Multiple Latitudes Image](./animationnodes/images/hopf_fibration_multiple_latitudes_image_an.png)|![Multiple Latitudes Node Tree](./animationnodes/images/hopf_fibration_multiple_latitudes_an.png)|

#### Script files

These are script files to make script node.
* hopf_fibration_sv.py
* hopf_fibration_greatcircle_sv.py
* hopf_fibration_latitude_sv.py
* hopf_fibration_spiral_sv.py
* hopf_fibration_flower_sv.py


## Requirements

* Blender 2.8 (or later)
* sverchok add-on 0.6 (or later)
* animation nodes add-on 2.1.7 (or later)
## Author

asahidari

## Licence

[GPL 3](https://www.gnu.org/licenses/quick-guide-gplv3.html)