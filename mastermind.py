from graphics import Canvas
import random
import time
import os

    
CANVAS_WIDTH = 480
CANVAS_HEIGHT = 720
CELL_WIDTH = 80
CELL_HEIGHT = 80
PEG_SIZE = 60
FEEDBACK_PEG_SIZE = 20
DELAY = 0.01


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # draw the board
    start_x = 0
    start_y = 0
    end_x = start_x + CANVAS_WIDTH
    end_y = start_y + 640
    board = canvas.create_rectangle(start_x, start_y, end_x, end_y, 'black')
    
    # draw peg choices
    draw_teal_peg = canvas.create_oval((CELL_WIDTH/2)-(PEG_SIZE/2), (CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2), ((CELL_WIDTH/2)-(PEG_SIZE/2) + PEG_SIZE), ((CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2) + PEG_SIZE), 'Teal')
    draw_magenta_peg = canvas.create_oval((CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2), (CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2), ((CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2) + PEG_SIZE), ((CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2) + PEG_SIZE), 'Magenta')
    draw_lime_peg = canvas.create_oval((2*CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2), (CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2), ((2*CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2) + PEG_SIZE), ((CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2) + PEG_SIZE), 'Lime')
    draw_blue_peg = canvas.create_oval((3*CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2), (CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2), ((3*CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2) + PEG_SIZE), ((CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2) + PEG_SIZE), 'Blue')
    draw_pink_peg = canvas.create_oval((4*CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2), (CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2), ((4*CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2) + PEG_SIZE), ((CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2) + PEG_SIZE), 'Pink')
    draw_orange_peg = canvas.create_oval((5*CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2), (CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2), ((5*CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2) + PEG_SIZE), ((CANVAS_HEIGHT-CELL_HEIGHT/2)-(PEG_SIZE/2) + PEG_SIZE), 'Orange')
    
    # draw guess numbers
    draw_guess_num_one = canvas.create_text((CELL_WIDTH/2)-(20), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*1)-(12))), font = "Arial", font_size = 30, text = "# 1", color = "White")
    draw_guess_num_two = canvas.create_text((CELL_WIDTH/2)-(20), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*2)-(12))), font = "Arial", font_size = 30, text = "# 2", color = "White")
    draw_guess_num_three = canvas.create_text((CELL_WIDTH/2)-(20), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*3)-(12))), font = "Arial", font_size = 30, text = "# 3", color = "White")
    draw_guess_num_four = canvas.create_text((CELL_WIDTH/2)-(20), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*4)-(12))), font = "Arial", font_size = 30, text = "# 4", color = "White")
    draw_guess_num_five = canvas.create_text((CELL_WIDTH/2)-(20), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*5)-(12))), font = "Arial", font_size = 30, text = "# 5", color = "White")
    draw_guess_num_six = canvas.create_text((CELL_WIDTH/2)-(20), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*6)-(12))), font = "Arial", font_size = 30, text = "# 6", color = "White")
    draw_guess_num_seven = canvas.create_text((CELL_WIDTH/2)-(20), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*7)-(12))), font = "Arial", font_size = 30, text = "# 7", color = "White")
    draw_guess_num_eight = canvas.create_text((CELL_WIDTH/2)-(20), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*8)-(12))), font = "Arial", font_size = 30, text = "# 8", color = "White")
    
    # pick random master pegs
    first_master_peg = random.randint(0, 5)
    second_master_peg = random.randint(0, 5)
    third_master_peg = random.randint(0, 5)
    forth_master_peg = random.randint(0, 5)
    
    master_colors = []
    
    master_pegs_0 = []
    master_pegs_1 = []
    master_pegs_2 = []
    master_pegs_3 = []
    master_pegs_4 = []
    master_pegs_5 = []
    
    if first_master_peg == 0:
        first_master_color = "Teal"
        master_pegs_0.append(1)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif first_master_peg == 1:
        first_master_color = "Magenta"
        master_pegs_0.append(0)
        master_pegs_1.append(1)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif first_master_peg == 2:
        first_master_color = "Lime"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(1)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif first_master_peg == 3:
        first_master_color = "Blue"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(1)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif first_master_peg == 4:
        first_master_color = "Pink"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(1)
        master_pegs_5.append(0)
    elif first_master_peg == 5:
        first_master_color = "Orange"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(1)
            
    if second_master_peg == 0:
        second_master_color = "Teal"
        master_pegs_0.append(1)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif second_master_peg == 1:
        second_master_color = "Magenta"
        master_pegs_0.append(0)
        master_pegs_1.append(1)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif second_master_peg == 2:
        second_master_color = "Lime"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(1)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif second_master_peg == 3:
        second_master_color = "Blue"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(1)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif second_master_peg == 4:
        second_master_color = "Pink"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(1)
        master_pegs_5.append(0)
    elif second_master_peg == 5:
        second_master_color = "Orange"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(1)
            
    if third_master_peg == 0:
        third_master_color = "Teal"
        master_pegs_0.append(1)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif third_master_peg == 1:
        third_master_color = "Magenta"
        master_pegs_0.append(0)
        master_pegs_1.append(1)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif third_master_peg == 2:
        third_master_color = "Lime"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(1)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif third_master_peg == 3:
        third_master_color = "Blue"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(1)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif third_master_peg == 4:
        third_master_color = "Pink"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(1)
        master_pegs_5.append(0)
    elif third_master_peg == 5:
        third_master_color = "Orange"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(1)
    
    if forth_master_peg == 0:
        forth_master_color = "Teal"
        master_pegs_0.append(1)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif forth_master_peg == 1:
        forth_master_color = "Magenta"
        master_pegs_0.append(0)
        master_pegs_1.append(1)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif forth_master_peg == 2:
        forth_master_color = "Lime"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(1)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif forth_master_peg == 3:
        forth_master_color = "Blue"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(1)
        master_pegs_4.append(0)
        master_pegs_5.append(0)
    elif forth_master_peg == 4:
        forth_master_color = "Pink"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(1)
        master_pegs_5.append(0)
    elif forth_master_peg == 5:
        forth_master_color = "Orange"
        master_pegs_0.append(0)
        master_pegs_1.append(0)
        master_pegs_2.append(0)
        master_pegs_3.append(0)
        master_pegs_4.append(0)
        master_pegs_5.append(1)
    
    master_colors.append(first_master_color)
    master_colors.append(second_master_color)
    master_colors.append(third_master_color)
    master_colors.append(forth_master_color)
    
    """
    print("Master pegs are: " + str(first_master_peg) , str(second_master_peg) , str(third_master_peg) , str(forth_master_peg))
    """
    # print("\x1b[2J\x1b[H", end="") # This was clearing the terminal but it is not working anymore on stanford ide
    """
    So we completely get rid of the terminal screen
    print("Welcome to Baris' Mastermind!")
    print("This is the classical code breaking game Mastermind. Computer picks 4 colors.")
    print("Find which colors picked!? Duplicate colors are allowed. Blanks are not.")
    print("Feedback appears on the right side of your guess.")
    print("Green = color picked and at the right place.")
    print("Yellow = color picked but not in the right place. Red = color doesn't picked.")
    print("Possible colors: Teal, Magenta, Lime, Blue, Pink, Orange")
    print("Are you ready! Let's get started!")
    """
    
    first_color_list = []
    second_color_list = []
    third_color_list = []
    forth_color_list = []
    first_feedback_color_list = []
    second_feedback_color_list = []
    third_feedback_color_list = []
    forth_feedback_color_list = []
    
    counter = 0
    
    while counter < 8:
        
        user_pegs_0 = []
        user_pegs_1 = []
        user_pegs_2 = []
        user_pegs_3 = []
        user_pegs_4 = []
        user_pegs_5 = []
        
        first_color = None
        # print("Pick your first color clicking on the sample colors above")
        while first_color not in {"T", "M", "L", "B", "P", "O", "t", "m", "l", "b", "p", "o"}:
            click = canvas.get_last_click()
            if click != None:
                click_x, click_y = click
                master_pegs = canvas.find_overlapping(click_x, click_y, click_x + 1, click_y + 1)
                if draw_teal_peg in master_pegs:
                    first_color = "T"
                elif draw_magenta_peg in master_pegs:
                    first_color = "M"
                elif draw_lime_peg in master_pegs:
                    first_color = "L"
                elif draw_blue_peg in master_pegs:
                    first_color = "B"
                elif draw_pink_peg in master_pegs:
                    first_color = "P"
                elif draw_orange_peg in master_pegs:
                    first_color = "O"
        
        if first_color == "T" or first_color == "t":
            first_peg = 0
            color = "Teal"
            user_pegs_0.append(1)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif first_color == "M" or first_color == "m":
            first_peg = 1
            color = "Magenta"
            user_pegs_0.append(0)
            user_pegs_1.append(1)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif first_color == "L" or first_color == "l":
            first_peg = 2
            color = "Lime"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(1)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif first_color == "B" or first_color == "b":
            first_peg = 3
            color = "Blue"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(1)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif first_color == "P" or first_color == "p":
            first_peg = 4
            color = "Pink"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(1)
            user_pegs_5.append(0)
        elif first_color == "O" or first_color == "o":
            first_peg = 5
            color = "Orange"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(1)
        
        first_color_list.append(color)
        draw_first_peg = draw_peg(canvas, ((CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2)), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*(counter+1))-(PEG_SIZE/2))), first_color_list[counter])
        
        second_color = None
        # print("Pick your second color clicking on the sample colors above")
        while second_color not in {"T", "M", "L", "B", "P", "O", "t", "m", "l", "b", "p", "o"}:
            click = canvas.get_last_click()
            if click != None:
                click_x, click_y = click
                master_pegs = canvas.find_overlapping(click_x, click_y, click_x + 1, click_y + 1)
                if draw_teal_peg in master_pegs:
                    second_color = "T"
                elif draw_magenta_peg in master_pegs:
                    second_color = "M"
                elif draw_lime_peg in master_pegs:
                    second_color = "L"
                elif draw_blue_peg in master_pegs:
                    second_color = "B"
                elif draw_pink_peg in master_pegs:
                    second_color = "P"
                elif draw_orange_peg in master_pegs:
                    second_color = "O"
            # second_color = input("Pick your second color (T)eal (M)agenta (L)ime (B)lue (P)ink (O)range: ")
        if second_color == "T" or second_color == "t":
            second_peg = 0
            color = "Teal"
            user_pegs_0.append(1)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif second_color == "M" or second_color == "m":
            second_peg = 1
            color = "Magenta"
            user_pegs_0.append(0)
            user_pegs_1.append(1)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif second_color == "L" or second_color == "l":
            second_peg = 2
            color = "Lime"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(1)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif second_color == "B" or second_color == "b":
            second_peg = 3
            color = "Blue"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(1)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif second_color == "P" or second_color == "p":
            second_peg = 4
            color = "Pink"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(1)
            user_pegs_5.append(0)
        elif second_color == "O" or second_color == "o":
            second_peg = 5
            color = "Orange"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(1)
        
        second_color_list.append(color)
        draw_second_peg = draw_peg(canvas, ((2*CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2)), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*(counter+1))-(PEG_SIZE/2))), second_color_list[counter])
        
        third_color = None
        # print("Pick your third color clicking on the sample colors above")
        while third_color not in {"T", "M", "L", "B", "P", "O", "t", "m", "l", "b", "p", "o"}:
            click = canvas.get_last_click()
            if click != None:
                click_x, click_y = click
                master_pegs = canvas.find_overlapping(click_x, click_y, click_x + 1, click_y + 1)
                if draw_teal_peg in master_pegs:
                    third_color = "T"
                elif draw_magenta_peg in master_pegs:
                    third_color = "M"
                elif draw_lime_peg in master_pegs:
                    third_color = "L"
                elif draw_blue_peg in master_pegs:
                    third_color = "B"
                elif draw_pink_peg in master_pegs:
                    third_color = "P"
                elif draw_orange_peg in master_pegs:
                    third_color = "O"
            # third_color = input("Pick your third color (T)eal (M)agenta (L)ime (B)lue (P)ink (O)range: ")
        if third_color == "T" or third_color == "t":
            third_peg = 0
            color = "Teal"
            user_pegs_0.append(1)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif third_color == "M" or third_color == "m":
            third_peg = 1
            color = "Magenta"
            user_pegs_0.append(0)
            user_pegs_1.append(1)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif third_color == "L" or third_color == "l":
            third_peg = 2
            color = "Lime"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(1)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif third_color == "B" or third_color == "b":
            third_peg = 3
            color = "Blue"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(1)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif third_color == "P" or third_color == "p":
            third_peg = 4
            color = "Pink"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(1)
            user_pegs_5.append(0)
        elif third_color == "O" or third_color == "o":
            third_peg = 5
            color = "Orange"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(1)
        
        third_color_list.append(color)
        draw_third_peg = draw_peg(canvas, ((3*CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2)), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*(counter+1))-(PEG_SIZE/2))), third_color_list[counter])
        
        forth_color = None
        # print("Pick your forth color clicking on the sample colors above")
        while forth_color not in {"T", "M", "L", "B", "P", "O", "t", "m", "l", "b", "p", "o"}:
            click = canvas.get_last_click()
            if click != None:
                click_x, click_y = click
                master_pegs = canvas.find_overlapping(click_x, click_y, click_x + 1, click_y + 1)
                if draw_teal_peg in master_pegs:
                    forth_color = "T"
                elif draw_magenta_peg in master_pegs:
                    forth_color = "M"
                elif draw_lime_peg in master_pegs:
                    forth_color = "L"
                elif draw_blue_peg in master_pegs:
                    forth_color = "B"
                elif draw_pink_peg in master_pegs:
                    forth_color = "P"
                elif draw_orange_peg in master_pegs:
                    forth_color = "O"
            # forth_color = input("Pick your forth color (T)eal (M)agenta (L)ime (B)lue (P)ink (O)range: ")
        if forth_color == "T" or forth_color == "t":
            forth_peg = 0
            color = "Teal"
            user_pegs_0.append(1)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif forth_color == "M" or forth_color == "m":
            forth_peg = 1
            color = "Magenta"
            user_pegs_0.append(0)
            user_pegs_1.append(1)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif forth_color == "L" or forth_color == "l":
            forth_peg = 2
            color = "Lime"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(1)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif forth_color == "B" or forth_color == "b":
            forth_peg = 3
            color = "Blue"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(1)
            user_pegs_4.append(0)
            user_pegs_5.append(0)
        elif forth_color == "P" or forth_color == "p":
            forth_peg = 4
            color = "Pink"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(1)
            user_pegs_5.append(0)
        elif forth_color == "O" or forth_color == "o":
            forth_peg = 5
            color = "Orange"
            user_pegs_0.append(0)
            user_pegs_1.append(0)
            user_pegs_2.append(0)
            user_pegs_3.append(0)
            user_pegs_4.append(0)
            user_pegs_5.append(1)
        
        forth_color_list.append(color)
        draw_forth_peg = draw_peg(canvas, ((4*CELL_WIDTH+CELL_WIDTH/2)-(PEG_SIZE/2)), (((CANVAS_HEIGHT-CELL_HEIGHT/2)-(CELL_HEIGHT*(counter+1))-(PEG_SIZE/2))), forth_color_list[counter])
        
        aa = first_peg == first_master_peg
        bb = second_peg == second_master_peg
        cc = third_peg == third_master_peg
        dd = forth_peg == forth_master_peg
        ab = first_peg == second_master_peg
        ac = first_peg == third_master_peg
        ad = first_peg == forth_master_peg
        ba = second_peg == first_master_peg
        bc = second_peg == third_master_peg
        bd = second_peg == forth_master_peg
        ca = third_peg == first_master_peg
        cb = third_peg == second_master_peg
        cd = third_peg == forth_master_peg
        da = forth_peg == first_master_peg
        db = forth_peg == second_master_peg
        dc = forth_peg == third_master_peg
        
        color_check_0 = []
        color_check_1 = []
        color_check_2 = []
        color_check_3 = []
        color_check_4 = []
        color_check_5 = []
        
        master_pegs_0_sorted = sorted(master_pegs_0)
        master_pegs_1_sorted = sorted(master_pegs_1)
        master_pegs_2_sorted = sorted(master_pegs_2)
        master_pegs_3_sorted = sorted(master_pegs_3)
        master_pegs_4_sorted = sorted(master_pegs_4)
        master_pegs_5_sorted = sorted(master_pegs_5)
        
        user_pegs_0_sorted = sorted(user_pegs_0)
        user_pegs_1_sorted = sorted(user_pegs_1)
        user_pegs_2_sorted = sorted(user_pegs_2)
        user_pegs_3_sorted = sorted(user_pegs_3)
        user_pegs_4_sorted = sorted(user_pegs_4)
        user_pegs_5_sorted = sorted(user_pegs_5)
        
        for i in range (len(master_pegs_0_sorted)):
            color_check = master_pegs_0_sorted[i] * user_pegs_0_sorted[i]
            color_check_0.append(color_check)
            
        for i in range (len(master_pegs_1_sorted)):
            color_check = master_pegs_1_sorted[i] * user_pegs_1_sorted[i]
            color_check_1.append(color_check)
            
        for i in range (len(master_pegs_2_sorted)):
            color_check = master_pegs_2_sorted[i] * user_pegs_2_sorted[i]
            color_check_2.append(color_check)
            
        for i in range (len(master_pegs_3_sorted)):
            color_check = master_pegs_3_sorted[i] * user_pegs_3_sorted[i]
            color_check_3.append(color_check)
            
        for i in range (len(master_pegs_4_sorted)):
            color_check = master_pegs_4_sorted[i] * user_pegs_4_sorted[i]
            color_check_4.append(color_check)
            
        for i in range (len(master_pegs_5_sorted)):
            color_check = master_pegs_5_sorted[i] * user_pegs_5_sorted[i]
            color_check_5.append(color_check)
            
        sum_color_check = (sum(color_check_0) + sum(color_check_1) + sum(color_check_2) + sum(color_check_3) + sum(color_check_4) + sum(color_check_5))
        
        feedback = []
        
        if sum_color_check == 0:
            for i in range(4):
                feedback.append(0)
        else:
            for i in range(sum_color_check):
                feedback.append(1)
            for i in range(4 - sum_color_check):
                feedback.append(0)
            
        list.sort(feedback, reverse = True)
        
        place_check_0 = []
        place_check_1 = []
        place_check_2 = []
        place_check_3 = []
        place_check_4 = []
        place_check_5 = []
        
        for i in range (len(master_pegs_0)):
            place_check = master_pegs_0[i] * user_pegs_0[i]
            place_check_0.append(place_check)
            
        for i in range (len(master_pegs_1)):
            place_check = master_pegs_1[i] * user_pegs_1[i]
            place_check_1.append(place_check)
            
        for i in range (len(master_pegs_2)):
            place_check = master_pegs_2[i] * user_pegs_2[i]
            place_check_2.append(place_check)
            
        for i in range (len(master_pegs_3)):
            place_check = master_pegs_3[i] * user_pegs_3[i]
            place_check_3.append(place_check)
            
        for i in range (len(master_pegs_4)):
            place_check = master_pegs_4[i] * user_pegs_4[i]
            place_check_4.append(place_check)
            
        for i in range (len(master_pegs_5)):
            place_check = master_pegs_5[i] * user_pegs_5[i]
            place_check_5.append(place_check)
            
        sum_place_check = (sum(place_check_0) + sum(place_check_1) + sum(place_check_2) + sum(place_check_3) + sum(place_check_4) + sum(place_check_5))
        
        for i in range(sum_place_check):
            feedback[i] += 1
        list.sort(feedback, reverse = True)
        
        """
        feedback.append(first_feedback)
        feedback.append(second_feedback)
        feedback.append(third_feedback)
        feedback.append(forth_feedback)
        list.sort(feedback, reverse = True)
        # print(*feedback)
        """
        
        feedback_colors = []
        
        for i in range (len(feedback)):
            if feedback[i] == 2:
                feedback_colors.append("Green")
            elif feedback[i] == 1:
                feedback_colors.append("Yellow")
            elif feedback[i] == 0:
                feedback_colors.append("Red")
            
        draw_first_feedback_peg = draw_feedback_peg(canvas, ((5*CELL_WIDTH+CELL_WIDTH/4)-(FEEDBACK_PEG_SIZE/2)), (((CANVAS_HEIGHT-CELL_HEIGHT*3/4)-(CELL_HEIGHT*(counter+1))-(FEEDBACK_PEG_SIZE/2))), feedback_colors[0])
        draw_second_feedback_peg = draw_feedback_peg(canvas, ((5*CELL_WIDTH+CELL_WIDTH*3/4)-(FEEDBACK_PEG_SIZE/2)), (((CANVAS_HEIGHT-CELL_HEIGHT*3/4)-(CELL_HEIGHT*(counter+1))-(FEEDBACK_PEG_SIZE/2))), feedback_colors[1])
        draw_third_feedback_peg = draw_feedback_peg(canvas, ((5*CELL_WIDTH+CELL_WIDTH/4)-(FEEDBACK_PEG_SIZE/2)), (((CANVAS_HEIGHT-CELL_HEIGHT/4)-(CELL_HEIGHT*(counter+1))-(FEEDBACK_PEG_SIZE/2))), feedback_colors[2])
        draw_forth_feedback_peg = draw_feedback_peg(canvas, ((5*CELL_WIDTH+CELL_WIDTH*3/4)-(FEEDBACK_PEG_SIZE/2)), (((CANVAS_HEIGHT-CELL_HEIGHT/4)-(CELL_HEIGHT*(counter+1))-(FEEDBACK_PEG_SIZE/2))), feedback_colors[3])
        
        if aa and bb and cc and dd:
            print("YOU WIN MASTERMIND!")
            print("You cracked the code on try #" + str(counter+1) + "!")
            break
        elif counter < 7:
            # print("\x1b[2J\x1b[H", end="")
            # print("Not quite right!")
            # print("Please try again using the feedback provided on the right side of your guess.")
            # print("Please try again. Guess number " + str(counter+2) + ":")
            # print(str(first_feedback), str(second_feedback), str(third_feedback), str(forth_feedback))
            pass
        else:
            print("GAME OVER")
            print("You used all 8 tries.")

        counter += 1
        
    print("The code was: ")
    print(*master_colors)
    print("To play again click the Run button above.")


def draw_peg(canvas, start_x, start_y, color):
    end_x = start_x + PEG_SIZE
    end_y = start_y + PEG_SIZE
    canvas.create_oval(start_x, start_y, end_x, end_y, color)


def draw_feedback_peg(canvas, start_x, start_y, color):
    end_x = start_x + FEEDBACK_PEG_SIZE
    end_y = start_y + FEEDBACK_PEG_SIZE
    canvas.create_oval(start_x, start_y, end_x, end_y, color)


def draw_guess_number(canvas, start_x, start_y, text, color):
    font = 'Arial'
    font_size = 50
    canvas.create_text(start_x, start_y, font, font_size, text, color)


if __name__ == '__main__':
    main()