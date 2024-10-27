import pgzrun
import random

WIDTH = 640
HEIGHT = 360

music.play('8-bit-music-on-245249')

vx = 4 
vy = 4

game_over = False
begin = False
score = 0

kunai_holdoff = 0
kunais = []
floors = []
platformies = []
enemies = []

ninja = Actor('idle__000')
ninja.pos = 32, HEIGHT - 95 #505

background = Actor('grass')

play = Actor('play')
play.pos = 530, 15
play_position = play.pos

music_sound = Actor('music_sound')
music_sound.pos = 555, 15

# floor
for x in range(2):
	for y in range(1):
		floor = Actor('floor') #width: 200; height: 30
		floor.x = x * 300 + 150
		floor.y = HEIGHT - 33
		floors.append(floor)

# platform
	platform = Actor('ground')
	platform.x = WIDTH - 450
	platform.y = HEIGHT - 150
	platformies.append(platform)

	platform = Actor('ground')
	platform.x = 250
	platform.y = 50
	platformies.append(platform) 

def update():
	global vx, vy, kunai_holdoff, game_over, enemy_1, velocity_y, score, begin, play_position
	
	# For the enemy
	if random.randint(0, 50) == 0:
		
		if int(ninja.x) > 0:
			enemy_1 = Actor('pokermad')
			enemy_1.x = random.randint(int(ninja.x + 100), WIDTH)
			enemy_1.y = HEIGHT - 95
			enemies.append(enemy_1)						

			enemy_2 = Actor('barnacle')
			enemy_2.x = random.randint(int(ninja.x + 100), WIDTH)
			enemy_2.y = HEIGHT - 95
			enemies.append(enemy_2)		

	if keyboard.left:

		if ninja.image == 'run__000' or ninja.image == 'run__001' or ninja.image == 'run__002' or ninja.image == 'run__003' or ninja.image == 'run__004' or ninja.image == 'run__005' or ninja.image == 'run__006' or ninja.image == 'run__007' or ninja.image == 'run__008' or ninja.image == 'run__009' or ninja.image == 'attack__005' or ninja.image == 'idle__000':
			ninja.image = 'r_run__000'

		if ninja.image == 'r_run__000':
			ninja.image = 'r_run__001'
		elif ninja.image == 'r_run__001':
			ninja.image = 'r_run__002'
		elif ninja.image == 'r_run__002':
			ninja.image = 'r_run__003'
		elif ninja.image == 'r_run__003':
			ninja.image = 'r_run__004'
		elif ninja.image == 'r_run__004':
			ninja.image = 'r_run__005'
		elif ninja.image == 'r_run__005':
			ninja.image = 'r_run__006'
		elif ninja.image == 'r_run__006':
			ninja.image = 'r_run__007'
		elif ninja.image == 'r_run__007':
			ninja.image = 'r_run__008'
		elif ninja.image == 'r_run__008':
			ninja.image = 'r_run__009'
		elif ninja.image == 'r_run__009':
			ninja.image = 'r_run__000'

		ninja.x -= 2

	if keyboard.right:

		if ninja.image == 'r_run__000' or ninja.image == 'r_run__001' or ninja.image == 'r_run__002' or ninja.image == 'r_run__003' or ninja.image == 'r_run__004' or ninja.image == 'r_run__005' or ninja.image == 'r_run__006' or ninja.image == 'r_run__007' or ninja.image == 'r_run__008' or ninja.image == 'r_run__009' or ninja.image == 'attack__005' or ninja.image == 'idle__000':
			ninja.image = 'run__000'

		if ninja.image == 'run__000':
			ninja.image = 'run__001'
		elif ninja.image == 'run__001':
			ninja.image = 'run__002'
		elif ninja.image == 'run__002':
			ninja.image = 'run__003'
		elif ninja.image == 'run__003':
			ninja.image = 'run__004'
		elif ninja.image == 'run__004':
			ninja.image = 'run__005'
		elif ninja.image == 'run__005':
			ninja.image = 'run__006'
		elif ninja.image == 'run__006':
			ninja.image = 'run__007'
		elif ninja.image == 'run__007':
			ninja.image = 'run__008'
		elif ninja.image == 'run__008':
			ninja.image = 'run__009'
		elif ninja.image == 'run__009':
			ninja.image = 'run__000'

		ninja.x += 2

	if keyboard.lctrl:

		if ninja.image == 'run__000' or ninja.image == 'run__001' or ninja.image == 'run__002' or ninja.image == 'run__003' or ninja.image == 'run__004' or ninja.image == 'run__005' or ninja.image == 'run__006' or ninja.image == 'run__007' or ninja.image == 'run__008' or ninja.image == 'run__009':
			on_key_down()
			on_key_up()
		if ninja.image == 'r_run__000' or ninja.image == 'r_run__001' or ninja.image == 'r_run__002' or ninja.image == 'r_run__003' or ninja.image == 'r_run__004' or ninja.image == 'r_run__005' or ninja.image == 'r_run__006' or ninja.image == 'r_run__007' or ninja.image == 'r_run__008' or ninja.image == 'r_run__009':
			on_key_down()
			on_key_up()

	if keyboard.up:
		ninja.image = 'jump__004'
		original_y = ninja.y
		ninja.y -= vy

	if keyboard.down:
		ninja.image = 'glide_006'
				
		if ninja.colliderect(floor):
			ninja.y = 100
		else:
			ninja.y += vy

	if kunai_holdoff == 0:
		if keyboard.space:
			ninja.image = 'throw__004'

			kunai = Actor('kunai')
			kunai.x = ninja.x + 35
			kunai.y = ninja.y	
			sounds.kunai.play()
			kunais.append(kunai)
			kunai_holdoff = 10			
	else:
		kunai_holdoff = kunai_holdoff - 1
		
	for kunai in kunais:
		kunai.x = kunai.x + 5

		for enemy_1 in enemies:
			if kunai.colliderect(enemy_1) and game_over == False:
				sounds.destroy.play()
				score += 1
				
				if enemy_1 in enemies:				
					enemies.remove(enemy_1)
				if kunai in kunais:
					kunais.remove(kunai)

			for enemy_2 in enemies:
				if kunai.colliderect(enemy_2) and game_over == False:
					sounds.destroy.play()
					score += 1
					
					if enemy_2 in enemies:	
						enemies.remove(enemy_2)

					if kunai in kunais:
						kunais.remove(kunai)			
		
