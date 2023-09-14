import pygame
import sys

# กำหนดค่าหน้าจอ
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # ให้หน้าจอเต็มจอ
WIDTH, HEIGHT = screen.get_size()
BG_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)

# กำหนดเนื้อเรื่องเกม
story = [
    {
        'text': 'คุณเป็นคนไร้บ้าน ซึงวันนี้เป็นวันที่อากาศหนาวและมีหิมะตก คุณเดินไปเจอโรงแรมร้างแห่งหนึ่ง แต่คุณเคยได้ยินข่าวลือว่ามีเหตุฆาตกรรมในนั้น คุณจะเข้าไปหรือไม่?',
        'options': ['Yes', 'No'],
        'next_story': [1, 2]  # เมื่อตอบ Yes ไปเรื่องที่ 1, ตอบ No ไปเรื่องที่ 2
    },
    {
        #1 yes
        'text': 'คุณตัดสินใจเข้าโรงแรมแห่งนี้คุณเดินไปเรื่อย ๆ คุณรู้สึกว่ามีบางอย่างไม่ปกติในนี้แต่คุณง่วงนอนมากจึงหลับตาเพื่อนอนและเพียงไม่กี่นาทีหลังคุณหลับตาคุณได้ยินเสียงกรีดร้องมาจากห้องข้างๆ...คุณต้องการไปสำรวจหรือไม่?',
        'options': ['Yes', 'No'],
        'next_story': [3, 4]  
    },
    {
        #2 no
        
        'text': 'คุณเสียชีวิตเนื่องจากความหนาวเย็นของหิมะ''กด ESC เพื่อ ออกจากเกม',
        'options': [],
        'next_story': []  # เรื่องนี้จบ
        

    },
    {
        #3
                'text': 'คุณเข้าห้องข้างๆเพื่อตรวจสอบ คุณก้าวเข้าสู่ห้อง แต่ไม่พบสิ่งใดเลย เพียงแต่รู้สึกว่าอากาศเย็นลงมาอย่างเร็วเร็ว คุณเดินออกมาจากห้องและไปที่ห้องของคุณ เมื่อคุณอยู่ในห้องอีกครั้ง คุณได้ยินเสียงกรีดร้องจากด้านหลัง...คุณจะสนใจมันมั้ย?',
        'options': ['Yes', 'No' ],
        'next_story': [5, 4]  
    },
    {
        #4
        'text': 'คุณไม่สนใจและหลับต่อจนถึงเช้า คุณคิดได้ว่าเมื่อคืนมันมีบางอย่างแปลก ๆ คุณเลยเลือกที่จะเดินออกจากที่นี่ กด ESC เพื่อออกจากเกม',
        'options': [],
        'next_story': []  # เรื่องนี้จบ
     },
    {       #5
        'text': '"เชี่ย"',
        'options': ['Next'],
        'next_story': [6,]  
    },
    {        #6
        'text': '"เสียงเชี่ยไรวะ"',
        'options': ['Next'],
        'next_story': [7,]  # เรื่องนี้จบ
    },
    {        #7
        'text': 'คุณกำลังคิดว่าคุณต้องวิ่งหนี หรือจะอยู่ที่นี่',
        'options': ['หนี', 'อยู่ต่อ'],
        'next_story': [8, 9]  
    },
    {        #8 หนี
        'text': 'คุณได้เห็นประตูที่คุณเข้ามาแล้วคุณก็พุ่งออกไป',
        'options': ['Next'],
        'next_story': [10]  # เรื่องนี้จบ
    },
    {        #9 อยู่ต่อ
        'text': 'คุณได้หันหลังไป เจอกับร่างผู้หญิงที่มีเลือดเต็มตัว แล้วก็มีเสียงหายใจรดอยู่ข้าง ๆ หูของคุณ',
        'options': ['Next'],
        'next_story': [11]  # เรื่องนี้จบ
    },
    {        #10
        'text': 'คุณสะดุ้งตื่นขึ้นมาข้างกองถังขยะเพราะคุณได้ยินเสียงไซเรนของตำรวจ ตรงข้ามโรงแรมร้างนั้น END กด ESC เพื่อออกจากเกม',
        'options': [],
        'next_story': []  # เรื่องนี้จบ
    },
        {        #11
        'text': 'คุณเสียชีวิต กด ESC เพื่อออกจากเกม:) ',
        'options': [],
        'next_story': []  # เรื่องนี้จบ
    },
]

# กำหนดฟอนต์ที่รองรับภาษาไทย
THAI_FONT = r"dist\PK Uttaradit-Medium.ttf"


def draw_text(text, font, surface, x, y):
    text_obj = font.render(text, True, TEXT_COLOR)
    text_rect = text_obj.get_rect()
    text_rect.center = (WIDTH // 2, y)  # จัดตำแหน่งตรงกลางของหน้าจอ
    surface.blit(text_obj, text_rect)

def main():
    font = pygame.font.Font(THAI_FONT, 16)
    current_story_index = 0
    #ตั้งให้ออกเกม
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    #รับค่าแป้นพิมพ์
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    options_count = len(story[current_story_index]['options'])
                    if options_count > 0:
                        current_story_index = story[current_story_index]['next_story'][0]
                elif event.key == pygame.K_LEFT:
                    options_count = len(story[current_story_index]['options'])
                    if options_count > 0:
                        current_story_index = story[current_story_index]['next_story'][1]
                elif pygame.K_1 <= event.key <= pygame.K_9:  # ตรวจสอบว่ากดตัวเลข 1-9
                    numeric_option = event.key - pygame.K_1  # แปลงตัวเลขจาก 1-9 เป็น 0-8
                    options_count = len(story[current_story_index]['options'])
                    if numeric_option < options_count:
                        current_story_index = story[current_story_index]['next_story'][numeric_option]

                # เพิ่มเงื่อนไขเพื่อออกจากเกม
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    #BACKGROUND UI
        screen.fill(BG_COLOR)
        draw_text(story[current_story_index]['text'], font, screen, 50, HEIGHT // 2)

        # แสดงตัวเลือก Yes/No
        options = story[current_story_index]['options']
        if options:
            for i, option in enumerate(options):
                draw_text(f'{i+1}. {option}', font, screen, 50, HEIGHT // 2 + (i + 1) * 50)

        pygame.display.update()

if __name__ == '__main__':
    main()