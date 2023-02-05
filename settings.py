# global variables
ghosts_killed = 0
bosses_killed = 0
bosses_to_spawn = 1

# Screen Settings
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920
SCREEN_TITLE = "The Cistern"
PLAYING_FIELD_WIDTH = SCREEN_WIDTH - 50
PLAYING_FIELD_HEIGHT = SCREEN_HEIGHT - 50

# Speeds
CAMERA_SPEED = 0.9
PLAYER_MOVEMENT_SPEED = 1
PLAYER_RUN_SPEED_MODIFIER = 1.8
SLASH_SPEED_MODIFIER = 0.15
SLASH_CHARGE_SPEED_MODIFIER = 0.8
SWORDSLASH_PROJECTILE_SPEED = 2.4
FLAMESLASH_PROJECTILE_SPEED = 1.5 * SWORDSLASH_PROJECTILE_SPEED
MONSTER_MOVEMENT_SPEED = 1.1
SPELL_MOVEMENT_SPEED = 1
BOSS_MOVEMENT_SPEED = 1

# Timing Settings
SWORDSLASH_FPS = 1/70
SLASH_CHARGE_TIME = 0.05

# Sizes
SPOTLIGHT_SIZE = 500
MONSTER_VISION_RANGE = 340
SPRITE_SCALING = 0.25
PLAYER_SCALING = 0.4
MONSTER_SCALING = 0.5
SWORDSLASH_SCALING = 0.35
FLAMESLASH_SCALING = 0.5
HEART_SCALING = 0.1
BOSS_SCALING = 0.35

# Alpha
GHOST_ALPHA = 210

# Health settings
HEART_HEALTH = 20
PLAYER_STARTING_HEALTH = 40
BOSS_HEALTH = 60

# Volume settings
MUSIC_VOLUME = 0.3
SWOOSH_VOLUME = 0.2
