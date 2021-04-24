from manim import *

class SimpleTexAndTexts(Scene):
    def construct(self):
        # Tex is a LaTeX plain text
        tex = Tex(r"This is \LaTeX, with a formula: $x^2$")
        # MathTex is Tex but with $$ $$
        math_tex = MathTex(r"\frac{\rm d}{\rm d\it x}f = f'(x)")
        # Sometimes it will be better to use
        # {n \over d}
        # instead
        # \frac{n}{d}

        text = Text("Normal text with PC fonts", font="Arial")

        Group(tex, math_tex, text).set(width=config.frame_width-1).arrange(DOWN)

        self.add(tex, math_tex, text)
        self.wait()

"""
  ____          _
 / ___|   _ ___| |_ ___  _ __ ___
| |  | | | / __| __/ _ \| '_ ` _ \
| |__| |_| \__ \ || (_) | | | | | |
 \____\__,_|___/\__\___/|_| |_| |_|
 _               _                       _       _
| |_ _____  __  | |_ ___ _ __ ___  _ __ | | __ _| |_ ___  ___
| __/ _ \ \/ /  | __/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \/ __|
| ||  __/>  <   | ||  __/ | | | | | |_) | | (_| | ||  __/\__ \
 \__\___/_/\_\___\__\___|_| |_| |_| .__/|_|\__,_|\__\___||___/
            |_____|               |_|
"""

# Example from example_scenes/advanced_tex_fonts.py

TemplateForFrenchCursive = TexTemplate(
    preamble=r"""
\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[T1]{fontenc}
\usepackage[default]{frcursive}
\usepackage[eulergreek,noplusnominus,noequal,nohbar,%
nolessnomore,noasterisk]{mathastext}
"""
)


def FrenchCursive(*tex_strings, **kwargs):
    return Tex(*tex_strings, tex_template=TemplateForFrenchCursive, **kwargs)


class TexFontTemplateManual(Scene):
    """An example scene that uses a manually defined TexTemplate() object to create
    LaTeX output in French Cursive font"""

    def construct(self):
        self.add(Tex("Tex Font Example").to_edge(UL))
        self.play(Write(FrenchCursive("$f: A \\longrightarrow B$").shift(UP)))
        self.play(Write(FrenchCursive("Behold! We can write math in French Cursive")))
        self.wait(1)
        self.play(
            Write(
                Tex(
                    "See more font templates at \\\\ http://jf.burnol.free.fr/showcase.html"
                ).shift(2 * DOWN)
            )
        )
        self.wait(2)

#  __  __           _     _____   __  __
# |  \/  |_   _ ___(_) __|_   _|__\ \/ /
# | |\/| | | | / __| |/ __|| |/ _ \\  /
# | |  | | |_| \__ \ | (__ | |  __//  \
# |_|  |_|\__,_|___/_|\___||_|\___/_/\_\

TemplateForMusicTeX = TexTemplate(
    preamble=r"""
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{mtxlatex}
\usepackage{graphicx}
"""
)

def MusicTeX(*tex_strings, **kwargs):
    return Tex(
        *tex_strings,
        tex_template=TemplateForMusicTeX,
        tex_environment="music", # <- Change enviroment
        **kwargs
    )

class MusicTeXExample(Scene):
    def construct(self):
        template = MusicTeX(r"""
            \parindent10mm
            \instrumentnumber{1}
            \setname1{Piano}
            \setstaffs1{2} 
            \generalmeter{\meterfrac44}
            \startextract 
            \Notes\ibu0f0\qb0{cge}\tbu0\qb0g|\hl j\en
            \Notes\ibu0f0\qb0{cge}\tbu0\qb0g|\ql l\sk\ql n\en
            \bar
            \Notes\ibu0f0\qb0{dgf}|\qlp i\en
            \notes\tbu0\qb0g|\ibbl1j3\qb1j\tbl1\qb1k\en
            \Notes\ibu0f0\qb0{cge}\tbu0\qb0g|\hl j\en
            \zendextract
        """)
        template.set(width=config["frame_width"]-1)
        self.play(
            Write(template)
        )
        self.wait(2)

"""
  ____      _                    _   _               ___     _            _
 / ___|___ | | ___  _ __ ___  __| | | |_ _____  __  ( _ )   | |_ _____  _| |_ ___
| |   / _ \| |/ _ \| '__/ _ \/ _` | | __/ _ \ \/ /  / _ \/\ | __/ _ \ \/ / __/ __|
| |__| (_) | | (_) | | |  __/ (_| | | ||  __/>  <  | (_>  < | ||  __/>  <| |_\__ \
 \____\___/|_|\___/|_|  \___|\__,_|  \__\___/_/\_\  \___/\/  \__\___/_/\_\\__|___/
"""

