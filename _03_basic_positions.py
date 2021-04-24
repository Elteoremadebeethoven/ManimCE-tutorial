from manim import *

# Source code:
# https://github.com/Elteoremadebeethoven/MyAnimations/blob/master/screen_grid/screen_grid_mce.py

class Grid(VGroup):
    def __init__(self, rows, columns, height=6, width=6,**kwargs):
        self.height_g = height
        self.width_g = width
        super().__init__(**kwargs)

        x_step = self.width_g / columns
        y_step = self.height_g / rows

        for x in np.arange(0, self.width_g + x_step, x_step):
            self.add(Line(
                [x - self.width_g / 2., -self.height_g / 2., 0],
                [x - self.width_g / 2., self.height_g / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width_g / 2., y - self.height_g / 2., 0],
                [self.width_g / 2., y - self.height_g / 2., 0]
            ))


class ScreenGrid(VGroup):
    def __init__(
            self,
            rows=8,
            columns=14,
            height=config.frame_height,
            width=14,
            grid_stroke=0.5,
            grid_color=WHITE,
            axis_color=RED,
            axis_stroke=2,
            labels_scale=0.25,
            labels_buff=0,
            number_decimals=2,
            **kwargs):
        self.height_g = height
        self.width_g = width
        self.grid_stroke = grid_stroke
        self.grid_color = grid_color
        self.axis_color = axis_color
        self.axis_stroke = axis_stroke
        self.labels_scale = labels_scale
        self.labels_buff = labels_buff
        self.number_decimals = number_decimals
        super().__init__(**kwargs)
        grid = Grid(width=self.width_g, height=self.height_g, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width_g / 2, - self.height_g / 2, 0))
        vector_si = ORIGIN + np.array((- self.width_g / 2, self.height_g / 2, 0))
        vector_sd = ORIGIN + np.array((self.width_g / 2, self.height_g / 2, 0))

        axes_x = Line(LEFT * self.width_g / 2, RIGHT * self.width_g / 2)
        axes_y = Line(DOWN * self.height_g / 2, UP * self.height_g / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width_g / columns
        divisions_y = self.height_g / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)


class CoordScreen(Scene):
    def construct(self):
        screen_grid = ScreenGrid()
        dot = Dot([1, 1, 0])
        self.add(screen_grid)
        self.play(FadeIn(dot))
        self.wait()

"""
 ____                                 _ _                          _
/ ___|  ___ _ __ ___  ___ _ __     __| (_)_ __ ___   ___ _ __  ___(_) ___  _ __  ___
\___ \ / __| '__/ _ \/ _ \ '_ \   / _` | | '_ ` _ \ / _ \ '_ \/ __| |/ _ \| '_ \/ __|
 ___) | (__| | |  __/  __/ | | | | (_| | | | | | | |  __/ | | \__ \ | (_) | | | \__ \
|____/ \___|_|  \___|\___|_| |_|  \__,_|_|_| |_| |_|\___|_| |_|___/_|\___/|_| |_|___/
"""

class BasicPositions(Scene):
    def construct(self):
        dot_center = Dot(color=WHITE)      # ORIGIN: [0,0,0] by default
        dot_left  = Dot(LEFT,color=RED)    # [-1,0,0]
        dot_right = Dot(RIGHT,color=BLUE)  # [1,0,0]
        dot_up    = Dot(UP,color=GREEN)    # [0,1,0]
        dot_down  = Dot(DOWN,color=ORANGE) # [0,-1,0]
        dot_2_3   = Dot([2,3,0],color=TEAL)# [2,3,0]

        logger.info(f"frame_width: {config.frame_width}")
        logger.info(f"frame_height: {config.frame_height}")

        self.add(
            # ScreenGrid(),
            dot_center,
            dot_left,
            dot_right,
            dot_up,
            dot_down,
            dot_2_3,
        )
        self.wait()

"""
    _    _               _       _                         _ _   _
   / \  | |__  ___  ___ | |_   _| |_ ___   _ __   ___  ___(_) |_(_) ___  _ __  ___
  / _ \ | '_ \/ __|/ _ \| | | | | __/ _ \ | '_ \ / _ \/ __| | __| |/ _ \| '_ \/ __|
 / ___ \| |_) \__ \ (_) | | |_| | ||  __/ | |_) | (_) \__ \ | |_| | (_) | | | \__ \
/_/   \_\_.__/|___/\___/|_|\__,_|\__\___| | .__/ \___/|___/_|\__|_|\___/|_| |_|___/
                                          |_|
"""