def on_key_down():
	if keyboard.lctrl:
		ninja.image = 'attack__005'
def on_key_up():
	ninja.image = 'idle__000'

def on_mouse_down():
    if play.collidepoint(play):
        begin = True
    else:
        print("You missed me!")

def draw():
	global score, game_over
	if game_over == False:		
		background.draw()
		ninja.draw()
		play.draw()
		music_sound.draw()
		screen.draw.text('Score: ' + str(score), (10, 10), color=(255,255,255), fontsize=30)

		for kunai in kunais:
			kunai.draw()

		for floor in floors:
			floor.draw()

		for platform in platformies:
			platform.draw()
	
		for enemy_1 in enemies:
			enemy_1.draw()
			enemy_1.x -= 2

			if ninja.colliderect(enemy_1):
				if score > 0:
					score -= 1
				else:
					game_over = True	
		
		for enemy_2 in enemies:
			enemy_2.draw()
			enemy_2.x -= 1

			if ninja.colliderect(enemy_2):
				if score > 0:
					score -= 1
				else:
					game_over = True
	else:
		screen.draw.text('Game Over', (360, 300), color=(255,255,255), fontsize=60)
		screen.draw.text('Score: ' + str(score), (260, 150), color=(255,255,255), fontsize=60)
			
pgzrun.go()