import arcade

arcade.open_window(600, 600, "Drawing Example")

#color fondo
arcade.set_background_color(arcade.csscolor.BLUE)

arcade.start_render()



#arcade.draw_lrtb_rectangle_filled(0(izq), 599(der), 300(arriba), 0(abajo), arcade.csscolor.GREEN)


#arcade.draw_rectangle_filled(100(centrox), 320(centroy), 20(ancho), 60(alto), arcade.csscolor.SIENNA(color))


#arcade.draw_circle_filled(100(centrox), 350(centroy), 30(radio), arcade.csscolor.DARK_GREEN)


#arcade.draw_ellipse_filled(300(centro x), 300(centroy), 350(ancho), 200(alto), arcade.csscolor.RED, 3)


#arcade.draw_triangle_filled(400, 400(punto a x,y), 370, 320(punto b x,y), 430, 320(punto c x,y), arcade.csscolor.DARK_GREEN)

#arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)



#mar
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.MIDNIGHT_BLUE)

#luna
arcade.draw_arc_filled(300, 300, 200, 200, arcade.csscolor.LEMON_CHIFFON, 0, 180)

#sombraluna
arcade.draw_rectangle_filled(300,290 , 200, 10, arcade.csscolor.ROYAL_BLUE)
arcade.draw_rectangle_filled(300, 275, 180, 10, arcade.csscolor.ROYAL_BLUE)
arcade.draw_rectangle_filled(300, 260, 170, 10, arcade.csscolor.ROYAL_BLUE)
arcade.draw_rectangle_filled(300, 245, 140, 10, arcade.csscolor.ROYAL_BLUE)
arcade.draw_rectangle_filled(300, 230, 110, 10, arcade.csscolor.ROYAL_BLUE)
arcade.draw_rectangle_filled(300, 215, 90, 10, arcade.csscolor.ROYAL_BLUE)
arcade.draw_rectangle_filled(300, 200, 55, 10, arcade.csscolor.ROYAL_BLUE)
arcade.draw_rectangle_filled(300, 185, 38, 10, arcade.csscolor.ROYAL_BLUE)
arcade.draw_rectangle_filled(300, 170, 23, 10, arcade.csscolor.ROYAL_BLUE)
arcade.draw_rectangle_filled(300, 155, 15, 10, arcade.csscolor.ROYAL_BLUE)

#cola
arcade.draw_triangle_filled(500,310, 490, 280, 510, 280, arcade.csscolor.BLACK)
#cola2
arcade.draw_ellipse_filled(483,307, 35, 10, arcade.csscolor.BLACK,10)
arcade.draw_ellipse_filled(522,305,45, 12, arcade.csscolor.BLACK,3)

#estela cola
#arcade.draw_rectangle_filled(500, 280, 40, 3, arcade.csscolor.ROYAL_BLUE)
arcade.draw_ellipse_filled(495,278,25, 7, arcade.csscolor.CADET_BLUE,3)
arcade.draw_ellipse_filled(509,278,27, 8, arcade.csscolor.CADET_BLUE,3)
#espuma cola
arcade.draw_circle_filled(530, 280, 2, arcade.csscolor.LEMON_CHIFFON)
arcade.draw_circle_filled(512, 275, 2, arcade.csscolor.LEMON_CHIFFON)
arcade.draw_circle_filled(508, 278, 2, arcade.csscolor.LEMON_CHIFFON)
arcade.draw_circle_filled(490, 280, 2, arcade.csscolor.LEMON_CHIFFON)


#estrella fugaz

arcade.draw_circle_filled(240, 550, 5, arcade.csscolor.LEMON_CHIFFON)
arcade.draw_circle_filled(255, 565, 6, arcade.csscolor.LEMON_CHIFFON)
arcade.draw_circle_filled(245, 530, 5, arcade.csscolor.LEMON_CHIFFON)
#cola estrella fugaz
arcade.draw_triangle_filled(440,450, 244, 554, 236, 546, arcade.csscolor.LEMON_CHIFFON)
arcade.draw_triangle_filled(460,465, 259, 569, 251, 561, arcade.csscolor.LEMON_CHIFFON)
arcade.draw_triangle_filled(445,430, 249, 534, 241, 526, arcade.csscolor.LEMON_CHIFFON)

#faro

arcade.draw_lrtb_rectangle_filled(0, 100, 330, 0, arcade.csscolor.BLACK)
arcade.draw_circle_filled(50, 485, 10, arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(50, 290, 125, 20, arcade.csscolor.BLACK)
arcade.draw_arc_filled(50, 430, 100, 100, arcade.csscolor.BLACK, 0, 180)
#ventana faro
arcade.draw_lrtb_rectangle_filled(0, 100, 429, 340, arcade.csscolor.STEEL_BLUE)
arcade.draw_lrtb_rectangle_filled(0, 100, 340, 300, arcade.csscolor.DARK_SLATE_GRAY)
#bombilla faro
arcade.draw_ellipse_filled(50,385,25, 70, arcade.csscolor.GOLD,0)





#estela faro

arcade.draw_lrtb_rectangle_filled(100, 200, 430, 340, arcade.csscolor.CORNFLOWER_BLUE)
arcade.draw_triangle_filled(100,430, 200, 430, 200, 450, arcade.csscolor.CORNFLOWER_BLUE)
arcade.draw_triangle_filled(100,340, 200, 340, 200, 320, arcade.csscolor.CORNFLOWER_BLUE)

#luz reflejada cristal
arcade.draw_lrtb_rectangle_filled(98, 102, 429, 341, arcade.csscolor.KHAKI)


#finish
arcade.finish_render()

arcade.run()

