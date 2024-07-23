import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def draw_snowflake(order, size):
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)
    
    turtle.done()

def main():
    try:
        order = int(input("Введіть рівень рекурсії (не менше 0): "))
        if order < 0:
            raise ValueError
    except ValueError:
        print("Будь ласка, введіть коректне число.")
        return

    size = 600  # Розмір фракталу
    draw_snowflake(order, size)

if __name__ == "__main__":
    main()
