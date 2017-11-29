#!/usr/bin/evn python

#too much image load...

import pygame
import sys
import time
import math
import random
import datetime
from numpy import array
from PIL import Image
from sys import exit
from pygame.locals import *

#system setting

pygame.init()
game_window = [1000, 600]
background_color = [34, 177, 76]
screen = pygame.display.set_mode((game_window[0], game_window[1]), 0, 32)
pygame.display.set_caption("-Simple Blackjack-")
#sys.path.append("C:\Users\kaz\Desktop\pywork\Blackjack\card")
#import sys_card

#setting image's file name

loading_image_filename = "./img/loading.png"
debug_image_filename = './img/card/half_png/x01.png'
background_image_filename = "./img/green.png"
start_image_filename = "./img/start2.png"
editor_image_filename = "./img/editor2.png"
startButton_image_filename = "./img/startButton.png"
redBackCard_image_filename = "./img/card/half_png/z02.png"
draw_image_filename = "./img/Draw.png"
youwin_image_filename = "./img/YouWin.png"
youlose_image_filename = "./img/YouLose.png"
blackjack_image_filename = "./img/BlackJack.png"
bust_image_filename = "./img/Bust.png"
hitorstand_image_filename = "./img/HitorStand.png"
deckShuffled_image_filename = "./img/DeckShuffled.png"
hit_image_filename = "./img/hit.png"
stand_image_filename = "./img/stand.png"
continue_image_filename = "./img/continue.png"
thankyou_image_filename = "./img/ThankYou.png"
dealerTurn_image_filename = "./img/DealerTurn.png"
#loading images

loading_image = pygame.image.load(loading_image_filename).convert()
debug_image = pygame.image.load(debug_image_filename).convert_alpha()
background_image = pygame.image.load(background_image_filename).convert()
start_image = pygame.image.load(start_image_filename).convert_alpha()
editor_image = pygame.image.load(editor_image_filename).convert_alpha()
startButton_image = pygame.image.load(startButton_image_filename).convert_alpha()
redBackCard_image = pygame.image.load(redBackCard_image_filename).convert_alpha()
draw_image = pygame.image.load(draw_image_filename).convert_alpha()
youwin_image = pygame.image.load(youwin_image_filename).convert_alpha()
youlose_image = pygame.image.load(youlose_image_filename).convert_alpha()
blackjack_image = pygame.image.load(blackjack_image_filename).convert_alpha()
bust_image = pygame.image.load(bust_image_filename).convert_alpha()
hitorstand_image = pygame.image.load(hitorstand_image_filename).convert_alpha()
deckShuffled_image = pygame.image.load(deckShuffled_image_filename).convert_alpha()
hit_image = pygame.image.load(hit_image_filename).convert_alpha()
stand_image = pygame.image.load(stand_image_filename).convert_alpha()
continue_image = pygame.image.load(continue_image_filename).convert_alpha()
thankyou_image = pygame.image.load(thankyou_image_filename).convert_alpha()
dealerTurn_image = pygame.image.load(dealerTurn_image_filename).convert_alpha()
#screen update

screen.blit(loading_image, (0, 0))
pygame.display.update()

#-----------------------------Game Setting Start---------------------------------------#

Card1 = ['C,01','C,02','C,03','C,04','C,05','C,06','C,07','C,08','C,09','C,10','C,11','C,12','C,13']
Card2 = ['D,01','D,02','D,03','D,04','D,05','D,06','D,07','D,08','D,09','D,10','D,11','D,12','D,13']
Card3 = ['H,01','H,02','H,03','H,04','H,05','H,06','H,07','H,08','H,09','H,10','H,11','H,12','H,13']
Card4 = ['S,01','S,02','S,03','S,04','S,05','S,06','S,07','S,08','S,09','S,10','S,11','S,12','S,13']

lined_deck = Card1 + Card2 + Card3 + Card4
deck = 4 * (Card1 + Card2 + Card3 + Card4)
each_deck_num = 13
count = 0
first_check = 0
for val in deck:
	count += 1
deck_num = range(0, count)
random.shuffle(deck_num)

#debug deck
#Card1 = ["S,10","S,01","S,10","S,01"]
#Card2 = ["S,10","S,01","S,10","S,01"]
#Card3 = ["S,05","S,05","S,10","S,01"]
#Card4 = ["S,05","S,05","S,10","S,01"]
#each_deck_num = 2
#lined_deck = Card1 + Card2 + Card3 + Card4
#deck = (Card1 + Card2 + Card3 + Card4)
#count = 0
#first_check = 0
#for val in deck:
#	count += 1
#deck_num = range(0, count)
#debug deck done

