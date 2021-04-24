from manim import *
import itertools as it

class TexWithSingleStringArrayFail(Scene):
    def construct(self):
        tex_string = "Single string"
        math_text_string = "x + y = 3"

        tex = Tex(tex_string)
        math_text = MathTex(math_text_string)

        logger.info(f"len(tex_string): {len(tex_string)}")
        logger.info(f"len(math_text_string): {len(math_text_string)}")
        print()
        logger.info(f"len(tex): {len(tex)}")
        logger.info(f"len(math_text): {len(math_text)}")

        vg = VGroup(tex,math_text).scale(3).arrange(DOWN)

        self.add(vg)
        self.wait()

class TexWithSingleStringArray(Scene):
    def construct(self):
        tex_string = "Single string"
        math_text_string = "x + y = 3"

        tex = Tex(tex_string)[0] # <- Add [0]
        math_text = MathTex(math_text_string)[0] # <- Add [0]

        logger.info(f"len(tex_string): {len(tex_string)}")
        logger.info(f"len(math_text_string): {len(math_text_string)}")
        print()
        logger.info(f"len(tex): {len(tex)}")
        logger.info(f"len(math_text): {len(math_text)}")

        vg = VGroup(tex,math_text).scale(3).arrange(DOWN)

        self.add(vg)
        self.wait()

def get_tex_indexes(
        tex,
        number_config={"height":0.28},
        colors=[RED,TEAL,PURPLE,GREEN,BLUE],
        funcs=[lambda mob,tex: mob.next_to(tex,DOWN,buff=0)]
    ):
    numbers = VGroup()
    colors = it.cycle(colors)
    for i,s in enumerate(tex):
        n = Text(f"{i}",color=next(colors),**number_config)
        for f in funcs:
            f(n,s)
        numbers.add(n)
    return numbers

class ShowIndexesOfTex(Scene):
    def construct(self):
        tex_string = "Single string"
        math_text_string = "x + y = 3"

        tex = Tex(tex_string) # <- Add [0]
        math_text = MathTex(math_text_string) # <- Add [0]

        vg = VGroup(tex,math_text).scale(3).arrange(DOWN,buff=1)

        n1 = get_tex_indexes(tex[0])
        n2 = get_tex_indexes(math_text[0])

        tex[0][3].set_color(ORANGE)
        math_text[0][4].set_color(ORANGE)

        self.add(vg,n1,n2)
        self.wait()

class MultipleTexString(Scene):
    def construct(self):
        tex_string = ["Multiple ","tex ","string"]
        math_text_string = ["x+","y","=","3"]

        tex = Tex(*tex_string) # <- Add [0]
        math_text = MathTex(*math_text_string) # <- Add [0]

        vg = VGroup(tex,math_text).scale(3).arrange(DOWN,buff=1)

        n1 = get_tex_indexes(tex)
        n2 = get_tex_indexes(math_text)

        f = lambda mob,tex: mob.next_to(tex,UP,buff=0)
        n_1_1 = get_tex_indexes(tex[0],funcs=[f])
        n_1_2 = get_tex_indexes(tex[1],funcs=[f])
        n_1_3 = get_tex_indexes(tex[2],funcs=[f])

        tex[0][2].set_color(TEAL)
        tex[1][1].set_color(ORANGE)
        tex[2][3].set_color(PINK)

        math_text[0].set_color(PURPLE)

        self.add(vg,n1,n2,n_1_1,n_1_2,n_1_3)
        self.wait()

