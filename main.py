from GameControler import *
from Menu.MenuControler import *

pygame.init()
pygame.display.set_caption("数媒1902丁昊天 - 毕业设计：PVZ")
menuCtrler = MenuControler()
gameCtrler = None

def main():
    global gameCtrler
    while True:
        img_bg = pygame.image.load('Assets/其他图片/菜单背景.png')
        SCR.blit(img_bg, (0, 0))
        GameData['mouse_data'][0] = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QUIT()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                GameData['mouse_data'][1] = event.button

        record = GameData['MODE']
        if GameData['MODE'] == 'menu':
            menuCtrler.update()
        else:
            SCR.fill('white')
            gameCtrler.update()
        if record == 'menu' and GameData['MODE'] != 'menu':
            gameCtrler = GameControler()
            music_bg.start()
            if GameData['MODE'] == 'ZBs':
                GameData['money_zb'] = 1000
            else:
                GameData['money_pl'] = 500

        # 总刷新与收尾
        pygame.display.flip()
        GameData['mouse_data'][1] = 0
        CLK.tick(60)


if __name__ == '__main__':
    main()
