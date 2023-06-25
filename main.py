# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1: Greet Template
def greet(name, greeting_template='Hello, <name>!'):
    return greeting_template.replace('<name>', name)

# Part 2: Force
gravity_factors = {
    'earth': 9.8,
    'mercury': 3.7,
    'venus': 8.9,
    'mars': 3.7,
    'jupiter': 23.1,
    'saturn': 9.0,
    'uranus': 8.7,
    'neptune': 11.0,
    'pluto': 0.7,
    'moon': 1.6
}

def force(mass, body='earth'):
    gravity = gravity_factors.get(body.lower(), 9.8)
    return mass * gravity

# Part 3: Gravity
G = 6.674e-11

def pull(m1, m2, d):
    return G * ((m1 * m2) / (d ** 2))

# example_cars
m1 = 800
m2 = 1500
d = 3
print(round(pull(m1, m2, d), 10))

