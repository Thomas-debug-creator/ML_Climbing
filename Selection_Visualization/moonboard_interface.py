from locale import currency
import cv2
import os
import sys
import pandas as pd
from enum import Enum

os.chdir(sys.path[0])

class SelectionType(Enum):
    HOLDS = 1
    MOVES = 2

#Setup the selection type (this should be an argument)

selection = SelectionType.MOVES

main_path = '../Data/'
video = 'moonboard'
directory = main_path + video + '/'

left_hand_color = (0, 204, 204)
right_hand_color = (0, 204, 0)
left_foot_color = (255, 102, 102)
right_foot_color = (76, 0, 153)
holds_color = (0,0,0)

limbs = ['left_hand', 'right_hand', 'left_foot', 'right_foot']
colors = [left_hand_color, right_hand_color, left_foot_color, right_foot_color]
y_coords = [30, 80, 130, 180]
color = left_hand_color

size = 30
thickness = 4

index = 0

move_id = 0

sequence = []



def increment_index():
    global index
    index += 1
    index %= 4

    global img
    img = img_without_circle.copy()

    cv2.circle(img, (10, y_coords[index]), 3, colors[index], thickness)
    cv2.imshow('image', img)

# function to display the coordinates
# of the points clicked on the image
def click_event(event, x, y, flags, params):

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        #Register the move in the sequence
        global sequence
        global index
        global move_id
        global color

        if selection == SelectionType.MOVES:
            sequence.append((x/frame_width,y/frame_height,limbs[index]))
            color = colors[index]
        
        elif selection == SelectionType.HOLDS:
            sequence.append((x/frame_width,y/frame_height))
            color = holds_color

        #Display it on the screen
        x_bg = x - size
        y_bg = y - size
        x_ed = x + size
        y_ed= y + size
 
        cv2.rectangle(img, (x_bg, y_bg), (x_ed, y_ed), color, thickness)
        cv2.putText(img, "{}".format(move_id), (x_bg, y_bg - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        cv2.rectangle(img_without_circle, (x_bg, y_bg), (x_ed, y_ed), color, thickness)
        cv2.putText(img_without_circle, "{}".format(move_id), (x_bg, y_bg - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        move_id += 1

        if selection == SelectionType.MOVES:
            increment_index()
        cv2.imshow('image', img)
 
# reading the image
# im = cv2.imread(main_path + '/' +video + '/' + video + '.jpg', 1)
im = cv2.imread(directory + video+ '_SCREEN.jpg', 1)
img = cv2.resize(im, (600, 980))   

frame_width = img.shape[1]
frame_height = img.shape[0]

if selection == SelectionType.MOVES:
    # Write the legend
    cv2.putText(img, "Left_hand", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, left_hand_color, 3)
    cv2.putText(img, "Right_hand", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.9, right_hand_color, 3)
    cv2.putText(img, "Left_foot", (20, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.9, left_foot_color, 3)
    cv2.putText(img, "Right_foot", (20, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.9, right_foot_color, 3)

img_without_circle = img.copy()

if selection == SelectionType.MOVES:
    cv2.circle(img, (10, y_coords[index]), 3, colors[index], thickness)
  
# displaying the image
cv2.imshow('image', img)

# setting mouse handler for the image
# and calling the click_event() function
cv2.setMouseCallback('image', click_event)

# Close the window if "x" is pressed
# If the window is closed, stop the program
while cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) > 0:
    k = cv2.waitKey(500)
    if k == 32:
        if selection == SelectionType.MOVES:
            increment_index()
        color = colors[index]
    elif k == 120:
        # close the window
        cv2.imwrite(main_path+ '/' + 'moonboard' + '/moonboard_holds_seqs.jpg', img)
        cv2.destroyAllWindows()
        break

if selection == SelectionType.MOVES:
    df_sequence = pd.DataFrame(sequence, columns=["x","y","limb"])
    df_sequence.to_csv(main_path+ '/' + 'moonboard' + '/' + 'moonboard_MOVE_SEQ.csv')

elif selection == SelectionType.HOLDS:
    df_sequence = pd.DataFrame(sequence, columns=["x","y"])
    df_sequence.to_csv(main_path+ '/' + 'moonboard' + '/' + 'moonboard_HOLDS_SEQ.csv')

print(df_sequence)