class TexAndMathTextColors(Scene):
    def construct(self):
        # If the texts are simple, that is, 
        # without fractions, roots, subscripts and/or superscripts,
        # it is possible to color the text as follows.
        tex = Tex(
            r"This is \LaTeX, with a formula: $x^2$",
            tex_to_color_map={
                r"\LaTeX": RED,
                "formula": ORANGE,
                "$x^2$": TEAL,
            }
        )
        math_tex = MathTex(
            r"\frac{\rm d}{\rm d\it x}f = f'(x)",
            # You cannot use "d": RED, try it
            tex_to_color_map={
                "f'(x)": YELLOW,
                # "d": RED,
            }
        )
        text = Text(
            "Normal text with PC fonts",
            font="Arial",
            # These arguments can present problems in
            # versions prior to 0.5.0, MarkupText class
            # can be used instead of Text if text with
            # alot of decorations is needed.
            # Use Text for simple texts.
            t2c={
                "Normal": RED,
            },
            t2w={
                "text": BOLD,
            },
            t2s={
                "fonts": ITALIC
            }
        )

        Group(tex, math_tex, text).set(width=config.frame_width-1).arrange(DOWN)

        self.add(tex, math_tex, text)
        self.wait()

"""
 __  __            _              _____         _
|  \/  | __ _ _ __| | ___   _ _ _|_   _|____  _| |_
| |\/| |/ _` | '__| |/ / | | | '_ \| |/ _ \ \/ / __|
| |  | | (_| | |  |   <| |_| | |_) | |  __/>  <| |_
|_|  |_|\__,_|_|  |_|\_\\__,_| .__/|_|\___/_/\_\\__|
                             |_|
"""


class BasicMarkupExample(Scene):
    def construct(self):
        text1 = MarkupText("<b>foo</b> <i>bar</i> <b><i>foobar</i></b>")
        text2 = MarkupText("<s>foo</s> <u>bar</u> <big>big</big> <small>small</small>")
        text3 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
        text4 = MarkupText("type <tt>help</tt> for help")
        text5 = MarkupText(
            '<span underline="double">foo</span> <span underline="error">bar</span>'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)

class ColorExample(Scene):
    def construct(self):
        text1 = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        text2 = MarkupText("nice gradient", gradient=(BLUE, GREEN))
        text3 = MarkupText(
            'nice <gradient from="RED" to="YELLOW">intermediate</gradient> gradient',
            gradient=(BLUE, GREEN),
        )
        text4 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW">causing trouble</gradient> here'
        )
        text4s = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1">causing trouble</gradient> here'
        )
        text5 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1">defeated</gradient> with offset'
        )
        text6 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1">floating</gradient> inside'
        )
        text7 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1,1">floating</gradient> inside'
        )
        group = VGroup(text1, text2, text3, text4, text4s, text5, text6, text7).arrange(DOWN)
        self.add(group)

class UnderlineExample(Scene):
    def construct(self):
        text1 = MarkupText(
            '<span underline="double" underline_color="green">bla</span>'
        )
        text2 = MarkupText(
            '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        )
        text3 = MarkupText(
            '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-1">aabb</gradient>y'
        )
        text4 = MarkupText(
            '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        )
        text5 = MarkupText(
            '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-2">aabb</gradient>y'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)

"""
  ____          _      __  __       _     _           _
 / ___|___   __| | ___|  \/  | ___ | |__ (_) ___  ___| |_
| |   / _ \ / _` |/ _ \ |\/| |/ _ \| '_ \| |/ _ \/ __| __|
| |__| (_) | (_| |  __/ |  | | (_) | |_) | |  __/ (__| |_
 \____\___/ \__,_|\___|_|  |_|\___/|_.__// |\___|\___|\__|
                                       |__/
"""

class CodeFromString(Scene):
    def construct(self):
        code = '''
        from manim import Scene, Square

        class FadeInSquare(Scene):
            def construct(self):
                s = Square()
                self.play(FadeIn(s))
                self.play(s.animate.scale(3))
                self.wait()'''
        rendered_code = Code(
            code=code,
            tab_width=4,
            background="window",
            language="Python",
            font="Monospace",
            style="monokai"
        )
        self.draw_code_all_lines_at_a_time(rendered_code)
        self.wait()

    def draw_code_all_lines_at_a_time(self, code, **kwargs):
        self.play(LaggedStart(*[
                Write(code[i])
                for i in range(len(code))
            ]),
            **kwargs
        )