now = 0
blackjack = [0, 0]

#-------------------------------------Load card deck--------------------------------
#Card1_image = range(len(Card1))
#Card2_image = range(len(Card2))
#Card3_image = range(len(Card3))
#Card4_image = range(len(Card4))

#for val in range(13):
#	Card1_image[val] = pygame.image.load(card2img(Card1[val])).convert_alpha()
#	Card2_image[val] = pygame.image.load(card2img(Card2[val])).convert_alpha()
#	Card3_image[val] = pygame.image.load(card2img(Card3[val])).convert_alpha()
#	Card4_image[val] = pygame.image.load(card2img(Card4[val])).convert_alpha()

Card1_image = []
Card2_image = []
Card3_image = []
Card4_image = []

def card2img(card):
	card_id = card.split(",")
	card_img = "./img/card/half_png/" + card_id[0].lower() + card_id[1] + ".png"
	return card_img

for val in range(each_deck_num):
	Card1_image.append(pygame.image.load(card2img(Card1[val])).convert_alpha())
	Card2_image.append(pygame.image.load(card2img(Card2[val])).convert_alpha())
	Card3_image.append(pygame.image.load(card2img(Card3[val])).convert_alpha())
	Card4_image.append(pygame.image.load(card2img(Card4[val])).convert_alpha())

#-------------------------------------Load End--------------------------------#

def Kev_sleep_second(time):	#only allowed integer
	finishFlag = 0
	time_passed = 0
	clock = datetime.datetime.today()
	clock_change = clock

	event = pygame.event.poll()	#Get event
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	while finishFlag== 0:
		clock = datetime.datetime.today()
		if clock.second != clock_change.second :
		        time_passed += 1
        	        clock_change = clock
		if time_passed == time:
			finishFlag = 1

def Kev_sleep_millisecond(time):	#maximum is 999
	time *= 1000
	time_passed = 0
	finishFlag = 0
	clock = datetime.datetime.today()
	clock_change = clock

	event = pygame.event.poll()	#Get event
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	if clock_change.microsecond + time > 1000000:
        	clock_change = clock_change.microsecond + time - 1000000
	else:
	        clock_change = clock_change.microsecond + time

	while finishFlag== 0:
		clock = datetime.datetime.today()

		if clock.microsecond == clock_change:
			finishFlag = 1

def Kev_sleep_millisecond2(time):
	second = 1
	while time > 1000:
		second += 1
		time -= 1000

	time *= 1000
	time_passed = 0
	finishFlag = 0
	clock = datetime.datetime.today()
	clock_change = clock

	event = pygame.event.poll()	#Get event
	for event in pygame.event.get():
		if event.type == QUIT:
				exit()

	if clock_change.microsecond + time > 1000000:
        	clock_change = clock_change.microsecond + time - 1000000
	else:
	        clock_change = clock_change.microsecond + time

	while finishFlag < second:
		clock = datetime.datetime.today()
		event = pygame.event.poll()	#Get event
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				exit()
			if event.key == K_SPACE:
				return 0
		else:
			if clock.microsecond == clock_change - 1000:
				finishFlag += 1
				while clock.microsecond == clock_change - 1000:
					clock = datetime.datetime.today()

def centerPos(image_filename):
	image = pygame.image.load(image_filename).convert_alpha()
	pos = [(game_window[0] - image.get_width()) / 2, (game_window[1] - image.get_height()) / 2]
	return pos

def transparent2(fade_image_filename, back_image_filename, color, x_pos, y_pos):	#color has to be list of 3

	event = pygame.event.poll()	#Get event
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	fade_image = pygame.image.load(fade_image_filename).convert_alpha()
	if back_image_filename != "NONE":
		back_image = pygame.image.load(back_image_filename).convert_alpha()

	for val in range(10):  #transparent
		Kev_sleep_millisecond2(100)
		screen.fill((color[0], color[1], color[2]))
		#pygame.time.wait(100)
		transparent_activate(fade_image, 1.5, 1)
		if back_image_filename != "NONE":
			screen.blit(back_image, (x_pos, y_pos))
		screen.blit(fade_image, (x_pos, y_pos))
		pygame.display.update()

