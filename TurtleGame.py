import turtle
import random

# Global değişkenler
score = 0
timer = 30
running = True

# Ekran ayarları
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtles Game")
screen.setup(800, 600)

# Skor gösterimi
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-200, 200)
score_display.write(f"Skor: {score}", align="center", font=("Arial", 20, "normal"))

# Zaman gösterimi
timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(200, 200)
timer_display.write(f"Zaman: {timer}", align="center", font=("Arial", 20, "normal"))

# Turtle 1 - Kırmızı
moving_turtle = turtle.Turtle()
moving_turtle.shape("turtle")
moving_turtle.color("red")
moving_turtle.penup()

# Turtle 2 - Sarı
moving_turtle2 = turtle.Turtle()
moving_turtle2.shape("turtle")
moving_turtle2.color("yellow")
moving_turtle2.penup()

# Skor güncelleme
def update_score(x, y):
    global score, running
    if running:
        score += 1
        score_display.clear()
        score_display.write(f"Skor: {score}", align="center", font=("Arial", 20, "normal"))

# Turtle'ları hareket ettirme
def move_turtle():
    if running:
        x = random.randint(-350, 350)
        y = random.randint(-250, 250)
        moving_turtle.goto(x, y)
        screen.ontimer(move_turtle, 1000)

def move_turtle2():
    if running:
        x = random.randint(-350, 350)
        y = random.randint(-250, 250)
        moving_turtle2.goto(x, y)
        screen.ontimer(move_turtle2, 1000)

# Geri sayım fonksiyonu
def countdown():
    global timer, running
    if timer > 0:
        timer -= 1
        timer_display.clear()
        timer_display.write(f"Zaman: {timer}", align="center", font=("Arial", 20, "normal"))
        screen.ontimer(countdown, 1000)
    else:
        running = False
        timer_display.clear()
        timer_display.write("Oyun bitti", font=("Arial", 20, "normal"))

        # Oyun bittiğinde skor yazdır ve kaydet
        final_message = f"Oyun Bitti! Toplam Skor: {score}"

        # Ekrana yazdır
        message_display = turtle.Turtle()
        message_display.hideturtle()
        message_display.penup()
        message_display.goto(0, 0)
        message_display.write(final_message, align="center", font=("Arial", 20, "bold"))

        # Dosyaya yaz
        with open("skor_kaydi.txt", "a", encoding="utf-8") as file:
            file.write(f"{final_message}\n")


# Tıklamaları aktif et
moving_turtle.onclick(update_score)
moving_turtle2.onclick(update_score)

# Başlat
move_turtle()
move_turtle2()
countdown()

# Sonsuz döngü
screen.mainloop()

