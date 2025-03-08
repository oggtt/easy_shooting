# This software is licensed by the PSFL.

import tkinter as tk

def click(e):
    click_x = e.x
    click_y = e.y
    image_line = canvas.create_line(270, 400, click_x, click_y, fill="yellow", width=3, arrow=tk.BOTH)
    if (click_x>=260 and click_x<=280) and (click_y>=90 and click_y<=110):
        canvas.delete(image_item)
        # 1秒後に線を消す
        root.after(200, lambda: canvas.delete(image_line))
    else:
        # 1秒後に線を消す
        root.after(200, lambda: canvas.delete(image_line))

root = tk.Tk()
root.title("Shooting")
canvas = tk.Canvas(root, width=560, height=420)
canvas.pack()
#基本画像
gazou_back = tk.PhotoImage(file="back.png")
gazou_enemy = tk.PhotoImage(file="enemy.png")
gazou_ship = tk.PhotoImage(file="ship.png")
#canvasメソッド
bg_image_id = canvas.create_image(0, 0, image=gazou_back, anchor="nw")
canvas.tag_lower(bg_image_id)#最背面に画像を配置

image_item = canvas.create_image(270, 100, image=gazou_enemy)
canvas.create_image(270, 400, image=gazou_ship)

root.bind("<Button>", click)

root.mainloop()
