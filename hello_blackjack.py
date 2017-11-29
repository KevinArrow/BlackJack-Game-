#!/usr/bin/evn python

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
start_image_filename = "./img/start.png"
editor_image_filename = "./img/editor.png"
startButton_image_filename = "./img/startButton.png"

#loading images

loading_image = pygame.image.load(loading_image_filename).convert()
debug_image = pygame.image.load(debug_image_filename).convert_alpha()
background_image = pygame.image.load(background_image_filename).convert()
start_image = pygame.image.load(start_image_filename).convert_alpha()
editor_image = pygame.image.load(editor_image_filename).convert_alpha()
startButton_image = pygame.image.load(startButton_image_filename).convert_alpha()

#screen setting

screen.blit(loading_image, (0, 0))
pygame.display.update()

#-----------------------------Game Setting Start---------------------------------------#

Card1 = ['C,01','C,02','C,03','C,04','C,05','C,06','C,07','C,08','C,09','C,10','C,11','C,12','C,13']
Card2 = ['D,01','D,02','D,03','D,04','D,05','D,06','D,07','D,08','D,09','D,10','D,11','D,12','D,13']
Card3 = ['H,01','H,02','H,03','H,04','H,05','H,06','H,07','H,08','H,09','H,10','H,11','H,12','H,13']
Card4 = ['S,01','S,02','S,03','S,04','S,05','S,06','S,07','S,08','S,09','S,10','S,11','S,12','S,13']

lined_deck = Card1 + Card2 + Card3 + Card4
deck = 4 * (Card1 + Card2 + Card3 + Card4)
count = 0
for val in deck:
	count += 1
deck_num = range(0, count)
random.shuffle(deck_num)

'''
#debug deck
card1 = ["S,10","S,10","S,10","S,10","S,5","S,5"]
count = 0
for val in card1:
	count += 1
deck = card1
deck_num = range(0,count)
#debug deck done
'''
now = 0
blackjack = [0, 0]

def card2img(card):
	card_id = card.split(",")
	card_img = "./img/card/half_png/" + card_id[0].lower() + card_id[1] + ".png"
	return card_img

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

for val in range(13):
	Card1_image.append(pygame.image.load(card2img(Card1[val])).convert_alpha())
	Card2_image.append(pygame.image.load(card2img(Card2[val])).convert_alpha())
	Card3_image.append(pygame.image.load(card2img(Card3[val])).convert_alpha())
	Card4_image.append(pygame.image.load(card2img(Card4[val])).convert_alpha())

#-------------------------------------Load End--------------------------------#


def transparent(fade_image, fade_speed, count, fadeInOut, R_color, G_color, B_color): #Default fade_speed = 1.5, count = 10
	pygame.init()

	screen = pygame.display.set_mode((game_window[0], game_window[1]), 0, 32)

	alpha_surface = pygame.image.load(fade_image).convert_alpha()

	for val in range(count):
		pygame.time.wait(100)
		screen.fill((R_color, G_color, B_color))
		transparent_activate(alpha_surface, fade_speed, fadeInOut)
		screen.blit(alpha_surface,(0,0))
		pygame.display.update()

		for e in pygame.event.get():
			if e.type == QUIT:
				return

def transparent_activate(surface, fade_speed, fadeInOut):
	uialpha = pygame.surfarray.pixels_alpha(surface)
	if fadeInOut == 1:
		uialpha /= fade_speed
	else:
		uialpha *= 1.2
	del uialpha


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

	if now == count:
		now = 0
		random.shuffle(deck_num)
		print "\n---Deck Shuffled---\n"
		time.sleep(1)

def game_ready_dealer():
	global now
	global deck
	global deck_num
	global blackjack

	blackjack = [0,0]
	dealer_open = deck[deck_num[now]]
	now += 1
	shuffle_check()
	dealer_hide = deck[deck_num[now]]
	now += 1
	shuffle_check()

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
	shuffle_check()
	player_hide = deck[deck_num[now]]
	now += 1
	shuffle_check()

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

