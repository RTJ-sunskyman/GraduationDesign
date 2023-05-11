from GameControler import *
from Network.client import *
c = Client()

pygame.init()
pygame.display.set_caption("植物方")
GCtrler = GameControler('PLs')

def main():
    while True:
        SCR.fill('white')
        GameData['mouse_data'][0] = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                GameData['mouse_data'][1] = event.button

        GCtrler.update(c)

        # 总刷新与收尾
        pygame.display.flip()
        GameData['mouse_data'][1] = 0
        CLK.tick(60)


if __name__ == '__main__':
    main()
