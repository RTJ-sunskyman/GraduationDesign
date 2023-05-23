from GameControler import *
from Menu.MenuControler import *

pygame.init()
pygame.display.set_caption("数媒1902丁昊天 - 毕业设计：PVZ")
menuCtrler = MenuControler()
gameCtrler = None

def main():
    global gameCtrler
    while True:
        SCR.fill('white')
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
            gameCtrler.update()
        if record == 'menu' and GameData['MODE'] != 'menu':
            gameCtrler = GameControler()
            if GameData['MODE'] == 'PLs':
                GameData['money_pl'] = 50
            if GameData['MODE'] == 'ZBs':
                GameData['money_zb'] = 1000

        # 总刷新与收尾
        pygame.display.flip()
        GameData['mouse_data'][1] = 0
        CLK.tick(60)


if __name__ == '__main__':
    main()