#color has to be list of 3, fade_image_filename has to be list type
def transparent3(fade_image_filename, back_image_filename, color, change_num, fade_speed):
	global card_pos_info
	fade_image = []

	if fade_speed == "Default":
		fade_speed = 100
	for val in range(len(fade_image_filename)):
		fade_image.append(pygame.image.load(fade_image_filename[val][0]).convert_alpha())
	if back_image_filename != "NONE":
		back_image = pygame.image.load(back_image_filename).convert_alpha()

	for val in range(10):  #transparent
		Kev_sleep_millisecond2(fade_speed)
		screen.fill((color[0], color[1], color[2]))
		transparent_activate(fade_image[change_num], 1.5, 1)

		if back_image_filename != "NONE":
			screen.blit(back_image, (fade_image_filename[change_num][1], fade_image_filename[change_num][2]))

		for i in range(len(fade_image_filename)):
			screen.blit(fade_image[i], (fade_image_filename[i][1], fade_image_filename[i][2]))

		pygame.display.update()
	card_pos_info[change_num][0] = back_image_filename
	reset()

def transparent_activate(surface, fade_speed, fadeInOut):
	uialpha = pygame.surfarray.pixels_alpha(surface)
	if fadeInOut == 1:
		uialpha /= fade_speed
	else:
		uialpha *= 1.2
	del uialpha

def setAllCardPos():
	global card_pos_info
	global player_pos_info
	global dealer_pos_info

	card_pos_info = []
	default_pos = [redBackCard_image_filename, center_card[0], center_card[1]]
	card_pos_info.append(default_pos)

	for val in player_pos_info:
		card_pos_info.append(val)
	for val in dealer_pos_info:
		card_pos_info.append(val)

def allShow(color):	#all images has to be list type
	global card_pos_info
	image_name = []

	for val in range(len(card_pos_info)):
		image_name.append(pygame.image.load(card_pos_info[val][0]).convert_alpha())

	screen.fill((color[0], color[1], color[2]))
	for i in range(len(card_pos_info)):
		screen.blit(image_name[i], (card_pos_info[i][1], card_pos_info[i][2]))

def get_one_card(who):	#player = 0, dealer = 1
	global card_pos_info
	global now
	global player_hold
	global dealer_hold
	global player_pos_info
	global dealer_pos_info
	check = 0
	speed = 4

	if who == 0:
		player_card_info = [redBackCard_image_filename, center_card[0], center_card[1]]
		player_hold.append(deck[deck_num[now]])
		card_num = len(player_hold)
		player_pos_info.append(player_card_info)

		while player_pos_info[card_num - 1][1] < (game_window[0] - redBackCard_image.get_width()) / 2 + (card_num - 1) * (redBackCard_image.get_width() / 2 + 5):
			player_pos_info[card_num - 1][1] += speed
			setAllCardPos()
			allShow(background_color)
			#pygame.time.wait(1)
			pygame.display.update()
			if (game_window[0] - redBackCard_image.get_width()) / 2 + (card_num - 1) * (redBackCard_image.get_width() / 2 + 5) - player_pos_info[card_num - 1][1] < speed:
				player_pos_info[card_num - 1][1] = (game_window[0] - redBackCard_image.get_width()) / 2 + (card_num - 1) * (redBackCard_image.get_width() / 2 + 5)
				setAllCardPos()
				allShow(background_color)
				pygame.display.update()


		while player_pos_info[card_num - 1][2] < game_window[1] - redBackCard_image.get_height():
			player_pos_info[card_num - 1][2] += speed
			if check != (redBackCard_image.get_width() / 2 + 5):
				for val in range(len(player_pos_info) - 1):
					player_pos_info[val][1] -= 1
				check += 1

			#pygame.time.wait(1)
			allShow(background_color)
			setAllCardPos()
			pygame.display.update()

			if game_window[1] - redBackCard_image.get_height() - player_pos_info[card_num - 1][2] < speed:
				player_pos_info[card_num - 1][2] = game_window[1] - redBackCard_image.get_height()
				setAllCardPos()
				allShow(background_color)
				pygame.display.update()


#		player_card_info.append((game_window[0] - redBackCard_image.get_width()) / 2 + (card_num - 1) * (redBackCard_image.get_width() / 2 + 5))
#		player_card_info.append(game_window[1] - redBackCard_image.get_height())

