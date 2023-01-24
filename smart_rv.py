from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory as F
from kivy.animation import Animation


class SmartRV(F.RecycleView):
    """
    This RecycleView implements a smart scroll behavior.
    You can select the item you want to scroll to by using the
    function to scroll to an item called `scroll_to_item`. You will
    be able to scroll to the item by using the item's index, and you can
    select among three different scroll behaviors: `scroll_to_top`,
    `scroll_to_center` and `scroll_to_bottom`.
    """

    orientation = F.OptionProperty("vertical", options=["vertical", "horizontal"])

    children_height = F.NumericProperty()
    children_width = F.NumericProperty()

    vertical_behavior = F.OptionProperty(
        "scroll_to_top",
        options=["scroll_to_top", "scroll_to_center", "scroll_to_bottom"],
    )
    horizontal_behavior = F.OptionProperty(
        "scroll_to_left",€
        options=["scroll_to_left", "scroll_to_center", "scroll_to_right"],
    )
    scroll_duration = F.NumericProperty(1)

    def scroll_to_item(self, index):
        """
        Scroll to the item at the given index.
        :param index: The index of the item to scroll to.
        """
        if not self.data:
            return

        if self.orientation == "vertical":
            N = len(self.data)  # number of items

            h = self.children_height  # height of each item
            H = self.height  # height of the RecycleView

            if self.vertical_behavior == "scroll_to_top":
                scroll_y = 1 - (index * h) / (N * h - H)
            elif self.vertical_behavior == "scroll_to_center":
                scroll_y = 1 - (index * h - H / 2 + h / 2) / (N * h - H)
            elif self.vertical_behavior == "scroll_to_bottom":
                scroll_y = 1 - (index * h - H + h) / (N * h - H)

            Animation(scroll_y=scroll_y, d=self.scroll_duration).start(self)

        elif self.orientation == "horizontal":
            N = len(self.data)  # number of items

            w = self.children_width  # width of each item
            W = self.width  # width of the RecycleView

            if self.horizontal_behavior == "scroll_to_left":
                scroll_x = (index * w) / (N * w - W)

            elif self.horizontal_behavior == "scroll_to_center":
                scroll_x = (index * w - W / 2 + 1 / 2 * w) / (N * w - W)

            elif self.horizontal_behavior == "scroll_to_right":
                scroll_x = (index * w - W + w) / (N * w - W)

            Animation(scroll_x=scroll_x, d=self.scroll_duration).start(self)


# fmt: off
kv = Builder.load_string("""
#:import random random
#:import Animation kivy.animation.Animation

BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        Button:
            text: "Click to \\nscroll"
            font_size: sp(42)
            halign: 'center'
            color: 0,1,0,1
            on_release:
                rv.data = [{'text': str(x)} for x in range(100)]
                random_number = random.randint(0, 100)
                self.text = str(random_number)
                rv.scroll_to_item(random_number)
                for value in rv.data: value['color'] = [1, 1, 1, 1]
                if random_number > 0: rv.data[random_number]['color'] = [0, 1, 0, 1]
                else: rv.data[0]['color'] = [0, 1, 0, 1]
        ToggleButton:
            text: "TOP"
            group: "vertical_behavior"
            state: "down"
            on_state:
                if self.state == "down": rv.vertical_behavior = "scroll_to_top"
        ToggleButton:
            text: "CENTER"
            group: "vertical_behavior"
            on_state:
                if self.state == "down": rv.vertical_behavior = "scroll_to_center"
        ToggleButton:
            text: "BOTTOM"
            group: "vertical_behavior"
            on_state:
                if self.state == "down": rv.vertical_behavior = "scroll_to_bottom"

    SmartRV:
        id: rv
        viewclass: 'Button'
        data: [{'text': str(x)} for x in range(100)]
        size_hint_y: None
        height: dp(250)
        children_height: dp(50)
        RecycleBoxLayout:
            default_size: None, dp(50)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'

    BoxLayout:
        Button:
            text: "Click to \\nscroll"
            font_size: sp(42)
            halign: 'center'
            color: 1,0,0,1
            on_release:
                rv2.data = [{'text': str(x)} for x in range(100)]
                random_number = random.randint(0, 100)
                self.text = str(random_number)
                rv2.scroll_to_item(random_number)
                for value in rv2.data: value['color'] = [1, 1, 1, 1]
                if random_number > 0: rv2.data[random_number]['color'] = [1, 0, 0, 1]
                else: rv2.data[0]['color'] = [1, 0, 0, 1]
        ToggleButton:
            text: "LEFT"
            group: "horizontal_behavior"
            state: "down"
            on_state:
                if self.state == "down": rv2.horizontal_behavior = "scroll_to_left"
        ToggleButton:
            text: "CENTER"
            group: "horizontal_behavior"
            on_state:
                if self.state == "down": rv2.horizontal_behavior = "scroll_to_center"
        ToggleButton:
            text: "RIGHT"
            group: "horizontal_behavior"
            on_state:
                if self.state == "down": rv2.horizontal_behavior = "scroll_to_right"

    SmartRV:
        id: rv2
        viewclass: 'Button'
        data: [{'text': str(x)} for x in range(100)]
        size_hint_x: None
        width: dp(700)
        children_width: dp(50)
        orientation: 'horizontal'
        pos_hint: {'center_x': 0.5}
        RecycleBoxLayout:
            default_size: dp(50), None
            default_size_hint: None, 1
            size_hint_x: None
            width: self.minimum_width
            orientation: 'horizontal'

"""
)
# fmt: on


class TestApp(App):
    def build(self):
        return kv


TestApp().run()
