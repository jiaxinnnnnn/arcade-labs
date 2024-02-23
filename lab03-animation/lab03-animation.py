import arcade

def draw_the_sea():
    # mar
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.MIDNIGHT_BLUE)

def draw_the_moon():
    # luna
    arcade.draw_arc_filled(300, 300, 200, 200, arcade.csscolor.LEMON_CHIFFON, 0, 180)

def draw_the_stars(posx, posy, tamstar,longstar):

    # estrella fugaz
    arcade.draw_circle_filled(posx, posy, tamstar, arcade.csscolor.LEMON_CHIFFON)
    # cola estrella fugaz
    arcade.draw_triangle_filled(posx+longstar, posy, posx, posy+tamstar-1, posx, posy-tamstar-1, arcade.csscolor.LEMON_CHIFFON)


def draw_cola(x,y,alto, ancho):
    # cola
    arcade.draw_triangle_filled(x, y+(alto/2), x-(ancho/2), y-(alto/2), x+(ancho/2), y-(alto/2), arcade.csscolor.BLACK)
    #cola aletas
    arcade.draw_ellipse_filled(x-(ancho), y+(alto/2), ancho*2, alto/4, arcade.csscolor.BLACK, 0)
    arcade.draw_ellipse_filled(x+(ancho), y+(alto/2), ancho*2, alto/4, arcade.csscolor.BLACK, 0)

    # espuma cola
    arcade.draw_ellipse_filled(x-(ancho/2), y-(alto/2), ancho*2, alto/7, arcade.csscolor.CADET_BLUE, 3)
    arcade.draw_ellipse_filled(x+(ancho/2), y-(alto/2), ancho*2, alto/7, arcade.csscolor.CADET_BLUE, 3)

def on_draw(delta_time):
    arcade.start_render()


    draw_cola(on_draw.cola1_x, 140, 200,100)
    draw_cola(400,400,200,100)

    on_draw.cola1_x -= 5



on_draw.cola1_x = 600




def main():
    arcade.open_window(600, 600, "Drawing With Funtions")

    arcade.set_background_color(arcade.csscolor.BLUE)



#    draw_the_sea()
#
 #   draw_the_moon()

  #  draw_the_stars(300,300,50, 300)
    #draw_cola(400,400,200,100)

    arcade.schedule(on_draw, 1 / 60)


    # finish
    #arcade.finish_render()

    arcade.run()

main()

