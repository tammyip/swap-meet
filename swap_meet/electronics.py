from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category = "", condition = 0):
        # super().__init__(category = "Electronics")
        self.category = "Electronics"
        self.condition = condition

    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        return super().condition_description()