class EdgesAndCorners(Scene):
    def construct(self):
        square = Square()
        square.to_edge(UR)               # UP + RIGHT

        triangle = Triangle()
        triangle.to_edge(DL,buff=0.1)   # DOWN + LEFT

        dot_up   = Dot(color=RED)
        dot_up.to_edge(UP)

        dot_down = Dot(color=BLUE)
        dot_down.to_edge(DOWN,buff=2)

        self.add(
            square,
            triangle,
            dot_up,
            dot_down
        )
        self.wait()

"""
 ____      _       _   _                             _ _   _
|  _ \ ___| | __ _| |_(_)_   _____   _ __   ___  ___(_) |_(_) ___  _ __  ___
| |_) / _ \ |/ _` | __| \ \ / / _ \ | '_ \ / _ \/ __| | __| |/ _ \| '_ \/ __|
|  _ <  __/ | (_| | |_| |\ V /  __/ | |_) | (_) \__ \ | |_| | (_) | | | \__ \
|_| \_\___|_|\__,_|\__|_| \_/ \___| | .__/ \___/|___/_|\__|_|\___/|_| |_|___/
                                    |_|
"""


class ShiftMethod(Scene):
    """
    The shift method moves the object 
    based on the current position of 
    the object.
    """
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait()
        circle.shift(RIGHT)
        self.wait()
        circle.shift(RIGHT)
        self.wait()
        circle.shift(DOWN)
        self.wait()
        circle.shift(LEFT)
        self.wait()

class MoveToMethod1(Scene):
    """
    The move_to method moves the object
    taking as reference the origin or
    some particular point
    """
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait()
        circle.move_to(RIGHT)
        self.wait()
        circle.move_to(RIGHT)
        self.wait()
        circle.move_to(DOWN)
        self.wait()
        circle.move_to([2,3,0])
        self.wait()
    
class MoveToMethod2(Scene):
    def construct(self):
        circle = Circle()
        dot_1 = Dot([1,3,0],color=ORANGE)
        dot_2 = Dot([-2,-3,0],color=BLUE)
        self.add(circle,dot_1,dot_2)
        self.wait()
        circle.move_to(dot_1)
        self.wait()
        circle.move_to(dot_2)
        self.wait()
        circle.move_to(dot_2.get_center()+RIGHT)
        self.wait()

class NextTo(Scene):
    """
    next_to references the edges of an 
    object as a reference to locate 
    another object.
    """
    def construct(self):
        text = Text("Hello world")
        text.shift(LEFT+2*UP)

        left_dot = Dot().next_to(text,LEFT)
        right_dot = Dot().next_to(text,RIGHT,buff=0)
        down_dot = Dot().next_to(text,DOWN,buff=1)

        self.add(text, left_dot, right_dot,down_dot)
        self.wait()

class BordersAndCorners(Scene):
    def construct(self):
        text = Text("Hello world").scale(2)
        d1 = Dot(text.get_corner(UL))
        d2 = Dot(text.get_bottom())
        d3 = Dot(text.get_top())
        d4 = Dot(text.get_left())
        d5 = Dot(text.get_right())

        self.add(text,d1,d2,d3,d4,d5)
        self.wait()

"""
    _    _ _
   / \  | (_) __ _ _ __
  / _ \ | | |/ _` | '_ \
 / ___ \| | | (_| | | | |
/_/   \_\_|_|\__, |_| |_|
             |___/
"""

class Align(Scene):
    def construct(self):
        rect = Rectangle(width=6,height=4,color=RED)
        a = Text("A")
        b = Text("B")
        c = Text("C")

        a.align_to(rect,LEFT)
        b.align_to(rect,UP)
        c.align_to(rect,UR)

        self.add(rect,a,b,c)
        self.wait()

"""
 ____       _        _   _
|  _ \ ___ | |_ __ _| |_(_) ___  _ __  ___
| |_) / _ \| __/ _` | __| |/ _ \| '_ \/ __|
|  _ < (_) | || (_| | |_| | (_) | | | \__ \
|_| \_\___/ \__\__,_|\__|_|\___/|_| |_|___/
"""

class Rotations(Scene):
    def construct(self):
        a = Text("A")
        a.shift(LEFT*3)
        a.rotate(30*DEGREES) #or .rotate(PI/6)

        dot = Dot(RIGHT)
        b = Text("B")
        b.rotate(PI/2,about_point=dot.get_center())

        self.add(a,b,dot)
        self.wait()
