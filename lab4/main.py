from abc import ABC, abstractmethod
import pygame


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Rectangle(ABC):
    @abstractmethod
    def draw(self, surface: pygame.Surface):
        pass


class SimpleRectangle(Rectangle, Prototype):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.width, self.height))

    def clone(self) -> 'SimpleRectangle':
        return SimpleRectangle(self.x, self.y, self.width, self.height)


class RoundedRectangle(Rectangle, Prototype):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.width, self.height), border_radius=10)

    def clone(self) -> 'RoundedRectangle':
        return RoundedRectangle(self.x, self.y, self.width, self.height)


class Ellipse(ABC):
    @abstractmethod
    def draw(self, surface: pygame.Surface):
        pass


class SimpleEllipse(Ellipse, Prototype):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface: pygame.Surface):
        pygame.draw.ellipse(surface, (0, 0, 0), (self.x, self.y, self.width, self.height))

    def clone(self) -> 'SimpleEllipse':
        return SimpleEllipse(self.x, self.y, self.width, self.height)


class Line(ABC):
    @abstractmethod
    def draw(self, surface: pygame.Surface):
        pass


class SimpleLine(Line, Prototype):
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, surface: pygame.Surface):
        pygame.draw.line(surface, (0, 0, 0), (self.x1, self.y1), (self.x2, self.y2), 5)

    def clone(self) -> 'SimpleLine':
        return SimpleLine(self.x1, self.y1, self.x2, self.y2)


class Text(ABC):
    @abstractmethod
    def draw(self, surface: pygame.Surface):
        pass


class SimpleText(Text, Prototype):
    def __init__(self, text: str, center_x: int, center_y: int):
        self.text = text
        self.x = center_x
        self.y = center_y
        self.font = pygame.font.Font('Roboto-Regular.ttf', 14)

    def draw(self, surface: pygame.Surface):
        text_object = self.font.render(self.text, True, (255, 255, 255), (0, 0, 0))
        text_rect = text_object.get_rect()
        text_rect.center = (self.x, self.y)
        surface.blit(text_object, text_rect)

    def clone(self) -> 'SimpleText':
        return SimpleText(self.text, self.x, self.y)


class DiagramFactory:
    def __init__(self,
                 rectangle: Rectangle | Prototype,
                 ellipse: Ellipse | Prototype,
                 line: Line | Prototype,
                 text: Text | Prototype):
        super().__init__()
        self.rectangle_prototype = rectangle
        self.ellipse_prototype = ellipse
        self.line_prototype = line
        self.text_prototype = text

    def create_rectangle(self) -> Rectangle:
        return self.rectangle_prototype.clone()

    def create_ellipse(self) -> Ellipse:
        return self.ellipse_prototype.clone()

    def create_line(self) -> Line:
        return self.line_prototype.clone()

    def create_text(self) -> Text:
        return self.text_prototype.clone()


if __name__ == '__main__':
    pygame.init()

    _rectangle: Rectangle = RoundedRectangle(100, 50, 500, 200)
    _ellipse: Ellipse = SimpleEllipse(300, 500, 500, 200)
    _line: Line = SimpleLine(350, 250, 550, 500)
    _text: Text = SimpleText("Sample text", 350, 150)

    factory: DiagramFactory = DiagramFactory(_rectangle, _ellipse, _line, _text)

    rectangle: Rectangle = factory.create_rectangle()
    ellipse: Ellipse = factory.create_ellipse()
    line: Line = factory.create_line()
    text: Text = factory.create_text()

    objects = [rectangle, ellipse, line, text]

    window = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()

    is_working = True
    while is_working:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_working = False

        window.fill((255, 255, 255))
        for obj in objects:
            obj.draw(window)

        pygame.display.flip()
        clock.tick(60)
