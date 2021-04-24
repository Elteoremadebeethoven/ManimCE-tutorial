from manim import *

# Docs
# https://docs.manim.community/en/stable/tutorials/configuration.html

"""
                                   DEFAULTS
=================================================================================
-p          PREVIEW                       Open the scene with your media player

-a          RENDER ALL SCENES
            IN THE FILE
            (DON'T USE IT WITH -p FLAG)

-ql         LOW QUALITY         480p    15 fps
-qm         MEDIUM QUALITY      720p    30 fps
-qh         HIGHT QUALITY       1080p   60 fps
-qp         PRODUCTION QUALITY  1440p   60 fps
-qk         4K                  2160p   60 fps
-s          RENDER PNG OF THE
            LAST FRAME

Shorts:
    -pql    PREVIEW IN LOW QUALITY
    -pqm    PREVIEW IN MEDIUM QUALITY
    -pqh    PREVIEW IN HIGHT QUALITY
    -pqp    PREVIEW IN PRODUCTION QUALITY
    -pqk    PREVIEW IN 4K QUALITY
    -ps     RENDER LAST FRAME AS PNG

                                   CUSTOM
=================================================================================
-r H,W      RENDER WITH CUSTOM
            DIMENSIONS

            Example: -r 500,500

--fps <NUMBER>
            Example: --fps 20

-o FILE_NAME

CLICK (Not all properties works fine yet)
-----------------------------------
[CLI]
# my config file
#save_as_gif = True
#background_color = WHITE
-----------------------------------


                                   Examples
=================================================================================
RENDER 30 fps at 480p:
    Option 1:
        -qm -r 854,480
    Option 2:
        -ql --fps 30
"""

# aspect_ratio = 16 / 9

# config.background_color = WHITE
# config.frame_rate = 20
# config.pixel_height = 800
# config.pixel_width = int(config.pixel_height * aspect_ratio)

class Scene1(Scene):
    def construct(self):
        t = Text("SCENE 1")
        self.play(Write(t))
        self.wait()

class Scene2(Scene):
    def construct(self):
        t = Text("SCENE 2")
        self.play(FadeIn(t))
        self.wait()

class Scene3(Scene):
    def construct(self):
        t = Text("SCENE 3")
        self.play(GrowFromCenter(t))
        self.wait()