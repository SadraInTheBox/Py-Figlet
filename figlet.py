import pyfiglet
import pyfiglet as fg1
import sys
from random import choice

fg = pyfiglet.Figlet()

color = ""
colors = {
	"BLACK": 30,
	"RED": 31,
	"GREEN": 32,
	"YELLOW": 32,
	"BLUE": 34,
	"MAGNETA": 35,
	"PURPLE": 35,
	"CYAN": 36,
	"LIGHT_GRAY": 37,
	"LIGHT GRAY": 37,
	"DEFAULT": 39,
	"DARK_GRAY": 90,
	"LIGHT_RED": 91,
	"DARK GRAY": 90,
	"LIGHT RED": 91,
	"WHITE": 97,
	"RESET": 0
}
#color = "DEFAULT"
font = ""
fonts = fg.getFonts()
font = choice(fonts)
text = ""

if len(sys.argv) == 1:
	print("pls say\n\tfiglet [text] [font]")
	sys.exit()
if len(sys.argv) >= 2:
	if sys.argv[1].lower() == "-help":
		print("figlet [text] [font]")
		sys.exit()
	elif sys.argv[1].lower() == "-fonts":
		for i in fonts:
			print(i)
		print("[----Z3R0----]")
		sys.exit()
	else:
		text = sys.argv[1]
if len(sys.argv) >= 3:
	font = sys.argv[2]

if not font in fonts:
	print("choice a vallid font")
	sys.exit()

result = fg1.figlet_format(
	text=text,
	font=font,
	#colors=color
)

print(result)