
import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window

class FlappyBirdGame(Widget):
    def __init__(self, **kwargs):
        super(FlappyBirdGame, self).__init__(**kwargs)

        self.pipe_vel_x = -4
        self.pipe_gap = 150
        self.pipe_spacing = 400
        self.pipe_pairs = []
        self.score = 0

        self.background = Image(source='gallery/sprites/background.png')
        self.player = Image(source='gallery/sprites/bird.png', pos=(50, 100))
        self.base = Image(source='gallery/sprites/base.png', pos=(0, 0))

        self.add_widget(self.background)
        self.add_widget(self.base)
        self.add_widget(self.player)

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        # Move pipes
        for pipe_pair in self.pipe_pairs:
            pipe_pair['upper'].pos[0] += self.pipe_vel_x
            pipe_pair['lower'].pos[0] += self.pipe_vel_x

            if pipe_pair['upper'].pos[0] < -pipe_pair['upper'].size[0]:
                self.remove_widget(pipe_pair['upper'])
                self.remove_widget(pipe_pair['lower'])
                self.pipe_pairs.remove(pipe_pair)

        # Add new pipe pair
        if len(self.pipe_pairs) == 0 or self.pipe_pairs[-1]['upper'].pos[0] < Window.width - self.pipe_spacing:
            gap_y = random.randint(50, Window.height - self.pipe_gap - 50)
            upper_pipe = Image(source='gallery/sprites/pipe.png', pos=(Window.width, gap_y + self.pipe_gap))
            lower_pipe = Image(source='gallery/sprites/pipe.png', pos=(Window.width, gap_y - 500), allow_stretch=True, keep_ratio=False)
            self.pipe_pairs.append({'upper': upper_pipe, 'lower': lower_pipe})
            self.add_widget(upper_pipe)
            self.add_widget(lower_pipe)

        # Update score
        player_x = self.player.pos[0]
        for pipe_pair in self.pipe_pairs:
            if pipe_pair['upper'].pos[0] < player_x < pipe_pair['upper'].pos[0] + pipe_pair['upper'].size[0]:
                self.score += 1
                print(f"Score: {self.score}")

    def on_touch_down(self, touch):
        self.player.pos[1] += 50

class FlappyBirdApp(App):
    def build(self):
        game = FlappyBirdGame()
        return game

if __name__ == "__main__":
    FlappyBirdApp().run()