#		for val in range(len(player_pos_info)):5)
#			player_pos_info[val][1] -= (redBackCard_image.get_width() / 2 +
		setAllCardPos()
		transparent3(card_pos_info, card2img(player_hold[len(player_hold) - 1]), background_color, len(player_hold), 50)
		now += 1

	else:
		dealer_card_info = [redBackCard_image_filename, center_card[0], center_card[1]]
		dealer_hold.append(deck[deck_num[now]])
		card_num = len(dealer_hold)
		dealer_pos_info.append(dealer_card_info)

		while  dealer_pos_info[card_num - 1][1] < (game_window[0] - redBackCard_image.get_width()) / 2 + (card_num - 1) * (redBackCard_image.get_width() / 2 + 5):
			dealer_pos_info[card_num - 1][1] += speed
			setAllCardPos()
			allShow(background_color)
			#pygame.time.wait(1)
			screen.blit(hit_image, ((game_window[0] - hit_image.get_width()) / 2, (game_window[1] - hit_image.get_height()) / 2))
			pygame.display.update()
			if (game_window[0] - redBackCard_image.get_width()) / 2 + (card_num - 1) * (redBackCard_image.get_width() / 2 + 5) - dealer_pos_info[card_num - 1][1] < speed:
				dealer_pos_info[card_num - 1][1] = (game_window[0] - redBackCard_image.get_width()) / 2 + (card_num - 1) * (redBackCard_image.get_width() / 2 + 5)
				setAllCardPos()
				allShow(background_color)
				screen.blit(hit_image, ((game_window[0] - hit_image.get_width()) / 2, (game_window[1] - hit_image.get_height()) / 2))
				pygame.display.update()


		while dealer_pos_info[card_num - 1][2] > 0:
			dealer_pos_info[card_num - 1][2] -= speed
			if check != (redBackCard_image.get_width() / 2 + 5):
				for val in range(len(dealer_pos_info) - 1):
					dealer_pos_info[val][1] -= 1
				check += 1

			#pygame.time.wait(1)
			allShow(background_color)
			setAllCardPos()
			screen.blit(hit_image, ((game_window[0] - hit_image.get_width()) / 2, (game_window[1] - hit_image.get_height()) / 2))
			pygame.display.update()

			if dealer_pos_info[card_num - 1][2] < speed:
				dealer_pos_info[card_num - 1][2] = 0
				setAllCardPos()
				allShow(background_color)
				pygame.display.update()

		setAllCardPos()
		transparent3(card_pos_info, card2img(dealer_hold[len(dealer_hold) - 1]), background_color, len(card_pos_info) - 1, 50)
		now += 1
		Kev_sleep_millisecond2(1000)

def bustCheck(hold):
	global dealer_hold

	if total(hold) > 21:
		if len(dealer_hold) == 2:	#dont want to sleep after dealer's bust
			Kev_sleep_millisecond2(1000)
		allShow(background_color)
		screen.blit(bust_image, ((game_window[0] - bust_image.get_width()) / 2, (game_window[1] - bust_image.get_height()) / 2))
		pygame.display.update()
		Kev_sleep_millisecond2(1500)
		return True
	return False



def total(hold):
	ace = 0
	hold_result = 0
	for val in hold:
		hold_split = val.split(",")
		math = int(hold_split[1])
		if math > 10:
			math = 10
		if math == 1:
			ace = 1
		hold_result += math

	if hold_result < 12:
		if ace == 1:
			hold_result += 10

	return hold_result

def shuffle_check():
	global now
	global deck
	global deck_num

	if now > count - 10:
		now = 0
		random.shuffle(deck_num)
		screen.blit(deckShuffled_image, ((game_window[0] - deckShuffled_image.get_width()) / 2, (game_window[1] - deckShuffled_image.get_height()) / 2))
		pygame.display.update()
		Kev_sleep_millisecond2(1500)
		allShow(background_color)
		pygame.display.update()
		Kev_sleep_millisecond2(1000)


def game_ready_dealer():
	global now
	global deck
	global deck_num
    	global blackjack

	blackjack = [0,0]
	dealer_open = deck[deck_num[now]]
	now += 1
	dealer_hide = deck[deck_num[now]]
	now += 1

	dealer_hold = [dealer_open, dealer_hide]

	if total(dealer_hold) == 21:
		blackjack[0] = 1

	return dealer_hold

def game_ready_player():
	global now
	global deck
	global deck_num
	global blackjack

	player_open = deck[deck_num[now]]
	now += 1
	player_hide = deck[deck_num[now]]
	now += 1

	player_hold = [player_open, player_hide]

	if total(player_hold) == 21:
		blackjack[1] = 1

	return player_hold

def show(who, hold):
	player_total = total(hold)


	if who == 0:
		print hold[0], "|",
		for val in hold[1:]:
			print " ?  |",
		print

	elif who == 1:
		for val in hold:
			print  val, "|",
		print "   SUM = ", player_total
	else:
		print "ERROR 3"

def dealer_AI():
	global now
	global deck
	global deck_num
	global dealer_hold

	result = total(dealer_hold)
	if result < 17:
		get_one_card(1)
	else:
		return True

