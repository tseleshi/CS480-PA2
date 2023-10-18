"""
Model our creature and wrap it in one class.
First version on 09/28/2021

:author: micou(Zezhou Sun)
:version: 2021.2.1

----------------------------------

Modified by Daniel Scrivener 09/2023
"""

from Component import Component
from Point import Point
import ColorType as Ct
from Shapes import Cube
from Shapes import Cylinder
import numpy as np


class ModelLinkage(Component):
    """
    Define our linkage model
    """

    ##### TODO 2: Model the Creature
    # Build the class(es) of objects that could utilize your built geometric object/combination classes. E.g., you could define
    # three instances of the cyclinder trunk class and link them together to be the "limb" class of your creature. 
    #
    # In order to simplify the process of constructing your model, the rotational origin of each Shape has been offset by -1/2 * dz,
    # where dz is the total length of the shape along its z-axis. In other words, the rotational origin lies along the smallest 
    # local z-value rather than being at the translational origin, or the object's true center. 
    # 
    # This allows Shapes to rotate "at the joint" when chained together, much like segments of a limb. 
    #
    # In general, you should construct each component such that it is longest in its local z-direction: 
    # otherwise, rotations may not behave as expected.
    #
    # Please see Blackboard for an illustration of how this behavior works.

    components = None
    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None):
        super().__init__(position, display_obj)

        # Create body parts of your creature using geometric primitives
        body = Cube(Point((0, 0, 0.5)), shaderProg, [1, 1, 1], Ct.DARKORANGE1, limb=False)
        head = Cube(Point((0, 0, 0.75)), shaderProg, [0.5, 0.5, 0.5], Ct.BLUE, limb=False)

        leg1 = self.createLeg(shaderProg, [0.5, 0.5, -0.5], Ct.RED)
        leg2 = self.createLeg(shaderProg, [-0.5, 0.5, -0.5], Ct.RED)
        leg3 = self.createLeg(shaderProg, [0.5, -0.5, -0.5], Ct.GREEN)
        leg4 = self.createLeg(shaderProg, [-0.5, -0.5, -0.5], Ct.GREEN)
        leg5 = self.createLeg(shaderProg, [0.5, 0, -0.5], Ct.YELLOW)
        leg6 = self.createLeg(shaderProg, [-0.5, 0, -0.5], Ct.YELLOW)


        # Position and attach body parts to build the creature
        self.addChild(body)
        body.addChild(head)
        body.addChild(leg1)
        body.addChild(leg2)
        body.addChild(leg3)
        body.addChild(leg4)
        body.addChild(leg5)
        body.addChild(leg6)

    def createLeg(self, shaderProg, position, color):
        leg = Cylinder(Point(position), shaderProg, [0.05, 0.05, 0.5], color)


         # Set rotational limits for leg joints
        leg.rotation_min = -45
        leg.rotation_max = 45
        
        return leg

     

        ##### TODO 4: Define creature's joint behavior
        # Requirements:
        #   1. Set a reasonable rotation range for each joint,
        #      so that creature won't intersect itself or bend in unnatural ways
        #   2. Orientation of joint rotations for the left and right parts should mirror each other.