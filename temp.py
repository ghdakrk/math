from manim import *


# manim temp.py IMG -pqm

# class IMG(Scene):
#     def construct(self):

#         icon = ImageMobject("img.jpg").scale(2.0).to_edge(DL)
#         box = SurroundingRectangle(icon, color=BLUE, fill_opacity=0.2, fill_color=RED, buff=2)

#         self.play(Create(box), run_time=3)
#         self.play(FadeIn(icon), run_time=3)
#         self.wait()
#         self.play(icon.animate.to_edge(UL).scale(0.8), run_time=3)
#         self.wait()
        


# manim temp.py UpdaterGraphing -pqm 
# class UpdaterGraphing(Scene):
#     def construct(self):
#         k = ValueTracker(-6)
#         ax = (
#             Axes(x_range = [-8,8,1], y_range = [-2,2,1], 
#             x_length=10, y_length=6).to_edge(DOWN).add_coordinates()
#             ).set_color(WHITE)

#         func = ax.get_graph(lambda x : np.sin(x), x_range=[-8,8], color=BLUE)
#         slope = always_redraw(
#                     lambda: ax.get_secant_slope_group(
#                         x=k.get_value(), 
#                         graph= func, dx=0.01, 
#                         secant_line_color=GREEN, 
#                         secant_line_length=3,)) 
        
#         pt = always_redraw(lambda: Dot().move_to(ax.c2p(k.get_value(), func.underlying_function(k.get_value()))))

#         self.play(Create(ax), run_time=3)
#         self.play(Create(func), run_time=3)
#         self.play(Create(pt), run_time=2)
#         self.play(Create(slope), run_time=3)
#         self.wait()
#         self.play(k.animate.set_value(6), run_time=6)
#         self.wait()

# manim temp.py graphing -pqm 
# class graphing(Scene):
#     def construct(self):
        
#         plane = (NumberPlane(x_range = [-4,4,2], x_length=8, y_range=[0,16,4], y_length=12)
#         .to_edge(DOWN).add_coordinates())
#         labels = plane.get_axis_labels(x_label = 'x', y_label = 'f(x)')

#         parab = plane.get_graph(lambda x: x**2, x_range=[-4,4], color=GREEN)
#         func_label = (MathTex("f(x)={x}**{2}").scale(0.6)
#                       .next_to(parab, RIGHT, buff=0.5).set_color(GREEN))

#         area = plane.get_riemann_rectangles(graph=parab, x_range=[-2,3], dx=0.2, stroke_width=0.1, stroke_color=WHITE) 
        

#         self.play(DrawBorderThenFill(plane))
#         self.play(Create(VGroup(labels, parab, func_label)), run_time=8)
#         self.wait()
#         self.play(Create(area))
#         self.wait()




# manim temp.py ValueTrackers -pqm
# class ValueTrackers(Scene):
    # def construct(self):
        
    #     k = ValueTracker(7)

    #     num = always_redraw(lambda: DecimalNumber().set_value(k.get_value())) 

    #     self.play(FadeIn(num))
    #     self.wait()
    #     self.play(k.animate.set_value(0), run_time=3, rate_functions=smooth)





# manim temp.py Updaters -pqm
# class Updaters(Scene):
#     def construct(self):
#         num = MathTex('ln(2)')
#         box1 = always_redraw(lambda: SurroundingRectangle(num, color=BLUE, fill_opacity=0.4, fill_color=RED, buff=2)) 
#         box2 = SurroundingRectangle(num, color=BLUE, fill_opacity=0.4, fill_color=BLUE, buff=2)

#         self.play(Create(num), run_time=1)
#         self.play(Create(VGroup(box1, box2)), run_time=5)
#         self.play(box1.animate.to_edge(LEFT), run_time=2)
#         self.play(box2.animate.to_edge(RIGHT), run_time=2)
#         self.play(num.animate.shift(UL*3.5), run_time=2)
    
#         self.wait()



# class Getters(Scene):
#     def construct(self):
        
#         rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)
#         circ = Circle().to_edge(DOWN)
#         arrow = always_redraw(lambda : Line(start = rect.get_center(), end=circ.get_center(), buff=0.2).add_tip()) 