def youWin():
	allShow(background_color)
	screen.blit(youwin_image, ((game_window[0] - youwin_image.get_width()) / 2, (game_window[1] - youwin_image.get_height()) / 2))
	pygame.display.update()
	Kev_sleep_millisecond2(2000)

def youLose():
	allShow(background_color)
	screen.blit(youlose_image, ((game_window[0] - youlose_image.get_width()) / 2, (game_window[1] - youlose_image.get_height()) / 2))
	pygame.display.update()
	Kev_sleep_millisecond2(2000)

def draw():
	allShow(background_color)
	screen.blit(draw_image, ((game_window[0] - draw_image.get_width()) / 2, (game_window[1] - draw_image.get_height()) / 2))
	pygame.display.update()
	Kev_sleep_millisecond2(2000)

def gameResult():
	global player_hold
	global dealer_hold
	global player_bust
	global dealer_bust
	global blackjack

	dealer_count = 0
	player_count = 0
	player = total(player_hold)
	dealer = total(dealer_hold)

	if blackjack[0] == 1:
			allShow(background_color)
			screen.blit(blackjack_image, ((game_window[0] - blackjack_image.get_width()) / 2, (game_window[1] - blackjack_image.get_height()) / 2))
			pygame.display.update()
			Kev_sleep_millisecond2(2000)
			allShow(background_color)
			pygame.display.update()
			Kev_sleep_millisecond2(1000)
			youLose()

	elif player_bust == 1 or dealer_bust == 1:
		if player_bust == 0:	#player win
			youWin()
		elif dealer_bust == 0:	#dealer win
			youLose()
		else:	#draw
			draw()

	else:
		if player >  21 and dealer > 21:
			print "Error Code 1"

		elif player == dealer:
			for val in dealer_hold:
				dealer_count += 1
			for val in player_hold:
				player_count += 1

			if dealer_count == player_count:
				draw()
			elif dealer_count > player_count:
				youWin()
			else:
				youLose()
		elif player > dealer:
			youWin()
		else:
			youLose()

def reset():
	global i
	global j
	global val

	i = 0
	j = 0
	val = 0

Kev_sleep_millisecond2(1000)
pygame.display.update()

#-----------------------------Start Up-----------------------------------------------#

transparent2(loading_image_filename, "NONE", background_color, 0, 0)
#transparent(loading_image_filename, 1.5, 10, 1, background_color[0], background_color[1], background_color[2])
pygame.display.update()
Kev_sleep_millisecond2(500)

#start_image_setting = Image.open(start_image_filename)
#editor_image_setting = Image.open(editor_image_filename)

#screen.blit(start_image, (0, 0))
screen.blit(editor_image, ((game_window[0] - editor_image.get_width()) / 2, (game_window[1] - editor_image.get_height()) / 3))
pygame.display.update()
Kev_sleep_millisecond2(3000)

screen.blit(background_image, (0, 0))
pygame.display.update()
Kev_sleep_millisecond2(1000)
#screen.blit(background_image, (0, 0))
#screen.blit(start_image, ((game_window[0] - start_image.get_width()) / 2, (game_window[1] - start_image.get_height()) / 3))
#pygame.display.update()
#pygame.time.delay(3000)

pos1 = 0
card_change = 0
x1 = 0.0
y1 = 0.0
#pos2 = 1
#x2 = 0.0 + game_window[0] - redBackCard_image.get_width()
#y2 = 0.0
startFlag = 0

while True:
	while startFlag == 0:	#introduction
		now = 0
		now_time = datetime.datetime.today()
		screen.blit(background_image, (0, 0))

		if now_time.second % 2 == 0:
			screen.blit(startButton_image, ((game_window[0] - startButton_image.get_width()) / 2, (game_window[1] - startButton_image.get_height()) / 3 * 1.6))

		if pos1 == 0:
			x1 += 1
			if x1 + redBackCard_image.get_width() > game_window[0]:
				pos1 += 1
				card_change += 1

		elif pos1 == 1:
			y1 += 1
			if y1 + redBackCard_image.get_height() > game_window[1]:
				pos1 += 1
				card_change += 1

		elif pos1 == 2:
			x1 -= 1
			if x1 == 0:
				pos1 += 1
				card_change += 1

		elif pos1 == 3:
			y1 -= 1
			if y1 == 0:
				pos1 = 0
				card_change += 1

		if card_change > 12:
			card_change = 0

