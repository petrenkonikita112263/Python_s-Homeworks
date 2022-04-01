class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if (self.height > 50) or (self.width > 50):
            return "Too big for picture."
        else:
            row = "*" * self.width
            rows = [row for _ in range(self.height)]
            picture_result = "\n".join(rows)
            return picture_result + "\n"

    def get_amount_inside(self, shape):
        self.num_width = self.width // shape.width
        self.num_height = self.height // shape.height
        return self.num_width * self.num_height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_side(self, new_side_length):
        self.width = new_side_length
        self.height = new_side_length

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width

    def set_height(self, new_height):
        self.height = new_height
        self.width = new_height

    def __str__(self):
        return f"Square(side={self.width})"
