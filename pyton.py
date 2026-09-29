import math
import logging
import sys

# Шаблон строки лога (аналог template в Serilog)
# Содержит: время, уровень (до 7 символов для выравнивания), имя логгера и сообщение
log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Базовая настройка корневого логгера
logging.basicConfig(
    level=logging.DEBUG,  # Минимальный уровень логирования (аналог MinimumLevel.Debug)
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),          # Настройка логирования в консоль
        logging.FileHandler("logs/logi_txt.log", encoding="utf-8")  # Настройка логирования в файл
    ]
)

logging.warning("==============")
logging.info("Logger successfully configured")
logging.info("App is running...")

def parse_side(s):
    try:
        return float(s)
    except ValueError:
        return None

def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        logging.info("not triangle")
        return "не треугольник"
    if a == b == c:
        logging.info("equilateral")
        return "равносторонний"
    if a == b or b == c or a == c:
        logging.info("isosceles")
        return "равнобедренный"
    logging.info("not equilateral")
    return "разносторонний"

def coords(a, b, c):
    k = 100.0 / max(a, b, c)
    Ax, Ay = 0, 100
    Bx, By = int(a * k), 100
    x = (a*a + b*b - c*c) / (2*a)
    y = math.sqrt(max(b*b - x*x, 0))
    Cx = int(x * k)
    Cy = 100 - int(y * k)
    return [(Ax, Ay), (Bx, By), (Cx, Cy)]

s1 = input("enter dlina 1st side: ")
s2 = input("enter dlina 2nd side: ")
s3 = input("enter dlina 3rd side: ")

a = parse_side(s1)
b = parse_side(s2)
c = parse_side(s3)

if a is None or b is None or c is None:
    ttype = "не треугольник"
    verts = [(-2, -2), (-2, -2), (-2, -2)]
    logging.info("invalid values, all coords = (-2, -2) oo")
elif a <= 0 or b <= 0 or c <= 0:
    ttype = "не треугольник"
    verts = [(-1, -1), (-1, -1), (-1, -1)]
    logging.info("all coords = (-1, -1)")
else:
    ttype = triangle_type(a, b, c)
    if ttype == "не треугольник":
        verts = [(-1, -1), (-1, -1), (-1, -1)]
        logging.info("all coords = (-1, -1)")
    else:
        verts = coords(a, b, c)

print(ttype)
print(verts)