#		if pos2 == 0:
#			x2 += 1
#			if x2 + redBackCard_image.get_width() > game_window[0]:
#				pos2 += 1
#		elif pos2 == 1:
#				pos2 += 1
#		elif pos2 == 2:
#			x2 -= 1
#			if x2 == 0:
#				pos2 += 1
#		elif pos2 == 3:
#			y2 -= 1
#			if y2 == 0:
#				pos2 = 0

		screen.blit((Card1_image[card_change]), (x1, y1))
		screen.blit((Card2_image[card_change]), (abs(x1 - game_window[0]) - redBackCard_image.get_width(), y1))
		screen.blit((Card3_image[card_change]), (x1, abs(y1 - game_window[1] + redBackCard_image.get_height())))
		screen.blit((Card4_image[card_change]), (abs(x1 - game_window[0]) - redBackCard_image.get_width(), abs(y1 - game_window[1] + redBackCard_image.get_height())))
	#	screen.blit(redBackCard_image, (x2, y2))
	#	screen.blit(redBackCard_image, (abs(x2 - game_window[0]) - redBackCard_image.get_width(), abs(y2 - game_window[1] + redBackCard_image.get_height())))
		screen.blit(start_image, ((game_window[0] - start_image.get_width()) / 2, (game_window[1] - start_image.get_height()) / 3))

		pygame.time.delay(5)
		pygame.display.update()

		event = pygame.event.poll()	#Get event

		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				exit()
			if event.key == K_SPACE:
				startFlag = 1

 	while startFlag == 1:	#move all card to middle
		if x1 > game_window[0] / 2 -  redBackCard_image.get_width() / 2:
			x1 -= 1
		elif x1 < game_window[0] / 2 - redBackCard_image.get_width() / 2:
			x1 += 1
		if y1 > game_window[1] / 2 -  redBackCard_image.get_height() / 2:
			y1 -= 1
		elif y1 < game_window[1] / 2 - redBackCard_image.get_height() / 2:
			y1 += 1
		if x1 == game_window[0] / 2 -  redBackCard_image.get_width() / 2 and y1 == game_window[1] / 2 -  redBackCard_image.get_height() / 2:
			startFlag = 2

		screen.blit(background_image, (0, 0))

		screen.blit((Card1_image[card_change]), (x1, y1))
		screen.blit((Card2_image[card_change]), (abs(x1 - game_window[0]) - redBackCard_image.get_width(), y1))
		screen.blit((Card3_image[card_change]), (x1, abs(y1 - game_window[1] + redBackCard_image.get_height())))
		screen.blit((Card4_image[card_change]), (abs(x1 - game_window[0]) - redBackCard_image.get_width(), abs(y1 - game_window[1] + redBackCard_image.get_height())))

		pygame.time.delay(3)
		pygame.display.update()

	if startFlag == 2:	#transparent from card to backside
		x1 = 1
		y1 = 0
		center_card = centerPos(redBackCard_image_filename)
		transparent2(card2img(Card1[card_change]), redBackCard_image_filename, background_color, center_card[0],  center_card[1])
		startFlag = 3

		if startFlag == 3:
			reset()

#	for val in range(10):  #transparent
#		Kev_sleep_millisecond(100)
#		#pygame.time.wait(100)
#		transparent_activate(Card1_image[card_change], 1.5, 1)
#		screen.blit(redBackCard_image, (game_window[0] / 2 - redBackCard_image.get_width() / 2,  game_window[1] / 2 - redBackCard_image.get_height() / 2))
#		screen.blit(Card1_image[card_change], (game_window[0] / 2 - redBackCard_image.get_width() / 2,  game_window[1] / 2 - redBackCard_image.get_height() / 2))

#--------------------------------------------main start-------------------------------------------#

	while startFlag == 3:	#set player and dealer's hand
		if now > count - 4:	#deck shuffle
			now = 0
			random.shuffle(deck_num)
			screen.blit(deckShuffled_image, ((game_window[0] - deckShuffled_image.get_width()) / 2, (game_window[1] - deckShuffled_image.get_height()) / 3))
			pygame.display.update()
			Kev_sleep_millisecond2(500)

#		gameCardPos_x = [game_window[0] / 2 - redBackCard_image.get_width() - 10, game_window[0] / 2 + 10]
#		gameCardPos_y = [game_window[1] - redBackCard_image.get_height(), game_window[1] - redBackCard_image.get_height()]
		pos = [0, 0]
#		i += 1

