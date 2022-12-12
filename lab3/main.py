from abc import ABC, abstractmethod
import pygame


class Rectangle(ABC):
    @abstractmethod
    def draw(self, surface: pygame.Surface):
        pass


class SimpleRectangle(Rectangle):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.width, self.height))


class RoundedRectangle(Rectangle):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.width, self.height), border_radius=10)


class Ellipse(ABC):
    @abstractmethod
    def draw(self, surface: pygame.Surface):
        pass


class SimpleEllipse(Ellipse):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface: pygame.Surface):
        pygame.draw.ellipse(surface, (0, 0, 0), (self.x, self.y, self.width, self.height))


class Line(ABC):
    @abstractmethod
    def draw(self, surface: pygame.Surface):
        pass


class SimpleLine(Line):
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, surface: pygame.Surface):
        pygame.draw.line(surface, (0, 0, 0), (self.x1, self.y1), (self.x2, self.y2), 5)


class Text(ABC):
    @abstractmethod
    def draw(self, surface: pygame.Surface):
        pass


class SimpleText(Text):
    def __init__(self, text: str, center_x: int, center_y: int):
        self.text = text
        self.x = center_x
        self.y = center_y
        self.font = pygame.font.Font('Roboto-Regular.ttf', 24)

    def draw(self, surface: pygame.Surface):
        text_object = self.font.render(self.text, True, (255, 255, 255), (0, 0, 0))
        text_rect = text_object.get_rect()
        text_rect.center = (self.x, self.y)
        surface.blit(text_object, text_rect)


class AbstractDiagramFactory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create_rectangle(self, x: int, y: int, width: int, height: int) -> Rectangle:
        pass

    @abstractmethod
    def create_ellipse(self, x: int, y: int, width: int, height: int) -> Ellipse:
        pass

    @abstractmethod
    def create_line(self, x1: int, y1: int, x2: int, y2: int) -> Line:
        pass

    @abstractmethod
    def create_text(self, text: str, center_x: int, center_y: int) -> Text:
        pass


class SimpleDiagramFactory(AbstractDiagramFactory):
    def __init__(self):
        super().__init__()

    def create_rectangle(self, x: int, y: int, width: int, height: int) -> Rectangle:
        return SimpleRectangle(x, y, width, height)

    def create_ellipse(self, x: int, y: int, width: int, height: int) -> Ellipse:
        return SimpleEllipse(x, y, width, height)

    def create_line(self, x1: int, y1: int, x2: int, y2: int) -> Line:
        return SimpleLine(x1, y1, x2, y2)

    def create_text(self, text: str, center_x: int, center_y: int) -> Text:
        return SimpleText(text, center_x, center_y)
    
    
class RoundedDiagramFactory(AbstractDiagramFactory):
    def __init__(self):
        super().__init__()

    def create_rectangle(self, x: int, y: int, width: int, height: int) -> Rectangle:
        return RoundedRectangle(x, y, width, height)

    def create_ellipse(self, x: int, y: int, width: int, height: int) -> Ellipse:
        return SimpleEllipse(x, y, width, height)

    def create_line(self, x1: int, y1: int, x2: int, y2: int) -> Line:
        return SimpleLine(x1, y1, x2, y2)

    def create_text(self, text: str, center_x: int, center_y: int) -> Text:
        return SimpleText(text, center_x, center_y)


if __name__ == '__main__':
    pygame.init()

    factory: AbstractDiagramFactory = RoundedDiagramFactory()

    rectangle: Rectangle = factory.create_rectangle(100, 50, 500, 200)
    ellipse: Ellipse = factory.create_ellipse(300, 500, 500, 200)
    line: Line = factory.create_line(350, 250, 550, 500)
    text: Text = factory.create_text("Sample text", 350, 150)

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
