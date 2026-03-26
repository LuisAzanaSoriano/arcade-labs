import arcade

# Configuración de la pantalla
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Moviendo un personaje"
MOVEMENT_SPEED = 5

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Variables para la posición y el movimiento del jugador
        self.player_x = 300
        self.player_y = 200
        self.player_change_x = 0
        self.player_change_y = 0

    def on_draw(self):
        """ Renderizar la pantalla """
        self.clear()
        # Dibujamos a nuestro jugador (un cuadrado amarillo)
        arcade.draw_ellipse_filled(self.player_x, self.player_y, 50, 50, arcade.color.YELLOW)

    def on_update(self, delta_time):
        """ Toda la lógica y movimiento va aquí """
        # Actualizamos la posición sumando la velocidad actual
        self.player_x += self.player_change_x
        self.player_y += self.player_change_y

        # Evitar que el jugador se salga de la pantalla
        if self.player_x < 25: self.player_x = 25
        if self.player_x > SCREEN_WIDTH - 25: self.player_x = SCREEN_WIDTH - 25
        if self.player_y < 25: self.player_y = 25
        if self.player_y > SCREEN_HEIGHT - 25: self.player_y = SCREEN_HEIGHT - 25

    def on_key_press(self, key, modifiers):
        """ Se llama cada vez que se presiona una tecla """
        if key == arcade.key.UP:
            self.player_change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Se llama cada vez que se suelta una tecla """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_change_x = 0

def main():
    game = MiJuego()
    arcade.run()

if __name__ == "__main__":
    main()