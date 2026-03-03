# // Define LCD cat sprites //
""" 
Sprites are to be drawn on the LCD screen 
according to the cats stats 
"""

# Colours
blue = 27965
black = 0
white = 65535
pink = 64765
yellow = 65317
green = 36495

# Sprites
def cat_standing(x, y):  # x, y to adjust position on screen   
    # Draw Head
    LCD1IN8.draw_rectangle(75 + x, 44 + y, 105 + x, 64 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    
    # Draw Outer Ears
    LCD1IN8.draw_rectangle(75 + x, 39 + y, 85 + x, 44 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(100 + x, 39 + y, 105 + x, 44 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    
    # Draw Inner Ears
    LCD1IN8.draw_rectangle(80 + x, 44 + y, 85 + x, 49 + y, pink, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(100 + x, 44 + y, 105 + x, 49 + y, pink, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Whiskers
    LCD1IN8.draw_rectangle(70 + x, 49 + y, 75 + x, 54 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(70 + x, 59 + y, 75 + x, 64 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    
    LCD1IN8.draw_rectangle(105 + x, 54 + y, 110 + x, 59 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(110 + x, 49 + y, 115 + x, 54 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(110 + x, 59 + y, 115 + x, 64 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Eyes
    LCD1IN8.draw_rectangle(85 + x, 54 + y, 90 + x, 59 + y, yellow, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(100 + x, 54 + y, 105 + x, 59 + y, yellow, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Neck
    LCD1IN8.draw_rectangle(80 + x, 64 + y, 100 + x, 79 + y, white, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Body
    LCD1IN8.draw_rectangle(60 + x, 69 + y, 75 + x, 84 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(80 + x, 69 + y, 85 + x, 79 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(85 + x, 74 + y, 90 + x, 79 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(95 + x, 74 + y, 100 + x, 79 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(85 + x, 79 + y, 100 + x, 84 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(75 + x, 69 + y, 80 + x, 79 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Legs
    LCD1IN8.draw_rectangle(60 + x, 84 + y, 65 + x, 89 + y, white, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(70 + x, 84 + y, 75 + x, 89 + y, white, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(85 + x, 84 + y, 90 + x, 89 + y, white, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(95 + x, 84 + y, 100 + x, 89 + y, white, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Tail
    LCD1IN8.draw_rectangle(55 + x, 69 + y, 60 + x, 74 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(50 + x, 54 + y, 55 + x, 69 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(55 + x, 49 + y, 60 + x, 54 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

def cat_sitting(x, y):  # x, y to adjust position on screen    
    # Draw Head
    LCD1IN8.draw_rectangle(75 + x, 44 + y, 105 + x, 64 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    
    # Draw Outer Ears
    LCD1IN8.draw_rectangle(75 + x, 39 + y, 85 + x, 44 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(100 + x, 39 + y, 105 + x, 44 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    
    # Draw Inner Ears
    LCD1IN8.draw_rectangle(80 + x, 44 + y, 85 + x, 49 + y, pink, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(100 + x, 44 + y, 105 + x, 49 + y, pink, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Whiskers
    LCD1IN8.draw_rectangle(70 + x, 49 + y, 75 + x, 54 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(70 + x, 59 + y, 75 + x, 64 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    
    LCD1IN8.draw_rectangle(105 + x, 54 + y, 110 + x, 59 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(110 + x, 49 + y, 115 + x, 54 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(110 + x, 59 + y, 115 + x, 64 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Eyes
    LCD1IN8.draw_rectangle(85 + x, 54 + y, 90 + x, 59 + y, yellow, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(100 + x, 54 + y, 105 + x, 59 + y, yellow, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Neck
    LCD1IN8.draw_rectangle(80 + x, 64 + y, 100 + x, 79 + y, white, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Body
    LCD1IN8.draw_rectangle(80 + x, 69 + y, 85 + x, 79 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(85 + x, 74 + y, 90 + x, 79 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(95 + x, 74 + y, 100 + x, 79 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(85 + x, 79 + y, 100 + x, 84 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(75 + x, 69 + y, 80 + x, 84 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(60 + x, 74 + y, 75 + x, 84 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Legs
    LCD1IN8.draw_rectangle(80 + x, 79 + y, 85 + x, 84 + y, white, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(100 + x, 79 + y, 105 + x, 84 + y, white, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Tail
    LCD1IN8.draw_rectangle(55 + x, 69 + y, 60 + x, 74 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(50 + x, 54 + y, 55 + x, 69 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(55 + x, 49 + y, 60 + x, 54 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

def cat_sleeping(x, y):  # x, y to adjust position on screen
    # Draw Head
    LCD1IN8.draw_rectangle(80 + x, 64 + y, 110 + x, 84 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    
    # Draw Outer Ears
    LCD1IN8.draw_rectangle(80 + x, 59 + y, 90 + x, 64 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(105 + x, 59 + y, 110 + x, 64 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    
    # Draw Inner Ears
    LCD1IN8.draw_rectangle(85 + x, 64 + y, 90 + x, 69 + y, pink, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(105 + x, 64 + y, 110 + x, 69 + y, pink, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Whiskers
    LCD1IN8.draw_rectangle(75 + x, 69 + y, 80 + x, 74 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(75 + x, 79 + y, 80 + x, 84 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    
    LCD1IN8.draw_rectangle(110 + x, 74 + y, 115 + x, 79 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(115 + x, 69 + y, 120 + x, 74 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(115 + x, 79 + y, 120 + x, 84 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Eyes
    LCD1IN8.draw_rectangle(90 + x, 74 + y, 95 + x, 76 + y, yellow, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(105 + x, 74 + y, 110 + x, 76 + y, yellow, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Body
    LCD1IN8.draw_rectangle(75 + x, 69 + y, 80 + x, 84 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(60 + x, 74 + y, 75 + x, 84 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

    # Draw Tail
    LCD1IN8.draw_rectangle(55 + x, 69 + y, 60 + x, 74 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(50 + x, 54 + y, 55 + x, 69 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(55 + x, 49 + y, 60 + x, 54 + y, black, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)

def background():
    LCD1IN8.draw_rectangle(0, 0, 160, 128, blue, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_rectangle(0, 110, 160, 128, green, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.LCD_Display()

# // Define LED emotes //
"""
Emotes to be displayed on the microbit's LED screen,
according to its stats (e.g. High happiness = happy emote)
"""
def cat_emote():
    basic.show_leds("""
        . . . . .
        . # . # .
        . # # # .
        . # # # .
        . . . . .
        """)
    basic.pause(1000)
    basic.clear_screen()

def happy_emote():
    basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)
    basic.pause(3000)
    basic.clear_screen()

def sad_emote():
    basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    . # # # .
    # . . . #
    """)
    basic.pause(3000)
    basic.clear_screen()

def neutral_emote():
    basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # # # # #
    . . . . .
    """)
    basic.pause(3000)
    basic.clear_screen()

def angry_emote():
    basic.show_leds("""
    # . . . #
    # # . # #
    . . . . .
    . # # # .
    # . . . #
    """)
    basic.pause(3000)
    basic.clear_screen()

def sleepy_emote():
    basic.show_string("zzzzzzz...")
    basic.pause(5000)

# // Define sounds //
music.set_built_in_speaker_enabled(True)

def happyMeow():
    music.play(music.create_sound_expression(WaveShape.SQUARE,
            1,
            1259,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)

def sadMeow():
    music.play(music.create_sound_expression(WaveShape.SQUARE,
            1233,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)

def angryMeow():
    music.play(music.create_sound_expression(WaveShape.NOISE,
            2742,
            3689,
            255,
            0,
            500,
            SoundExpressionEffect.TREMOLO,
            InterpolationCurve.CURVE),
        music.PlaybackMode.UNTIL_DONE)

# // Initialise screen //
LCD1IN8.LCD_ClearBuf(0)
LCD1IN8.LCD_Init()
LCD1IN8.LCD_Clear()
LCD1IN8.LCD_SetBL(0)

# // Display home screen //
LCD1IN8.direct_dis_string(55, 60, "ByteCat", white)
LCD1IN8.direct_dis_string(5, 115, "Hold B to start.", white)
LCD1IN8.LCD_Display()

# Wait for user to press 'B' to begin game
while (True):
    if (input.button_is_pressed(Button.B)):
        happyMeow()
        break;

# // Begin game //
cat_emote()
LCD1IN8.LCD_ClearBuf(0)
LCD1IN8.LCD_Clear()
LCD1IN8.LCD_Display()

# // Setup cat //
class Cat:
    def __init__(self):
        # Set stats of cat
        self.min_stats = 0
        self.max_stats = 100

        self.happiness = 100
        self.hunger = 100
        self.energy = 100

        # Track how much the user can pet the cat
        self.min_petCount = 0
        self.max_petCount = 3
        self.petCount = 0

        """
        At less than 25 energy, recovering is set to True,
        and the cat begins sleeping.

        At 75 and above energy, the cat wakes up and recovering
        is set to False.

        This avoids an infinite loop for energy
        where the cat sleeps for only 10 minutes,
        only to lose enough energy again 10 minutes later
        and start sleeping, repeat. 
        
        ByteCat can enjoy a proper nap.
        """
        self.recovering = False

        # Stat decrease interval (10 minutes)
        minutes = 10
        self.stat_timer = (minutes * 60) * 1000
        
        """
        Happiness - time to reach 0 depends on other stats
        Hunger - 8 hours to reach 0
        Energy - 16 hours to reach 0
        """
        
    # Update screen with current stats
    def display_stats(self):        
        LCD1IN8.direct_draw_rectangle(0, 0, 160, 34, blue, DRAW_FILL.DRAW_FULL, DOT_PIXEL.DOT_PIXEL_1)
        LCD1IN8.direct_dis_string(5, 1, "Happiness: " + self.happiness, white)
        LCD1IN8.direct_dis_string(5, 11, "Hunger: " + self.hunger, white)
        LCD1IN8.direct_dis_string(5, 21, "Energy: " + self.energy, white)

    # Update stats in background
    def update_stats(self):
        # Decreases cat's stats over time and updates its state
        self.hunger -= 2
        self.energy -= 1
        self.petCount -= 1

        # Update happiness based on hunger
        if (self.hunger >= 75):  # Well fed
            self.happiness += 3
        elif (self.hunger < 75 and self.hunger > 25):  # Moderate hunger
            self.happiness -= 1
        elif (self.hunger <= 25):  # Starving
            self.happiness -= 3

        # Update state based on energy
        if (self.energy < 25):  # Sleepy
            recovering = True  # Sleep until 75 energy
            self.sleep()
        elif (self.energy > 75 and recovering == True):
            recovering = False
            self.check_emotion()
        else:
            self.check_emotion()
        
        """ 
        Prevent stats exceeding limits
        (Checks and returns stat if value is greater than 0 and less than 100,
        otherwise, returns min or max as the new value)
        """
        self.happiness = max(self.min_stats, min(self.happiness, self.max_stats))
        self.hunger = max(self.min_stats, min(self.hunger, self.max_stats))
        self.energy = max(self.min_stats, min(self.energy, self.max_stats))
        self.petCount = max(self.min_petCount, min(self.petCount, self.max_petCount))

        self.draw_sprite()

    def draw_sprite(self):    
        # Refresh stats display
        LCD1IN8.LCD_ClearBuf(0)
        background()

        # Draw cat sprite based on energy
        if (self.energy > 50):
            cat_standing(0, 21)
        elif (self.energy > 25 and self.energy <= 50):
            cat_sitting(0, 26)
        else:
            cat_sleeping(0, 26)

        self.display_stats()
        LCD1IN8.LCD_Display()

    def sleep(self):
        if (self.recovering == True):
            self.energy += 2

    def sleepy_emote_display(self):
        if (self.recovering == True):
            sleepy_emote()

    def check_emotion(self):
        if (self.happiness >= 75):
            happy_emote()
            happyMeow()
        elif (self.happiness <= 25):
            sad_emote()
            sadMeow()
        else:
            neutral_emote()

# // Create ByteCat //
# Create instance of cat
byte_cat = Cat()

""" 
Makecode doesn't support @staticmethods
So a global function is needed
"""
def byte_cat_update_stats():
    byte_cat.update_stats()
def byte_cat_sleepy_emote_display():
    byte_cat.sleepy_emote_display()

# Every 10 minutes, update and display stats
loops.every_interval(byte_cat.stat_timer, byte_cat_update_stats)

# Display 'zzzz...' every 10 seconds if cat is sleepy
loops.every_interval(10000, byte_cat_sleepy_emote_display)

# // Define buttons //
# (Shake)
def pet_cat():
    if (byte_cat.petCount < byte_cat.max_petCount):
        byte_cat.happiness += 3
        byte_cat.petCount += 1

        byte_cat.happiness = max(byte_cat.min_stats, min(byte_cat.happiness, byte_cat.max_stats))
        byte_cat.petCount = max(byte_cat.min_petCount, min(byte_cat.petCount, byte_cat.max_petCount))

        happyMeow()
        basic.show_icon(IconNames.HEART)
        byte_cat.draw_sprite()
        basic.pause(1000)
        basic.clear_screen()


    else:
        angryMeow()
        basic.show_string("ByteCat doesn't want any more pets!")

# (A)
def feed_cat():
    if (byte_cat.recovering == False):
        byte_cat.hunger += 30
        
        byte_cat.hunger = max(byte_cat.min_stats, min(byte_cat.hunger, byte_cat.max_stats))
        
        happyMeow()
        happy_emote()
        byte_cat.draw_sprite()

    else:
        angryMeow()
        basic.show_string("ByteCat is asleep!")

# (B)
def play_with_cat():
    if (byte_cat.recovering == False):
        byte_cat.happiness += 10
        byte_cat.hunger -= 5
        byte_cat.energy -= 20
        happyMeow()
        happy_emote()
        byte_cat.draw_sprite()

        byte_cat.happiness = max(byte_cat.min_stats, min(byte_cat.happiness, byte_cat.max_stats))
        byte_cat.hunger = max(byte_cat.min_stats, min(byte_cat.hunger, byte_cat.max_stats))
        byte_cat.energy = max(byte_cat.min_stats, min(byte_cat.energy, byte_cat.max_stats))
    
    else:
        angryMeow()
        basic.show_string("ByteCat is asleep!")

# // Begin input loop //
def game_loop():
    # SHAKE: Pet cat
    if (input.is_gesture(Gesture.SHAKE)):
        pet_cat()
        byte_cat.display_stats()
    
    # A: Feed cat
    elif (input.button_is_pressed(Button.A)):
        feed_cat()
        byte_cat.display_stats()

    # B: Play with cat
    elif (input.button_is_pressed(Button.B)):
        play_with_cat()
        byte_cat.display_stats()
loops.every_interval(200, game_loop)