def dealer_AI(hold):
	global now
	global deck
	global deck_num
	result = total(hold)

	print "--Dealer's Hand--"
	show(1, dealer_hold)
	print "--Player's Hand--"
	show(1, player_hold)
	print 		#Line break for easily viewable
	time.sleep(1)


	while result < 17:
		hold.append(deck[deck_num[now]])
		now += 1
		result = total(hold)

		print "--Dealer's Hand--"
		show(1, dealer_hold)
		print "--Player's Hand--"
		show(1, player_hold)
		print 		#Line break for easily viewable
		shuffle_check()
		time.sleep(1)

	return hold

def gameResult(dealer_hold, player_hold):
	dealer_count = 0
	player_count = 0
	dealer = total(dealer_hold)
	player = total(player_hold)

	if player >  21 and dealer > 21:
		print "Error Code 1"
	elif player == dealer:
		for val in dealer_hold:
			dealer_count += 1
		for val in player_hold:
			player_count += 1

		if dealer_count == player_count:
			print "Draw"
		elif dealer_count > player_count:
			print "You Win!!!"
		else:
			print "You Lose..."
	elif player > 21:
		print "Error Code 2"
	elif dealer > 21:
		print "Dealer's Bust.  You Win!!!"
	elif dealer < player:
		print "You Win!!!"
	else:
		print "You Lose"

time.sleep(2)

pygame.display.update()

#-----------------------------Start Up-----------------------------------------------#

transparent(loading_image_filename, 1.5, 10, 1, background_color[0], background_color[1], background_color[2])

pygame.display.update()
time.sleep(0.5)

#start_image_setting = Image.open(start_image_filename)
#editor_image_setting = Image.open(editor_image_filename)

#screen.blit(start_image, (0, 0))
screen.blit(editor_image, ((game_window[0] - editor_image.get_width()) / 2, (game_window[1] - editor_image.get_height()) / 3))
pygame.display.update()
pygame.time.delay(3000)

screen.blit(background_image, (0, 0))
pygame.display.update()
pygame.time.delay(1000)
#screen.blit(background_image, (0, 0))
#screen.blit(start_image, ((game_window[0] - start_image.get_width()) / 2, (game_window[1] - start_image.get_height()) / 3))
#pygame.display.update()
#pygame.time.delay(3000)

pos1 = 0
card_change = 0
x1 = 0.0
y1 = 0.0
#pos2 = 1
#x2 = 0.0 + game_window[0] - debug_image.get_width()
#y2 = 0.0

while True:
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
		now_time = datetime.datetime.today()

		screen.blit(background_image, (0, 0))

		if now_time.second % 2 == 0:
			screen.blit(startButton_image, ((game_window[0] - startButton_image.get_width()) / 2, (game_window[1] - startButton_image.get_height()) / 3 * 1.6))

		if pos1 == 0:
			x1 += 1
			if x1 + debug_image.get_width() > game_window[0]:
				pos1 += 1
				card_change += 1

		elif pos1 == 1:
			y1 += 1
			if y1 + debug_image.get_height() > game_window[1]:
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

	#	if pos2 == 0:
	#		x2 += 1
	#		if x2 + debug_image.get_width() > game_window[0]:
	#			pos2 += 1
	#	elif pos2 == 1:
	#			pos2 += 1
	#	elif pos2 == 2:
	#		x2 -= 1
	#		if x2 == 0:
	#			pos2 += 1
	#	elif pos2 == 3:
	#		y2 -= 1
	#		if y2 == 0:
	#			pos2 = 0

		screen.blit((Card1_image[card_change]), (x1, y1))
		screen.blit((Card2_image[card_change]), (abs(x1 - game_window[0]) - debug_image.get_width(), y1))
		screen.blit((Card3_image[card_change]), (x1, abs(y1 - game_window[1] + debug_image.get_height())))
		screen.blit((Card4_image[card_change]), (abs(x1 - game_window[0]) - debug_image.get_width(), abs(y1 - game_window[1] + debug_image.get_height())))
	#	screen.blit(debug_image, (x2, y2))
	#	screen.blit(debug_image, (abs(x2 - game_window[0]) - debug_image.get_width(), abs(y2 - game_window[1] + debug_image.get_height())))
		screen.blit(start_image, ((game_window[0] - start_image.get_width()) / 2, (game_window[1] - start_image.get_height()) / 3))

		time.sleep(0.005)
		pygame.display.update()

