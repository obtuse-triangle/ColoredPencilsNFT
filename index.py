import random

f = open("Frame1.svg", "r")
string = str(f.read())
color = []
check = {}
recolor = False

for i in range(10):

    while True:
        check_color = [
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ]
        if color == []:
            for ii in color:
                if color[ii][0] > check_color[0] - 12.75:
                    if (
                        check_color[0] + 12.75 < color[ii][0]
                        or check_color[0] == color[ii][0]
                    ):
                        check[i][ii]["R"] = True

                if color[ii][1] > check_color[1] - 12.75:
                    if (
                        check_color[1] + 12.75 < color[ii][1]
                        or check_color[1] == color[ii][1]
                    ):
                        check[i][ii]["G"] = True

                if color[ii][2] > check_color[2] - 12.75:
                    if (
                        check_color[2] + 12.75 < color[ii][2]
                        or check_color[2] == color[ii][2]
                    ):
                        check[i][ii]["B"] = True

                if check[i][ii]["R"] and check[i][ii]["G"] and check[i][ii]["B"]:
                    recolor = True
                    print("recolor")
                    break
                else:
                    recolor = False

        if recolor is False:
            color.append(check_color)
            break

    hexcolor1 = "#%02x%02x%02x" % tuple(color[i])

    color2 = []
    color3 = []

    for iii in range(len(color[i])):
        if color[i][iii] > 225:
            color2.append(255)
            continue
        else:
            color2.append(color[i][iii] + 30)

    for iii in range(len(color[i])):
        if (color[i][iii] + 80) > 225:
            if (color[i][iii] + 40) > 225:
                if (color[i][iii] + 20) > 225:
                    color3.append(255)
                    continue
                else:
                    color3.append(color[i][iii] + 20)
                    continue
            else:
                color3.append(color[i][iii] + 40)
                continue
        color3.append(color[i][iii] + 80)

    print(color[i], color2, color3, "\n")

    hexcolor2 = "#%02x%02x%02x" % tuple(color2)
    hexcolor3 = "#%02x%02x%02x" % tuple(color3)

    new_frame = string.replace("#PencilColor1", str(hexcolor1))
    new_frame = new_frame.replace("#PencilColor2", str(hexcolor1))
    new_frame = new_frame.replace("#PencilBodyColor", str(hexcolor2))
    new_frame = new_frame.replace("#BackgroundColor", str(hexcolor3))
    f = open(f"output{i}.svg", "w")
    f.write(new_frame)
    f.close()

f.close()