#		gameCardPos_x.append(center_card[0])
#		gameCardPos_y.append(game_window[1] - redBackCard_image.get_height())

		for val in range((game_window[1] - redBackCard_image.get_height()) / 2):
			pos[0] += 1	#using pos in different way
			screen.blit(background_image, (0, 0))
			screen.blit((redBackCard_image), (center_card[0], center_card[1]))
			screen.blit((redBackCard_image), (center_card[0], center_card[1] + pos[0]))
			screen.blit((redBackCard_image), (center_card[0], center_card[1] - pos[0]))
			pygame.time.delay(1)
			pygame.display.update()

		while pos[1] < 5 + redBackCard_image.get_width() / 2: #using pos in different way
			pos[1] += 1
			screen.blit(background_image, (0, 0))
			screen.blit((redBackCard_image), (center_card[0], center_card[1]))
			screen.blit((redBackCard_image), (center_card[0] - pos[1], center_card[1] + pos[0]))	#left downside
			screen.blit((redBackCard_image), (center_card[0] + pos[1], center_card[1] + pos[0]))	#right downside
			screen.blit((redBackCard_image), (center_card[0] - pos[1], center_card[1] - pos[0]))	#left upside
			screen.blit((redBackCard_image), (center_card[0] + pos[1], center_card[1] - pos[0]))	#right upside
			pygame.time.delay(1)
			pygame.display.update()

		startFlag = 4
		reset()

	while startFlag == 4:	#open player and dealer's hand

		dealer_hold = game_ready_dealer()
		player_hold = game_ready_player()

		default_card_pos0 = [redBackCard_image_filename, center_card[0], center_card[1]]
		default_card_pos1 = [redBackCard_image_filename, center_card[0] - pos[1], center_card[1] + pos[0]]
		default_card_pos2 = [redBackCard_image_filename, center_card[0] + pos[1], center_card[1] + pos[0]]
		default_card_pos3 = [redBackCard_image_filename, center_card[0] - pos[1], center_card[1] - pos[0]]
		default_card_pos4 = [redBackCard_image_filename, center_card[0] + pos[1], center_card[1] - pos[0]]

		card_pos_info = [default_card_pos0, default_card_pos1, default_card_pos2, default_card_pos3, default_card_pos4]

		transparent3(card_pos_info, card2img(player_hold[0]), background_color, 1, 50) #left downside
		transparent3(card_pos_info, card2img(player_hold[1]), background_color, 2, 50) #right downside
		transparent3(card_pos_info, card2img(dealer_hold[0]), background_color, 3, 50) #left upside

		player_pos_info = [default_card_pos1, default_card_pos2]
		dealer_pos_info = [default_card_pos3, default_card_pos4]

		startFlag = 5
		reset()

	while startFlag == 5:	#determine blackjack or not
		if blackjack[0] == 1 and blackjack[1] == 1:	#Both player and dealer have blackjack
			Kev_sleep_millisecond2(1000)
			allShow(background_color)
			screen.blit(blackjack_image, ((game_window[0] - blackjack_image.get_width()) / 2, (game_window[1] - blackjack_image.get_height()) / 2))
			pygame.display.update()
			Kev_sleep_millisecond2(2000)

			allShow(background_color)
			pygame.display.update()
			Kev_sleep_millisecond2(1000)

			transparent3(card_pos_info, card2img(dealer_hold[1]), background_color, 4, 50)
			Kev_sleep_millisecond2(1000)

			screen.blit(blackjack_image, ((game_window[0] - blackjack_image.get_width()) / 2, (game_window[1] - blackjack_image.get_height()) / 2))
			pygame.display.update()
			Kev_sleep_millisecond2(2000)

			allShow(background_color)
			pygame.display.update()
			Kev_sleep_millisecond2(1000)

			allShow(background_color)
			screen.blit(draw_image, ((game_window[0] - draw_image.get_width()) / 2, (game_window[1] - draw_image.get_height()) / 2))
			pygame.display.update()
			Kev_sleep_millisecond2(2000)

			allShow(background_color)
			pygame.display.update()
			Kev_sleep_millisecond2(1000)

			player_action = 2
			startFlag = 9

		#elif blackjack[0] == 1:	#Dealer has blackjack
		#	print "--Dealer's Hand--"
		#	show(1, dealer_hold)
		#	print "--Player's Hand--"
		#	show(1, player_hold)
		#	print "Dealer has blackjack!!!"
		#	player_action = 2
		#	startFlag = 6

		elif blackjack[1] == 1:	#Player has blackjack
			Kev_sleep_millisecond2(1000)
			allShow(background_color)
			screen.blit(blackjack_image, ((game_window[0] - blackjack_image.get_width()) / 2, (game_window[1] - blackjack_image.get_height()) / 2))
			pygame.display.update()
			Kev_sleep_millisecond2(2000)

			allShow(background_color)
			pygame.display.update()
			Kev_sleep_millisecond2(1000)

			transparent3(card_pos_info, card2img(dealer_hold[1]), background_color, 4, 50)
			Kev_sleep_millisecond2(1000)

			screen.blit(youwin_image, ((game_window[0] - youwin_image.get_width()) / 2, (game_window[1] - youwin_image.get_height()) / 2))
			pygame.display.update()
			Kev_sleep_millisecond2(2000)

			allShow(background_color)
			pygame.display.update()
			Kev_sleep_millisecond2(1000)

			player_action = 2
			startFlag = 9
		else:
			startFlag = 6

	while startFlag == 6:	#player's turn
		player_bust = False
		allShow(background_color)
		screen.blit(hitorstand_image, ((game_window[0] - hitorstand_image.get_width()) / 2, (game_window[1] - hitorstand_image.get_height()) / 2))
		pygame.display.update()

		event = pygame.event.poll()	#Get event
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		if event.type == KEYDOWN:
			if event.key == K_h:
				get_one_card(0)	#player = 0, dealer = 1
				#Kev_sleep_millisecond2(500)

				if bustCheck(player_hold) == True:
					startFlag += 1
					player_bust = 1
					allShow(background_color)
					pygame.display.update()
					Kev_sleep_millisecond2(1000)
					allShow(background_color)
					screen.blit(dealerTurn_image, ((game_window[0] - dealerTurn_image.get_width()) / 2, (game_window[1] - dealerTurn_image.get_height()) / 2))
					pygame.display.update()
					Kev_sleep_millisecond2(1500)
					allShow(background_color)
					pygame.display.update()
					Kev_sleep_millisecond2(1000)

			elif event.key == K_s:
				startFlag += 1
				allShow(background_color)
				pygame.display.update()
				Kev_sleep_millisecond2(1000)
				allShow(background_color)
				screen.blit(dealerTurn_image, ((game_window[0] - dealerTurn_image.get_width()) / 2, (game_window[1] - dealerTurn_image.get_height()) / 2))
				pygame.display.update()
				Kev_sleep_millisecond2(1500)
				allShow(background_color)
				pygame.display.update()
				Kev_sleep_millisecond2(1000)
			else:
				print "Not allowed"

	while startFlag == 7:	#Dealer's turn
		if first_check == 0:
			transparent3(card_pos_info, card2img(dealer_hold[1]), background_color, len(card_pos_info) - 1, 50)
			first_check += 1
			dealer_bust = False
			Kev_sleep_millisecond2(1000)

		if dealer_AI() == True:
			if bustCheck(dealer_hold) == True:
				dealer_bust = 1
				startFlag += 1
				first_check = 0
			else:
				#Kev_sleep_millisecond2(1500)
				screen.blit(stand_image, ((game_window[0] - stand_image.get_width()) / 2, (game_window[1] - stand_image.get_height()) / 2))
				pygame.display.update()
				Kev_sleep_millisecond2(1500)
				startFlag += 1
				first_check = 0

	while startFlag == 8: #check result
		allShow(background_color)
		pygame.display.update()
		Kev_sleep_millisecond2(2000)
		gameResult()
		startFlag += 1
		allShow(background_color)
		pygame.display.update()
		Kev_sleep_millisecond2(1000)

	while startFlag == 9:	# continue check
		shuffle_check()
		allShow(background_color)
		screen.blit(continue_image, ((game_window[0] - continue_image.get_width()) / 2, (game_window[1] - continue_image.get_height()) / 2))
		pygame.display.update()

		event = pygame.event.poll()	#Get event

		for event in pygame.event.get():
			if event.type == QUIT:
				exit()


		if event.type == KEYDOWN:
			if event.key == K_y:
				startFlag += 1
			elif event.key == K_n:
				startFlag = 0
			else:
				print "Not allowed"

	while startFlag == 10: #move out all cards
		for val in range(1, len(player_pos_info) + 1):
			card_pos_info[val][1] -= 4
		for val in range(len(player_pos_info) + 1, len(card_pos_info)):
			card_pos_info[val][1] += 4

		if len(dealer_hold) > len(player_hold):
			if card_pos_info[len(player_pos_info) + 1][1] > game_window[0]:
				startFlag = 3
		else:
			if card_pos_info[len(player_hold)][1] + redBackCard_image.get_width() < 0:
				startFlag = 3

		setAllCardPos()
		allShow(background_color)
		pygame.display.update()
