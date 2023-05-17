# from GameControler import *
from Menu.MenuControler import *
# c = Client()

pygame.init()
pygame.display.set_caption("数媒1902丁昊天 - 毕业设计：PVZ")
menuCtrler = MenuControler()

def main():
    while True:
        SCR.fill('white')
        GameData['mouse_data'][0] = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QUIT()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                GameData['mouse_data'][1] = event.button

        if GameData['MODE'] == 'menu':
            menuCtrler.update()
        elif GameData['MODE'] == 'PLs':
            # gameCtrler.update(c)
            pass

        # 总刷新与收尾
        pygame.display.flip()
        GameData['mouse_data'][1] = 0
        CLK.tick(60)


if __name__ == '__main__':
    main()
