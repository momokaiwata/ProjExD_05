import pygame as pg
import sys

def main():
    pg.display.set_caption("RPG of くそげー")
    screen = pg.display.set_mode((1400,700))
    bg_img = pg.image.load("./ex05/fig/back.png") #背景
    bg_img1 = pg.image.load("./ex05/fig/slime.png") #スライム
    bg_img2 = pg.transform.rotozoom(bg_img1, 0, 0.5)
    fontsize = 50
    font_path = "./ex05/fig/ipaexm.ttf" #日本語フォント
    font = pg.font.Font(font_path,fontsize)
    text = "スライムが現れた!!!"
    x = 450
    y = 100
    text_1 = font.render(text, True, (255,255,255))

    back = pg.image.load("./ex05/fig/R.png") #文字の枠
    back1 = pg.transform.rotozoom(back, 0, 1)
    x_back = 280
    y_back = 45

    frame = pg.image.load("./ex05/fig/frame.png")#攻撃選択用枠
    frame1 = pg.transform.rotozoom(frame, 0, 1)
    x_frame = 280
    y_frame = 400

    fontsize = 25
    text1 = "攻撃"
    text1_x = 350
    text1_y = 500
    text1_1 = font.render(text1, True, (255,255,255))

    

    # sentaku = pg.image.load("./ex05/fig/sentaku.png")#選択画面
    # sentaku1 = pg.transform.rotozoom(sentaku, 0, 1)
    # x_sentaku = 25
    # y_sentaku = 400

    


    while True: #イベントループ
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img,[0,0]) #背景をscreenの位置に描写
        screen.blit(bg_img2,[600,250]) #スライムを500,350の位置に描写
        screen.blit(back1, (x_back,y_back))
        screen.blit(text_1, (x, y))
        screen.blit(frame1, (x_frame, y_frame))
        screen.blit(text1_1, (text1_x,text1_y))

        # screen.blit(sentaku1,(x_sentaku, y_sentaku))
        pg.display.update() #ウィンドウを更新

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit() #pygameの終了
    sys.exit()