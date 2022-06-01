extends Node2D



var game_paused = false


func _ready():
	pass 

func _process(delta):
	
	
	#pausing
	if Input.is_action_just_pressed("ui_cancel") and game_paused == false:
		get_tree().paused = true
		game_paused = true
		$Caretaker/Control.show()
		Input.set_mouse_mode(Input.MOUSE_MODE_CONFINED)
	elif Input.is_action_just_pressed("ui_cancel") and game_paused == true:
		Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
		get_tree().paused = false
		game_paused = false
		$Caretaker/Control.hide()
		


