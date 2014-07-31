import turtle
import sys
import fileinput
import getopt
import csv

master_city = []

# CLASSES
# City Class
class City(object):
  def __init__(self, name, xcoord, ycoord, pop):
    self.name = name
    self.xcoord = xcoord
    self.ycoord = ycoord + 100
    self.pop = pop
    global master_city
    master_city.append(self)

  def getx(self):
    return self.xcoord

  def gety(self):
    return self.ycoord

  def getname(self):
    return self.name

  def getpop(self):
    return self.pop

# Road Class
class Road(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end

# VARIOUS FUNCTIONS
# Create New City Object
def create_city(line_item):
  print("N:", line_item[1], "X", line_item[2], "Y", line_item[3], "P", line_item[4])
  #print("Master:", master_city)
  new_city = City(line_item[1], float(line_item[2]), float(line_item[3]), float(line_item[4]))
  city_circle(new_city)
  city_name(new_city)

# Create New Road Object
def create_road(line_item):
  new_road = Road(line_item[1], line_item[2])
  draw_road(new_road)

# Print City Circle
def city_circle(city):
  turtle.penup()
  turtle.setx(city.xcoord)
  turtle.sety(city.ycoord)
  if city.getpop() > 0 and city.getpop() < 90001:
    turtle.setx(turtle.xcor() + 2)
    turtle.pendown()
    turtle.circle(2)
    turtle.penup()
    turtle.setx(turtle.xcor() - 2)
  if city.getpop() > 90000:
    turtle.setx(turtle.xcor() + 3)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    turtle.penup()
    turtle.setx(turtle.xcor() - 3)

# Print City Name
def city_name(city):
  if city.getname()[0] != "_":
    turtle.setx(turtle.xcor() + 10)
    turtle.sety(turtle.ycor() - 2)
    turtle.write(city.getname(), align="left")

# Draw a Road
def draw_road(road):
  startx = 0
  starty = 0
  endx = 0
  endy = 0
  for city in master_city:
    if road.start == city.getname():
      print("Start City:", city.getname())
      startx = city.getx()
      starty = city.gety()
    if road.end == city.getname():
      print("End City:", city.getname())
      endx = city.getx()
      endy = city.gety()
  turtle.goto(startx, starty)
  turtle.pendown()
  turtle.goto(endx, endy)
  turtle.penup()

# MAIN PROGRAM
# Main Function
def main(argv):
  user_file = ""

  # User GetOpt to Pull File from Command Line
  try:
    opts, args = getopt.getopt(argv,"hi:",["ifile="])
  except getopt.GetoptError:
    print("name-strip.py -i <input_file>")
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print("name-strip.py HELP\n\t-i <input_file>\t selects input file csv to interpret as map")
      sys.exit()
    elif opt in ("-i", "--ifile"):
      user_file = arg

  # Quit if no File Given
  if user_file == "":
    print("No file entered. Program terminating.")
    sys.exit()

  # Set Up CSV Reader
  mapReader = csv.reader(open(user_file, newline=''), delimiter=',', quotechar='|')

  # Iterate Through CSV
  for map_item in mapReader:
    #print("Map Item:", map_item)
    if map_item[0] == "c":
      create_city(map_item)
    else:
      create_road(map_item)

  turtle.hideturtle()
  turtle.done()

# Run Program from Command Line
if __name__ == "__main__":
   main(sys.argv[1:])
