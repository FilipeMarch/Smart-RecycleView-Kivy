# Smart-RecycleView-Kivy
Control the way you scroll to an item on a RecycleView on Kivy

Sometimes you want to scroll to a specific item on your RecycleView, but how could you scroll your RecycleView to show some specific item on the top, center or bottom of the RV?



https://user-images.githubusercontent.com/23220309/214221627-d37fd2ac-e81e-43d5-bab4-dcc19b38da1c.mp4



I created this `SmartRV` which is a RecycleView that implements a function `scroll_to_item` that you can call from any widget and just pass the index of the item you want to scroll to. 

The usage is very simple, you just need to choose the orientation of the children ('horizontal' or 'vertical'), and set the height or width of the children.

For example, if you want a vertical `SmartRV`, you need to say what is the height of its children:
```yml
SmartRV:
    id: rv
    children_height: dp(50)
    orientation: 'vertical'
    RecycleBoxLayout:
        default_size: None, dp(50)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
```

And if you want a horizontal SmartRV, you need to say what is the width of its children:
```yml
SmartRV:
    id: rv
    children_width: dp(50)
    orientation: 'horizontal'
    RecycleBoxLayout:
        default_size: dp(50), None
        default_size_hint: None, 1
        size_hint_x: None
        width: self.minimum_width
        orientation: 'horizontal'
```

Now suppose you want to scroll to the item whose index is 15, how do you do it?

```yml
Button:
    on_release: rv.scroll_to_item(15)
```

That's it! I hope it helps.

If you want, you can change the SmartRV.vertical_behavior property to one of these:
```python
options=["scroll_to_top", "scroll_to_center", "scroll_to_bottom"]
```

Or you can change the SmartRV.horizontal_behavior property to one of these:
```python
options=["scroll_to_left", "scroll_to_center", "scroll_to_right"]
```

Also, you can define the duration of the animation by changing the property `scroll_duration`.
