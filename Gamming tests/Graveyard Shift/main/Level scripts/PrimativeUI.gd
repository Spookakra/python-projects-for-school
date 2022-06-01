extends Control


onready var game_data = SaveFile.game_data

# Called when the node enters the scene tree for the first time.
func _ready():
#	print(save_file.ammo)
	pass



# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Button_pressed():
	game_data.ammo += 20
