# 1 can of paint = 5 sq m

from calendar import c


def coverage_calc(wall_height, wall_width, coverage_per_can):
    return (wall_height * wall_width) / coverage_per_can


cvg = 400

wh = float(input("$> Enter wall height (ft): "))
ww = float(input("$> Enter wall width (ft): "))

print("You will need %s can(s)." %
      '{:.2f}'.format(coverage_calc(wh, ww, cvg), '%2f'))
