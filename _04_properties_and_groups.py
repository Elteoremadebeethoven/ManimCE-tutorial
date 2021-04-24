from manim import *

class VMobjectProperties(Scene):
    def construct(self):
        square = Square(
            side_length=4,
            # All VMobjects have
            color=YELLOW,
            stroke_width=5,
            stroke_opacity=0.8,
            stroke_color=PINK,
            fill_color=TEAL,
            fill_opacity=0.4
        )
        square.to_edge(LEFT)

        circle = Circle(radius=3)
        # All VMobjects have:
        circle.set_fill(color=RED,opacity=0.5)
        circle.set_stroke(color=YELLOW,opacity=0.8,width=9)
        circle.to_edge(RIGHT)

        self.add(
            square,
            circle
        )

class GroupMobjects(Scene):
    def construct(self):
        group = Group(
            Circle(),
            Triangle(),
            # Download image:
            # curl https://raw.githubusercontent.com/ManimCommunity/manim/master/logo/cropped.png --output image.png
            ImageMobject("image")
        )
        group.arrange(
            RIGHT, # Direction
            aligned_edge=UP,
            buff=0.3 # Separation
        )
        # old way: group.set_width(FRAME_WIDTH - 1)
        group.width = config.frame_width - 1
        self.add(group)
        self.wait()

class VGroupMobjects(Scene):
    def construct(self):
        vgroup = VGroup(
            Square(),
            Triangle(),
            Circle()
        )
        vgroup.arrange(
            RIGHT,
            aligned_edge=DOWN
        )
        # You cannot do this with simple Group
        vgroup.set_style(
            fill_color=ORANGE,
            fill_opacity=0.8,
            stroke_color=PINK,
            stroke_opacity=0.8,
            stroke_width=20
        )
        vgroup.width = config.frame_width - 1

        self.add(vgroup)
        self.wait()

class VGroupMobjectsListComprehension(Scene):
    def construct(self):
        vg = VGroup(
            VGroup(*[Square() for _ in range(6)])
                .arrange(RIGHT)
                .set_color_by_gradient(RED,TEAL)
                .set(width=config.frame_width-1),
            VGroup(*[RegularPolygon(n) for n in range(3,9)])
                .arrange(RIGHT)
                .set_color_by_gradient(YELLOW,ORANGE)
                .set(width=config.frame_width-1),
            VGroup(*[
                    VMClass().set(height=0.7) 
                    for VMClass in [Circle,Annulus,Ellipse,Triangle]
                ])
                .arrange(RIGHT)
                .set_color_by_gradient(BLUE,GREEN)
                .set(width=config.frame_width-1),
        )
        # width and height can be managed as normal properties
        # Use Mobject().set(width=WIDTH)
        # Use Mobject().set(height=HEIGHT)

        vg.arrange(DOWN,aligned_edge=LEFT)

        self.add(vg)