#         self.play(Create(VGroup(rect, circ, arrow), run_time=7))
#         self.wait()
#         self.play(rect.animate.to_edge(UR), run_time=3)
#         self.play(circ.animate.to_edge(DL), run_time=3)
#         self.wait()
#         self.play(rect.animate.scale(0.5), run_time=3)
#         self.wait()



# class Library(Scene):
#     def construct(self):
#         ax = Axes()
#         self.play(Create(ax)) 

# manim temp.py Kepler -pqm
# import math
# import manim.utils.color as c

# ellipse = Ellipse(width=2, height=1.5)
# planet = Dot(color=c.BLUE)
# sun = Dot(radius=0.15, color=c.YELLOW)
# sun2 = sun.copy().shift(np.array([-0.661, 0, 0]))
# planet2 = planet.copy().shift(RIGHT)


# class Kepler(Scene):
#     def construct(self):
#         self.play(GrowFromCenter(ellipse))
#         self.add(planet)
#         self.play(Transform(planet, planet2))
#         self.add(sun)
#         self.play(Transform(sun, sun2))
#         self.play(MoveAlongPath(planet, ellipse), run_time=7)


# def vis_viva(t: float) -> float:
#     pla_x = planet.get_x()
#     pla_y = planet.get_y()
#     sun_x = sun.get_x()
#     sun_y = sun.get_y()
#     r = math.sqrt((pla_x - sun_x) ** 2 + (pla_y - sun_y) ** 2)
#     a = max(ellipse.width, ellipse.height) / 2
#     return 2 / r - 1 / a


# manim temp.py Test1 -pqm 

class Test1(Scene):
    def construct(self):
        sun = Circle(radius=3, color=WHITE, fill_color=RED, fill_opacity=0.5)
        earth = Circle(radius=0.6, color=BLUE, fill_color=GREEN, fill_opacity=0.75)
        arrow = always_redraw(lambda : Line(start = sun.get_center(), end=earth.get_center(), buff=0.2))


        self.play(Create(VGroup(sun, earth)), run_time=4)
        self.wait()
        
        self.play(sun.animate.to_edge(LEFT), earth.animate.to_edge(RIGHT), run_time=4)
        self.wait(2)
        self.play(FadeIn(arrow), run_time=1)
        self.wait(2)
        self.play(FadeOut(arrow), run_time=3)
        self.wait(2)

        self.play(sun.animate.scale(2), run_time=4)
        self.play(earth.animate.scale(0.9), run_time=4)
        self.wait(4)

        self.play(sun.animate.scale(0.4), earth.animate.scale(0.5), run_time=4)
        self.wait(3)

        self.play(sun.animate.move_to(RIGHT), earth.animate.shift(LEFT*1), run_time=3)
        self.wait()
        ellipse = Ellipse(width=10, height=7)
        self.play(MoveAlongPath(earth, ellipse), rate_func=linear, run_time=4)
        self.play(MoveAlongPath(earth, ellipse), rate_func=linear, run_time=4)
        self.play(MoveAlongPath(earth, ellipse), rate_func=linear, run_time=4)
        self.play(MoveAlongPath(earth, ellipse), rate_func=linear, run_time=4)
        self.wait(7)

        arc1 = Arc(radius=5, start_angle=0, angle=PI/6)
        arc2 = Arc(radius=5, start_angle=0, angle=PI/4)
        self.play(MoveAlongPath(earth, arc1), rate_func=linear, run_time=4)
        self.wait(6)
        self.play(MoveAlongPath(earth, arc1), rate_func=linear, run_time=5)
        self.wait(8)

        self.play(earth.animate.shift(DOWN*2.5, LEFT*4.5), sun.animate.shift(RIGHT*4), run_time=3)
        self.wait(3)
        ellipse1 = Ellipse(width=10, height=6)
        self.play(MoveAlongPath(sun, ellipse1), rate_func=linear, run_time=8)
        self.play(MoveAlongPath(sun, ellipse1), rate_func=linear, run_time=8)
        self.wait(5)

# class Test(Scene):
#     def construct(self):
#         name = Tex('Amedee').to_edge(UL, buff=0.5)
#         sq = Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.75).shift(LEFT * 3)
#         tri = Triangle().scale(0.6).to_edge(DR)

#         self.play(Write(name))
#         self.play(DrawBorderThenFill(sq), run_time=2)
#         self.play(Create(tri))
#         self.wait()

#         self.play(name.animate.to_edge(UR), run_time=2)
#         self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)
#         self.wait()
