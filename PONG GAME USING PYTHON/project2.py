import pygame

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, direction):
        self.rect.y += direction
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = 5
        self.speed_y = 5
        self.direction_x = 1
        self.direction_y = 1

    def move(self):
        self.rect.x += self.speed_x * self.direction_x
        self.rect.y += self.speed_y * self.direction_y

        # Bounce off the top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.direction_y *= -1

    def check_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.direction_x *= -1

    def check_score(self):
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            return True
        return False

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Main function
def main():
    clock = pygame.time.Clock()
    paddle_left = Paddle(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    paddle_right = Paddle(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle_left.move(-5)
        if keys[pygame.K_s]:
            paddle_left.move(5)
        if keys[pygame.K_UP]:
            paddle_right.move(-5)
        if keys[pygame.K_DOWN]:
            paddle_right.move(5)

        ball.move()

        ball.check_collision(paddle_left)
        ball.check_collision(paddle_right)

        if ball.check_score():
            ball = Ball()

        screen.fill(BLACK)
        paddle_left.draw()
        paddle_right.draw()
        ball.draw()
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
